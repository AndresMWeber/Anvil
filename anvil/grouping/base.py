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

    def __init__(self, layout=None, meta_data=None, parent=None, top_node=None, **flags):
        self.top_node = top_node
        self.layout = layout
        self.hierarchy = {}
        self.flags = flags or {}
        self.meta_data = self.merge_dicts({'type': self.ANVIL_TYPE}, meta_data)
        self._nomenclate = nomenclate.Nom(self.meta_data)
        if parent:
            self.parent(parent)

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
        new_parent = str(new_parent)
        if rt.dcc.scene.exists(new_parent) and rt.dcc.scene.exists(self.top_node):
            anvil.LOG.info('Parenting control offset group %s to %s' % (str(self), new_parent))
            rt.dcc.scene.parent(str(self.top_node), new_parent)
        else:
            anvil.LOG.warning('Parent(%s) -> %r does not exist.' % (new_parent, self))

    def rename(self, *input_dicts, **name_tokens):
        anvil.LOG.info('Renaming %r...' % (self))
        self.meta_data.update(self.merge_dicts(input_dicts + (name_tokens,)))
        self._nomenclate.merge_dict(**self.meta_data)

        # Sub node is going to be either subtype of grouping or objects.
        for sub_node_key, sub_node in iteritems(self.hierarchy):
            if issubclass(type(sub_node), AbstractGrouping):
                sub_node.rename(self.merge_dicts(self.meta_data, sub_node.meta_data))
                anvil.LOG.info('Renamed grouping to %r...' % (sub_node))

            elif issubclass(type(sub_node), ot.UnicodeDelegate):
                sub_node.rename(self._nomenclate.get(**sub_node.meta_data))
                print(self.meta_data, sub_node.meta_data, self._nomenclate.get(**sub_node.meta_data))
                anvil.LOG.info('Renamed sub_node to %r...' % (sub_node))

    def add_node(self, node_class, node_key, meta_data=None, **flags):
        flags = {} if flags is None else flags
        anvil.LOG.info('rig add %r.%s = %s(meta_data=%s, flags=%s)' % (self, node_key, node_class, meta_data, flags))
        self.hierarchy[node_key] = node_class.build(meta_data=meta_data, **flags)
        return self.hierarchy[node_key]

    def find_node(self, node_key):
        try:
            return self.hierarchy[node_key]
        except:
            raise KeyError('Node from key %s not found in hierarchy' % node_key)

    def __getattr__(self, item):
        try:
            return super(AbstractGrouping, self).__getattribute__('hierarchy').get(item)
        except AttributeError:
            return super(AbstractGrouping, self).__getattribute__(item)

    def __str__(self):
        try:
            return str(self.find_node('top_node'))
        except:
            return super(AbstractGrouping, self).__str__()

    def __repr__(self):
        return super(AbstractGrouping, self).__repr__()
