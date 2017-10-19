import nomenclate
import anvil


class AbstractGrouping(object):
    """ A fully functional and self-contained rig with all requirements implemented that
        require it to give a performance.

    """
    ANVIL_TYPE = 'group'

    def __init__(self, layout=None, name_tokens=None, meta_data=None, **flags):
        self.layout = layout
        self.hierarchy = {}
        self.flags = flags or {}
        self._nomenclate = nomenclate.Nom(name_tokens or {})

        default_meta_data = {'type': self.ANVIL_TYPE}
        default_meta_data.update(meta_data or {})
        self.meta_data = default_meta_data

    def parent(self, new_parent):
        raise NotImplementedError

    def build(self):
        raise NotImplementedError

    def build_layout(self):
        raise NotImplementedError

    def rename(self, *input_dicts, **name_tokens):
        raise NotImplementedError

    def add_node(self, node_class, node_key, meta_data=None, **flags):
        flags = {} if flags is None else flags
        anvil.LOG.info('rig add %s.%s = %s(meta_data=%s, flags=%s)' % (self, node_key, node_class, meta_data, flags))
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
            return str(self.find_node('group_root'))
        except:
            return super(AbstractGrouping, self).__str__()

    def __repr__(self):
        return super(AbstractGrouping, self).__repr__()