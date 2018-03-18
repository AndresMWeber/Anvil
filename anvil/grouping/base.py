from six import iteritems, itervalues
import nomenclate
import anvil
import anvil.log as log
import anvil.runtime as rt
import anvil.config as cfg
from anvil.utils.generic import Map, gen_flatten_dict_depth_two
import anvil.objects.attribute as at
from anvil.meta_data import MetaData
from anvil.utils.generic import merge_dicts
from anvil.decorators import register_built_nodes, generate_build_report


class AbstractGrouping(log.LogMixin):
    """ A fully functional and self-contained rig with all requirements implemented that
        are required to give a performance.

    """
    LOG = log.obtain_logger(__name__)
    ANVIL_TYPE = cfg.RIG_TYPE
    BUILT_IN_NAME_TOKENS = MetaData({cfg.TYPE: cfg.GROUP_TYPE, cfg.NAME: 'untitled'}, protected=cfg.TYPE)
    BUILT_IN_META_DATA = MetaData()
    BUILT_IN_ATTRIBUTES = MetaData({})
    RENDERING_ATTRIBUTES = MetaData({
        '%ss' % cfg.SURFACE_TYPE: at.DISPLAY_KWARGS,
        '%ss' % cfg.JOINT_TYPE: merge_dicts(at.DISPLAY_KWARGS, {cfg.DEFAULT_VALUE: 2}),
        '%ss' % cfg.NODE_TYPE: at.DISPLAY_KWARGS,
        '%ss' % cfg.CONTROL_TYPE: merge_dicts(at.DISPLAY_KWARGS, {cfg.DEFAULT_VALUE: 1}),
        '%s' % cfg.LOD: merge_dicts(at.DISPLAY_KWARGS, {cfg.ENUM_NAME: 'Hero:Proxy'})
    })
    BUILD_REPORT_KEYS = [cfg.CONTROL_TYPE, cfg.JOINT_TYPE, cfg.NODE_TYPE]

    def __init__(self, layout_joints=None, parent=None, top_node=None, name_tokens=None, meta_data=None, **kwargs):
        self.hierarchy = Map()
        self.root = top_node
        self.layout_joints = layout_joints
        self.build_joints = None
        self.build_kwargs = MetaData(kwargs)
        self.name_tokens = self.BUILT_IN_NAME_TOKENS.merge(name_tokens, new=True)
        self.meta_data = self.BUILT_IN_META_DATA.merge(meta_data, new=True)

        self._nomenclate = nomenclate.Nom(self.name_tokens.data)
        self.chain_nomenclate = nomenclate.Nom()

        for namer in [self._nomenclate, self.chain_nomenclate]:
            namer.format = cfg.RIG_FORMAT
            namer.var.case = cfg.UPPER

        self.parent(parent)

    @property
    def is_built(self):
        return all([self.root])

    def build(self, joints=None, meta_data=None, name_tokens=None, **kwargs):
        self.build_kwargs.merge(kwargs)
        self.meta_data.merge(meta_data)
        self.name_tokens.merge(name_tokens)
        self.build_joints = joints or self.layout_joints

    def build_layout(self):
        raise NotImplementedError

    @register_built_nodes
    @generate_build_report
    def register_node(self, node, **kwargs):
        print('registering node manually %s' % node, kwargs)
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

    def rename_chain(self, nodes, use_end_naming=False, **name_tokens):
        self.chain_nomenclate.merge_dict(self.name_tokens.merge(name_tokens))

        for index, object in enumerate(nodes):
            variation_kwargs = {'var': index}
            if use_end_naming and index == len(nodes) - 1:
                variation_kwargs = {'decorator': 'End'}
            rt.dcc.scene.rename(object, self.chain_nomenclate.get(**variation_kwargs))

    def rename(self, *input_dicts, **kwargs):
        new_tokens = MetaData(*input_dicts, **kwargs)
        self.name_tokens.merge(new_tokens)
        self._nomenclate.merge_dict(**self.name_tokens.data)
        self._cascade_across_hierarchy(lambda n: n.rename(self._nomenclate.get(**n.name_tokens.update(new_tokens))),
                                       lambda n: n.rename(self.name_tokens, n.name_tokens))

    @register_built_nodes
    @generate_build_report
    def build_node(self, node_class, *args, **kwargs):
        try:
            build_function = kwargs.pop('build_fn')
        except KeyError:
            build_function = 'build'
        kwargs[cfg.NAME_TOKENS] = self.name_tokens.merge(kwargs.get(cfg.NAME_TOKENS, {}), new=True)
        kwargs[cfg.META_DATA] = self.meta_data.merge(kwargs.get(cfg.META_DATA, {}), new=True)
        return getattr(node_class, build_function)(*args, **kwargs)

    def auto_color(self):
        self._cascade_across_hierarchy(lambda n: n.auto_color() if hasattr(n, 'auto_color') else None,
                                       lambda n: n.auto_color() if hasattr(n, 'auto_color') else None)

    def find_node(self, node_key, category_override=None):
        """ This will only work with user specified hierarchy IDs.
            Otherwise it will not detect the node key from the default node list.

        :param node_key: str, node key we are looking for within the hierarchy initial sets
        :param category_override: str, if there are double keys we can add granularity and specify the initial key.
        """
        try:
            if category_override:
                return self.hierarchy[category_override][node_key]
            for sub_hierarchy in itervalues(self.hierarchy):
                candidate = sub_hierarchy.get(node_key)
                if candidate:
                    return candidate
        except:
            raise KeyError('Node from key %s not found in hierarchy' % (
                '.'.join([category_override, node_key]) if category_override else node_key))

    def _update_hierarchy(self, hierarchy_id, candidate):
        print('updating hierarchy from %s->%s' % (hierarchy_id, candidate))
        if isinstance(candidate, tuple):
            candidate = Map([(candidate[0], candidate[1])])
        elif isinstance(candidate, dict):
            candidate = Map(candidate)
        print('regsitering node %s in hierarchy %s' % (candidate, hierarchy_id))

        try:
            hierarchy_entry = self.hierarchy[hierarchy_id]

            # TODO: This breaks the Map hierarchy.
            if issubclass(type(hierarchy_entry), dict) and issubclass(type(candidate), dict):
                print('dictionary updating')
                hierarchy_entry.deep_update(candidate)

            elif isinstance(hierarchy_entry, list):
                if isinstance(candidate, list):
                    print('extending')
                    hierarchy_entry.extend(candidate)
                else:
                    print('appending')
                    hierarchy_entry.append(candidate)
            else:
                print('assigning straight up new list')
                self.hierarchy[hierarchy_id] = [hierarchy_entry, candidate]

        except KeyError:
            print('no previous key, assigning as node')
            self.hierarchy[hierarchy_id] = candidate

        print('hierarchy is now', self.hierarchy)

    def _flat_hierarchy(self):
        return gen_flatten_dict_depth_two(self.hierarchy)

    def _cascade_across_hierarchy(self, object_function, grouping_function):
        for sub_node in itervalues(self.hierarchy):
            for anvil_node in itervalues(sub_node):
                for node in anvil_node if anvil.is_aset(anvil_node) else [anvil_node]:
                    if anvil.is_agrouping(node):
                        grouping_function(node)
                    elif anvil.is_aobject(node):
                        object_function(node)

    def __getattr__(self, item):
        try:
            return super(AbstractGrouping, self).__getattribute__('hierarchy')[item]
        except KeyError:
            return super(AbstractGrouping, self).__getattribute__(item)

    def __str__(self):
        try:
            if self.root is None:
                raise KeyError
            return str(self.root)
        except (KeyError, AttributeError):
            return super(AbstractGrouping, self).__str__()

    def __repr__(self):
        formatted_properties = ' root=%s children=%d>' % (self.root, len(list(self.hierarchy)))
        return super(AbstractGrouping, self).__repr__().replace('>', formatted_properties)

    def __dir__(self):
        return dir(super(AbstractGrouping, self)) + list(self.hierarchy)
