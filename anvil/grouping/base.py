import nomenclate
from six import iteritems
import anvil.objects as ot
from six import iteritems
import anvil
import anvil.runtime as rt


class AbstractGrouping(object):
    """ A fully functional and self-contained rig with all requirements implemented that
        are required to give a performance.

    """
    ANVIL_TYPE = 'group'
    LOG = anvil.log.obtainLogger(__name__)
    BUILT_IN_META_DATA = {'type': ANVIL_TYPE}
    DEFAULT_ATTRS = {'surfaces': {'attributeType': 'enum',
                                  'enumName': 'off:on:template:reference',
                                  'keyable': True,
                                  'defaultValue': 0},
                     'joints': {'attributeType': 'enum',
                                'enumName': 'off:on:template:reference',
                                'keyable': True,
                                'defaultValue': 2},
                     'nodes': {'attributeType': 'enum',
                               'enumName': 'off:on:template:reference',
                               'keyable': True,
                               'defaultValue': 0},
                     'controls': {'attributeType': 'enum',
                                  'enumName': 'off:on:template:reference',
                                  'keyable': True,
                                  'defaultValue': 1},
                     'lod': {'attributeType': 'enum', 'enumName': 'Hero:Proxy', 'keyable': True, 'defaultValue': 0}}

    def __init__(self, layout_joints=None, meta_data=None, parent=None, top_node=None, **flags):
        print('setting root to %s' % top_node)
        self.root = top_node
        self.layout_joints = layout_joints
        self.hierarchy = {}
        self.flags = flags or {}
        self.meta_data = self.merge_dicts(self.BUILT_IN_META_DATA, meta_data)
        self._nomenclate = nomenclate.Nom(self.meta_data)
        self.chain_nomenclate = nomenclate.Nom()
        self.chain_nomenclate.format = 'side_location_nameDecoratorVar_childtype_purpose_type'
        self.chain_nomenclate.var.case = 'upper'
        self.parent(parent)
        self.LOG.info('%r.__init__(top_node=%s, parent=%s, meta_data=%s)' % (self, top_node, parent, meta_data))

    @property
    def is_built(self):
        return all([self.root])

    @staticmethod
    def merge_dicts(*input_dicts):
        """ Merge dictionaries. Rightmost dictionary overwrites all previous overlapping keys.

        :param input_dicts: list(dict), list of input dictionaries
        :return: dict, resulting dictionary.
        """
        result = {}
        if input_dicts:
            for input_dict in input_dicts:
                if isinstance(input_dict, dict):
                    result.update(input_dict)
        return result

    def build(self, parent=None):
        self.parent(parent)

    def build_layout(self):
        raise NotImplementedError

    def assign_rendering_delegate(self, assignee=None):
        # TODO: I Think this should be a part of the plugins section as it is very API dependent.
        assignee = anvil.factory(assignee) if assignee is not None else self.root
        self.LOG.info('Assigning/Connecting display attributes to %s' % assignee)
        for attr, attr_kwargs in iteritems(self.DEFAULT_ATTRS):
            attr_name, group_name = '%s_rendering' % attr, 'group_%s' % attr
            assignee.addAttr(attr_name, **attr_kwargs)
            if hasattr(self, group_name):
                target_group, display_attr = getattr(self, group_name), getattr(assignee, attr_name)
                target_group.overrideEnabled.set(1)
                display_attr.connect(target_group.visibility, force=True)
                assignee.buffer_connect(attr_name, target_group.overrideDisplayType, -1, force=True)

    def parent(self, new_parent):
        top_node, new_parent = str(self.root), str(new_parent)
        nodes_exist = [rt.dcc.scene.exists(node) if node != 'None' else False for node in [top_node, new_parent]]
        if all(nodes_exist or [False]):
            self.LOG.info('Parenting root of %r to %s' % (self, new_parent))
            rt.dcc.scene.parent(top_node, new_parent)
            return True
        else:
            self.LOG.warning('Parent(%s) -> %r does not exist.' % (new_parent, top_node))
            return False

    def rename_chain(self, objects, **name_tokens):
        self.LOG.info('Renaming chain %r...' % (self))
        self.chain_nomenclate.merge_dict(self.merge_dicts(self.meta_data, name_tokens))

        for index, object in enumerate(objects):
            variation_kwargs = {'var': index} if index != len(objects) - 1 else {'decorator': 'End'}
            rt.dcc.scene.rename(str(object), self.chain_nomenclate.get(**variation_kwargs))

    def rename(self, *input_dicts, **name_tokens):
        self.LOG.debug('Renaming %r...' % (self))
        self.meta_data.update(self.merge_dicts(*(input_dicts + (name_tokens,))))
        self._nomenclate.merge_dict(**self.meta_data)

        # Sub node is going to be either subtype of grouping or objects.
        for sub_node_key, sub_node in iteritems(self.hierarchy):
            if self.node_is_grouping(sub_node):
                sub_node.rename(self.merge_dicts(self.meta_data, sub_node.meta_data))

            elif self.node_is_object(sub_node):
                sub_node.rename(self._nomenclate.get(**sub_node.meta_data))

            self.LOG.debug('Renamed to %r' % (sub_node))

    def node_is_grouping(self, node):
        return issubclass(type(node), AbstractGrouping)

    def node_is_object(self, node):
        return issubclass(type(node), ot.UnicodeDelegate)

    def build_node(self, node_class, node_key, meta_data=None, **flags):
        self.LOG.info('build_node %r.%s = %s(meta_data=%s, flags=%s)' % (self, node_key, node_class, meta_data, flags))
        dag_node = node_class.build(meta_data=self.merge_dicts(self.meta_data, meta_data), **flags)
        self.register_node(node_key, dag_node)
        return dag_node

    def register_node(self, node_key, dag_node, parent=False, overwrite=True, meta_data=None):
        if dag_node is None:
            self.LOG.warning('Attempted register node %s with key %s but it does not exist' % (dag_node, node_key))
            return

        try:
            anvil.factory(dag_node)
        except:
            raise TypeError('Could not register unrecognized node type %s is not an anvil grouping or object class.')

        if self.hierarchy.get(node_key) is not None and not overwrite:
            raise IndexError('Preexisting node already is stored under key %s in the hierarchy' % node_key)

        self.hierarchy[node_key] = dag_node

        meta_data_dicts = [self.meta_data, meta_data or {}]
        try:
            meta_data_dicts.append(dag_node.meta_data)
        except:
            pass

        dag_node.meta_data = self.merge_dicts(*meta_data_dicts)

        return dag_node

    def find_node(self, node_key):
        try:
            return self.hierarchy[node_key]
        except:
            raise KeyError('Node from key %s not found in hierarchy' % node_key)

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
