from six import iteritems
import nomenclate
import anvil
import anvil.log as log
import anvil.runtime as rt
import anvil.config as cfg
import anvil.objects.attribute as at
import anvil.objects as ot
from anvil.meta_data import MetaData
from anvil.utils.generic import merge_dicts


class AbstractGrouping(log.LogMixin):
    """ A fully functional and self-contained rig with all requirements implemented that
        are required to give a performance.

    """
    LOG = log.obtainLogger(__name__)
    ANVIL_TYPE = cfg.GROUP_TYPE
    BUILT_IN_NAME_TOKENS = MetaData({cfg.TYPE: ANVIL_TYPE, cfg.NAME: 'untitled'}, protected=cfg.TYPE)
    BUILT_IN_META_DATA = MetaData()
    BUILT_IN_ATTRIBUTES = MetaData({})
    RENDERING_ATTRIBUTES = MetaData({
        '%ss' % cfg.SURFACE_TYPE: at.DISPLAY_KWARGS,
        '%ss' % cfg.JOINT_TYPE: merge_dicts(at.DISPLAY_KWARGS, {cfg.DEFAULT_VALUE: 2}),
        '%ss' % cfg.NODE_TYPE: at.DISPLAY_KWARGS,
        '%ss' % cfg.CONTROL_TYPE: merge_dicts(at.DISPLAY_KWARGS, {cfg.DEFAULT_VALUE: 1}),
        '%s' % cfg.LOD: merge_dicts(at.DISPLAY_KWARGS, {cfg.ENUM_NAME: 'Hero:Proxy'})
    })

    def __init__(self, layout_joints=None, parent=None, top_node=None, name_tokens=None, meta_data=None, **kwargs):
        self.hierarchy = {}
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

    def parent(self, new_parent):
        nodes_exist = [rt.dcc.scene.exists(node) if node != None else False for node in [self.root, new_parent]]
        if all(nodes_exist or [False]):
            self.root.parent(new_parent)
            return True
        else:
            self.warning('Parent(%s) -> %r does not exist.', new_parent, self.root)
            return False

    def rename_chain(self, objects, use_end_naming=False, **name_tokens):
        self.chain_nomenclate.merge_dict(self.name_tokens.merge(name_tokens))

        for index, object in enumerate(objects):
            variation_kwargs = {'var': index}
            if use_end_naming and index == len(objects) - 1:
                variation_kwargs = {'decorator': 'End'}
            rt.dcc.scene.rename(object, self.chain_nomenclate.get(**variation_kwargs))

    def rename(self, *input_dicts, **kwargs):
        new_tokens = MetaData(*input_dicts, **kwargs)
        self.name_tokens.merge(new_tokens)
        self._nomenclate.merge_dict(**self.name_tokens.data)
        self._cascading_function(lambda n:
                                 n.rename(self._nomenclate.get(**n.name_tokens.update(new_tokens))),
                                 lambda n:
                                 n.rename(self.name_tokens, n.name_tokens))

    def build_node(self, node_class, node_key, build_fn='build', *args, **kwargs):
        kwargs[cfg.NAME_TOKENS] = self.name_tokens.merge(kwargs.get(cfg.NAME_TOKENS, {}), new=True)
        kwargs[cfg.META_DATA] = self.meta_data.merge(kwargs.get(cfg.META_DATA, {}), new=True)
        dag_node = getattr(node_class, build_fn)(*args, **kwargs)
        self.register_node(node_key, dag_node)
        return dag_node

    def insert_transform_buffer(self, node_to_buffer, **kwargs):
        name_tokens = kwargs.get(cfg.NAME_TOKENS) or node_to_buffer.name_tokens
        buffer = ot.Transform.build(parent=node_to_buffer, name_tokens=name_tokens, **kwargs)
        buffer.transform.set((0,0,0))
        buffer.parent(node_to_buffer.get_parent())
        return buffer


    def register_node(self, node_key, dag_node, overwrite=True, name_tokens=None, meta_data=None):
        if dag_node is None:
            self.warning('Attempted register node %s with key %s but it does not exist', dag_node, node_key)
            return
        try:
            anvil.factory(dag_node)
        except:
            raise TypeError('Could not register unrecognized node type %s is not an anvil grouping or object class.')

        if self.hierarchy.get(node_key) is not None and not overwrite:
            raise IndexError('Preexisting node already is stored under key %s in the hierarchy' % node_key)

        self.hierarchy[node_key] = dag_node
        dag_node.meta_data.merge(self.meta_data, meta_data)
        dag_node.name_tokens.merge(self.name_tokens, name_tokens)
        return dag_node

    def auto_color(self, *args, **kwargs):
        auto_colorer = lambda n: n.auto_color() if hasattr(n, 'auto_color') else None
        self._cascading_function(auto_colorer, auto_colorer)

    def find_node(self, node_key):
        try:
            return self.hierarchy[node_key]
        except:
            raise KeyError('Node from key %s not found in hierarchy' % node_key)

    def _cascading_function(self, object_function, grouping_function):
        for sub_key, sub_node in iteritems(self.hierarchy):
            if anvil.is_agrouping(sub_node):
                grouping_function(sub_node)
            elif anvil.is_aobject(sub_node):
                object_function(sub_node)

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
        _ = (self.root, len(list(self.hierarchy)), self.meta_data, self.name_tokens)
        formatted_properties = ' root=%s children=%d meta_data=%s name_tokens=%s>' % _
        return super(AbstractGrouping, self).__repr__().replace('>', formatted_properties)

    def __dir__(self):
        return dir(super(AbstractGrouping, self)) + list(self.hierarchy)
