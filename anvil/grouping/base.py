import nomenclate
import anvil.objects as ot
from six import iteritems
import anvil
import anvil.runtime as rt


class AbstractGrouping(object):
    """ A fully functional and self-contained rig with all requirements implemented that
        require it to give a performance.

    """
    ANVIL_TYPE = 'group'
    LOG = anvil.log.obtainLogger(__name__)

    def __init__(self, layout=None, meta_data=None, parent=None, top_node=None, **flags):
        self.top_node = top_node
        self.layout = layout
        self.hierarchy = {}
        self.flags = flags or {}
        self.meta_data = self.merge_dicts({'type': self.ANVIL_TYPE}, meta_data)
        self._nomenclate = nomenclate.Nom(self.meta_data)
        self.parent(parent)
        self.LOG.debug('%r.__init__(top_node=%s, parent=%s, meta_data=%s)' % (self, top_node, parent, meta_data))

    @property
    def is_built(self):
        return all([self.top_node])

    def merge_dicts(self, *input_dicts):
        result = {}
        if input_dicts:
            for input_dict in input_dicts:
                if isinstance(input_dict, dict):
                    result.update(input_dict)

        return result

    def build(self):
        raise NotImplementedError

    def build_layout(self):
        raise NotImplementedError

    def parent(self, new_parent):
        top_node, new_parent = str(self.top_node), str(new_parent)
        if rt.dcc.scene.exists(new_parent, top_node) or new_parent is None or top_node is None:
            self.LOG.debug('Parenting control offset group %s to %s' % (top_node, new_parent))
            rt.dcc.scene.parent(top_node, new_parent)
        else:
            self.LOG.warning('Parent(%s) -> %r does not exist.' % (new_parent, top_node))

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
        dag_node = node_class.build(meta_data=meta_data, **flags)
        self.register_node(node_key, dag_node)
        return dag_node

    def register_node(self, node_key, dag_node, overwrite=True):
        if dag_node is None:
            self.LOG.warning('Attempted register node %s with key %s but it does not exist' % (dag_node, node_key))
            return
        if issubclass(type(dag_node), AbstractGrouping) or issubclass(type(dag_node), ot.UnicodeDelegate):
            if self.hierarchy.get(node_key) is not None and not overwrite:
                raise IndexError('Preexisting node already is stored under key %s in the hierarchy' % node_key)
            self.hierarchy[node_key] = dag_node
        else:
            raise TypeError('Could not register unrecognized node type %s is not an anvil grouping or object class.')

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
            if self.top_node is None:
                raise KeyError
            return str(self.top_node)
        except (KeyError, AttributeError):
            self.LOG.warning('Could not find top node on %r' % self)
            return super(AbstractGrouping, self).__str__()

    def __repr__(self):
        return super(AbstractGrouping, self).__repr__().replace('>', ' children=%d>' % len(list(self.hierarchy)))
