import anvil
import anvil.core.objects.node_types as nt


class Rig(object):
    """ A fully functional and self-contained rig with all requirements implemented that
        require it to give a performance.  A collection of SubRig(s)

    """
    NODE_TYPES = {}

    def __init__(self, layout_positions, name_tokens=None):
        self.hierarchy = {}
        self.name_tokens = name_tokens or {}

    def build_root_hierarchy(self):
        self.name_tokens['type'] = 'transform'
        self.add_node(nt.Transform, 'group_root', name_tokens=self.name_tokens)
        self.add_node(nt.Transform, 'group_model', flags={'parent': self.find_node('group_root')},
                      name_tokens=self.merge_naming_kwargs(childtype='model', type='group'))
        self.add_node(nt.Transform, 'group_joint', flags={'parent': self.find_node('group_root')},
                      name_tokens=self.merge_naming_kwargs(childtype='joint'))
        self.add_node(nt.Transform, 'group_controls', flags={'parent': self.find_node('group_root')},
                      name_tokens=self.merge_naming_kwargs(childtype='controls'))
        self.add_node(nt.Transform, 'group_nodes', flags={'parent': self.find_node('group_root')},
                      name_tokens=self.merge_naming_kwargs(childtype='nodes'))
        self.add_node(nt.Transform, 'group_world', flags={'parent': self.find_node('group_root')},
                      name_tokens=self.merge_naming_kwargs(childtype='world'))
        self.add_node(nt.Control, 'control_universal', flags={'parent': self.find_node('group_controls')},
                      name_tokens=self.merge_naming_kwargs(childtype='universal'))

    def rename(self, **name_tokens):

    def merge_naming_kwargs(self, **naming_kwargs):
        self.name_tokens.update(naming_kwargs)
        return self.name_tokens

    def build_layout(self):
        for sub_rig_member in self.hierarchy:
            sub_rig_member.build_layout()

    def add_node(self, node_class, node_key, meta_data=None, name_tokens=None, **flags):
        flags = {} if flags is None else flags
        anvil.LOG.info('rig add %s.%s = %s(flags=%s, name_tokens=%s)' %
                       (self, node_key, node_class, flags, name_tokens))
        node = lambda: node_class.build(meta_data=meta_data, name_tokens=name_tokens, **flags)
        self.hierarchy[node_key] = node
        return node

    def find_node(self, node_key):
        try:
            return self.hierarchy[node_key]
        except:
            raise KeyError('Node from key %s not found in hierarchy' % node_key)

    def __getattr__(self, item):
        try:
            return super(Rig, self).__getattribute__('hierarchy').find_member(item)
        except AttributeError:
            return super(Rig, self).__getattribute__(item)
