import nomenclate
import anvil


class AbstractGrouping(object):
    """ A fully functional and self-contained rig with all requirements implemented that
        require it to give a performance.

    """

    def __init__(self, layout=None, name_tokens=None):
        self.hierarchy = {}
        self._nomenclate = nomenclate.Nom(name_tokens or {})
        self.layout = layout

    def parent(self, new_parent):
        raise NotImplementedError

    def build(self):
        raise NotImplementedError

    def build_layout(self):
        raise NotImplementedError

    def rename(self, *input_dicts, **name_tokens):
        raise NotImplementedError

    def add_node(self, node_class, node_key, meta_data=None, name_tokens=None, **flags):
        flags = {} if flags is None else flags
        anvil.LOG.info('rig add %s.%s = %s(flags=%s, name_tokens=%s)' %
                       (self, node_key, node_class, flags, name_tokens))
        self.hierarchy[node_key] = node_class.build(meta_data=meta_data, name_tokens=name_tokens, **flags)
        return self.hierarchy[node_key]

    def find_node(self, node_key):
        try:
            return self.hierarchy[node_key]
        except:
            raise KeyError('Node from key %s not found in hierarchy' % node_key)

    def __getattr__(self, item):
        try:
            return super(AbstractGrouping, self).__getattribute__('hierarchy').find_member(item)
        except AttributeError:
            return super(AbstractGrouping, self).__getattribute__(item)
