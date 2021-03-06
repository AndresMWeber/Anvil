from functools import wraps
from six import iteritems, itervalues
import nomenclate
import anvil
import anvil.log as log
import anvil.runtime as rt
import anvil.config as cfg
import anvil.objects.attribute as at
from anvil.meta_data import MetaData
from anvil.utils.generic import merge_dicts, to_size_list, to_list, Map


class NomenclateMixin(object):
    def __init__(self):
        self.nomenclate = nomenclate.Nom(format_string=cfg.RIG_FORMAT)
        self.nomenclate.var.case = cfg.UPPER

        self.chain_nomenclate = nomenclate.Nom(format_string=cfg.RIG_FORMAT)
        self.chain_nomenclate.var.case = cfg.UPPER

    def rename_chain(self, nodes, use_end_naming=True, **kwargs):
        self.chain_nomenclate.merge_dict(kwargs)
        total_length = len(nodes)
        for index, node in enumerate(nodes):
            variation_kwargs = {'var': index}
            if use_end_naming and index == total_length - 1:
                variation_kwargs = {'decorator': 'End'}
            node.rename(self.nomenclate.get(**variation_kwargs))


def register_built_nodes(f):
    """Decorator to automatically register nodes formatted for induction by generate_build_report.

    This function automatically digests a dictionary formatted build report of all nodes created and returned
    during function 'f'.  They will be added to the existing dict object self.hierarchy which is a dot notation
    searchable dictionary subclass.  Any additional dictionary objects that are nested will be converted
    to bunch objects.

    Depends on all build node functions being comprised of a dictionary with str keys with the structure:
    {'controls': ..., 'joints': ..., 'nodes': ...}

    Operations based on input/existing types:
        (existing entry, new entry)
        - list, list: it will extend the list with the new list
        - list, object: adds the object to the list
        - dict, dict: it will update the existing dict with new dict
        - object, object: converts the entry to a list

    If there is no existing entry then we will just assign it.
    """

    @wraps(f)
    def wrapper(abstract_grouping, *args, **kwargs):
        skip_register = kwargs.pop('skip_register', False)
        results = f(abstract_grouping, *args, **kwargs)
        if skip_register:
            return results
        abstract_grouping.hierarchy.deep_update(results)
        return results

    return wrapper


def generate_build_report(f):
    @wraps(f)
    def wrapper(abstract_grouping, *args, **kwargs):
        """Creates a dictionary of created nodes that will be digested later by the node registration function.

        A build report looks like this:
            {'control': {'default': [anvil_controls_or_set_of_controls, ...]},
             'node': {'default': [anvil_nodes_or_set_of_nodes, ...],
                      'user custom hierarchy id': node}},
             'set': {'default': None},
             'joint': {'default': None},

        A top level key will not be present if the report nodes from the wrapped function are not of that type.
        The top level key possibilities are: ['control', 'joint', 'node', 'set']

        :param args: object, node to sort into the hierarchy, SHOULD be an Anvil node.
        :param kwargs: dict, use kwargs if you want to override the types.
                             By default accepts any key from abstract_grouping.BUILD_REPORT_KEYS
        :return:
        """
        skip_report = kwargs.pop('skip_report', False)
        custom_hierarchy_ids = kwargs.pop(cfg.ID_TYPE, None)
        nodes_built = f(abstract_grouping, *args, **kwargs)

        if skip_report:
            return nodes_built

        report = {}
        nodes_built = [nodes_built] if anvil.is_achunk(nodes_built) else to_list(nodes_built)
        for node, hierarchy_id in zip(nodes_built, to_size_list(custom_hierarchy_ids, len(nodes_built))):
            tag = getattr(node, cfg.ANVIL_TYPE, cfg.NODE_TYPE)
            if hierarchy_id:
                # We are assuming the extra tag is unique and we can just do a plain update instead of checking.
                report.update({tag: {hierarchy_id: node}})
            else:
                # Otherwise we auto tag the node and add to the default list under that tag.
                report[tag] = report.get(tag, {cfg.DEFAULT: []})
                report[tag][cfg.DEFAULT].append(node)
        return report

    return wrapper


