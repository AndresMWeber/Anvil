import anvil
import anvil.core.objects.node_types as nt


class Rig(object):
    """ A fully functional and self-contained rig with all requirements implemented that
        require it to give a performance.  A collection of SubRig(s)

    """
    NODE_TYPES = {}

    def __init__(self, layout_positions):
        self.hierarchy = {}

    def build_root_hierarchy(self):
        self.add_node(nt.Transform, 'group_root')
        self.add_node(nt.Transform, 'group_model', flags={'parent': self.find_node('group_root')})
        self.add_node(nt.Transform, 'group_joint', flags={'parent': self.find_node('group_root')})
        self.add_node(nt.Transform, 'group_controls', flags={'parent': self.find_node('group_root')})
        self.add_node(nt.Transform, 'group_nodes', flags={'parent': self.find_node('group_root')})
        self.add_node(nt.Transform, 'group_world', flags={'parent': self.find_node('group_root')})
        self.add_node(nt.Transform, 'control_universal', flags={'parent': self.find_node('group_controls')})

    def build_layout(self):
        for sub_rig_member in self.hierarchy:
            sub_rig_member.build_layout()

    def add_node(self, node_class, node_key, flags=None, name_tokens=None):
        flags = {} if flags is None else flags
        anvil.LOG.info('rig add %s.%s = %s(flags=%s, name_tokens=%s)' % (self, node_key, node_class, flags, name_tokens))
        node = node_class.build(name_tokens=name_tokens, **flags)
        self.hierarchy[node_key] = node
        return node

    def find_node(self, node_key):
        return self.hierarchy.get(node_key, None)

    def __getattr__(self, item):
        try:
            return super(Rig, self).__getattribute__('hierarchy').find_member(item)
        except AttributeError:
            return super(Rig, self).__getattribute__(item)
