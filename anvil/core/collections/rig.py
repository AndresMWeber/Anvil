import anvil.core.objects.node_types as nt
import anvil.plugins as plugins

dcc = plugins.current_dcc

class Rig(object):
    """ A fully functional and self-contained rig with all requirements implemented that
        require it to give a performance.  A collection of SubRig(s)

    """
    NODE_TYPES = {}

    def __init__(self, layout_positions):
        self.hierarchy = self.process_layout(layout_positions)

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
        self.hierarchy[node_key] = self.DCC.node_type

    def find_node(self, node_key):
        return self.hierarchy.get(node_key, None)

    def register_node(self, node_class):
        pass

    def __getattr__(self, item):
        try:
            return super(Rig, self).__getattribute__('hierarchy').find_member(item)
        except AttributeError:
            return super(Rig, self).__getattribute__(item)