class AbstractGrouping(log.LogMixin, NomenclateMixin):
    """A group of nodes with all requirements implemented that are required to give a performance."""

    LOG = log.obtain_logger(__name__)
    ANVIL_TYPE = cfg.RIG_TYPE
    BUILT_IN_META_DATA = MetaData({cfg.TYPE: cfg.GROUP_TYPE, cfg.NAME: 'untitled'}, protected=cfg.TYPE)
    BUILT_IN_ATTRIBUTES = MetaData({})
    RENDERING_ATTRIBUTES = MetaData({
        '%ss' % cfg.SURFACE_TYPE: at.DISPLAY_KWARGS,
        '%ss' % cfg.JOINT_TYPE: merge_dicts(at.DISPLAY_KWARGS, {cfg.DEFAULT_VALUE: 2}),
        '%ss' % cfg.NODE_TYPE: at.DISPLAY_KWARGS,
        '%ss' % cfg.CONTROL_TYPE: merge_dicts(at.DISPLAY_KWARGS, {cfg.DEFAULT_VALUE: 1}),
        '%s' % cfg.LOD: merge_dicts(at.DISPLAY_KWARGS, {cfg.ENUM_NAME: 'Hero:Proxy'})
    })
    BUILD_REPORT_KEYS = [cfg.CONTROL_TYPE, cfg.JOINT_TYPE, cfg.NODE_TYPE]

    def __init__(self, layout_joints=None, parent=None, top_node=None, meta_data=None, **kwargs):
        super(AbstractGrouping, self).__init__()
        self.hierarchy = Map()
        self.root = top_node
        self.layout_joints = layout_joints
        self.build_kwargs = MetaData(kwargs)
        self.build_joints = None
        self.meta_data = self.BUILT_IN_META_DATA.merge(meta_data, new=True)
        self.parent(parent)

    @property
    def is_built(self):
        return all([self.root])

    def build(self, joints=None, meta_data=None, **kwargs):
        self.build_kwargs.merge(kwargs)
        self.meta_data.merge(meta_data)
        self.build_joints = joints or self.layout_joints

    def build_layout(self):
        raise NotImplementedError

    @register_built_nodes
    @generate_build_report
    def register_node(self, node, **kwargs):
        return node

    def connect_rendering_delegate(self, assignee=None):
        # TODO: API Attribute dependent...dangerous.
        assignee = anvil.factory(assignee) if assignee is not None else self.root

        for attr, attr_kwargs in iteritems(self.RENDERING_ATTRIBUTES):
            attr_name = '%s_rendering' % attr
            group_name = 'group_%s' % attr

            rendering_attribute = assignee.add_attr(attr_name, **attr_kwargs)

            if hasattr(self, group_name):
                target_group = getattr(self, group_name)
                target_group.overrideEnabled.set(1)
                rendering_attribute.connect(target_group.visibility, force=True)
                assignee.buffer_connect(attr_name, target_group.overrideDisplayType, -1, force=True)

    def initialize_sub_rig_attributes(self, controller=None, attr_dict=None):
        attr_dict = self.BUILT_IN_ATTRIBUTES if attr_dict is None else attr_dict
        if attr_dict:
            controller = self.root if controller is None else anvil.factory(controller)
            for attr, attr_kwargs in iteritems(attr_dict):
                controller.add_attr(attr, **attr_kwargs)

    def parent(self, new_parent, override_root=None):
        nodes_exist = [rt.dcc.scene.exists(node) if node is not None else False for node in
                       [override_root or self.root, new_parent]]
        if all(nodes_exist or [False]):
            (override_root or self.root).parent(new_parent)
            return True
        else:
            self.warning('Parent(%s) -> %r does not exist.', new_parent, override_root or self.root)
            return False

    def rename(self, *input_dicts, **kwargs):
        new_tokens = MetaData(*input_dicts, **kwargs)
        self.meta_data.merge(new_tokens)
        self.nomenclate.merge_dict(**self.meta_data.data)
        self._cascade_across_hierarchy(lambda n: n.rename(self.nomenclate.get(**n.meta_data.update(new_tokens))),
                                       lambda n: n.rename(self.meta_data, n.meta_data))

    @register_built_nodes
    @generate_build_report
    def build_node(self, node_class, *args, **kwargs):
        try:
            build_function = kwargs.pop('build_fn')
        except KeyError:
            build_function = 'build'
        kwargs[cfg.META_DATA] = self.meta_data.merge(kwargs.get(cfg.META_DATA, {}), new=True)
        return getattr(node_class, build_function)(*args, **kwargs)

    def auto_color(self):
        self._cascade_across_hierarchy(lambda n: n.auto_color() if hasattr(n, 'auto_color') else None,
                                       lambda n: n.auto_color() if hasattr(n, 'auto_color') else None)

    def find_node(self, node_key, category_override=None):
        """Finds a node within a hierarchy.

        This will only work with user specified hierarchy IDs. Otherwise it will not detect the node key from the
        default node list.

        :param node_key: str, node key we are looking for within the hierarchy initial sets
        :param category_override: str, if there are double keys we can add granularity and specify the initial key.
        """
        try:
            if category_override:
                return self.hierarchy[category_override][node_key]
            return self.hierarchy.to_flat_dict()[node_key]
        except KeyError:
            raise KeyError('Node from key %s not found in hierarchy' % (
                '.'.join([category_override, node_key]) if category_override else node_key))

    def _update_hierarchy(self, hierarchy_id, candidate):
        """Merges candidate input with the entry under the given hierarchy_id.

        :param hierarchy_id: str, key value for the hierarchy ID.
        :param candidate: anvil.object.UnicodeDelegate, should be an Anvil type.
        """
        if isinstance(candidate, tuple):
            candidate = Map([(candidate[0], candidate[1])])
        elif isinstance(candidate, dict):
            candidate = Map(candidate)

        try:
            hierarchy_entry = self.hierarchy[hierarchy_id]

            if issubclass(type(hierarchy_entry), dict) and issubclass(type(candidate), dict):
                hierarchy_entry.deep_update(candidate)

            elif isinstance(hierarchy_entry, list):
                if isinstance(candidate, list):
                    hierarchy_entry.extend(candidate)
                else:
                    hierarchy_entry.append(candidate)
            else:
                self.hierarchy[hierarchy_id] = [hierarchy_entry, candidate]

        except KeyError:
            self.hierarchy[hierarchy_id] = candidate

    def _flat_hierarchy(self):
        return self.hierarchy.flatten()

    def _cascade_across_hierarchy(self, object_function, grouping_function):
        print('Running a function across the hierarchy:')
        from pprint import pprint
        pprint(self.hierarchy)
        for anvil_node in itervalues(self.hierarchy.to_flat_dict()):
            print('running on node %r' % anvil_node)
            for node in [anvil_node] if anvil.is_achunk(anvil_node) or anvil.is_agrouping(anvil_node) else to_list(
                    anvil_node):
                try:
                    print('\tnode %s->%s' % (node, node.meta_data))
                except AttributeError:
                    print('node did not have name tokens...', node)

                if anvil.is_agrouping(node) or anvil.is_achunk(anvil_node):
                    grouping_function(node)
                elif anvil.is_aobject(node):
                    object_function(node)
                try:
                    print('\t\tnow it is: %s' % node)
                except:
                    print('for some stupid reason could not format:', type(node))

    def __getattr__(self, item):
        """Returns a hierarchy object if accessing the hierarchy, otherwise default methodology."""
        try:
            return super(AbstractGrouping, self).__getattribute__(cfg.HIERARCHY_TYPE)[item]
        except KeyError:
            return super(AbstractGrouping, self).__getattribute__(item)

    def __str__(self):
        """Returns the name of the root if it is set, otherwise uses super method"""
        try:
            return str(self.root)
        except (KeyError, AttributeError):
            return super(AbstractGrouping, self).__str__()

    def __repr__(self):
        """Adds number of children and the root transform to default repr."""
        formatted_properties = ' root=%s children=%d>' % (self.root, len(list(self.hierarchy)))
        return super(AbstractGrouping, self).__repr__().replace('>', formatted_properties)

    def __dir__(self):
        """Adds hierarchy of nodes to the dir printout."""
        return dir(super(AbstractGrouping, self)) + list(self.hierarchy)
