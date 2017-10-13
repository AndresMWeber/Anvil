import nomenclate
import anvil
import anvil.core.objects.node_types as nt


class Rig(object):
    """ A fully functional and self-contained rig with all requirements implemented that
        require it to give a performance.  A collection of SubRig(s)

    """
    NODE_TYPES = {}

    def __init__(self, layout_positions, name_tokens=None):
        self.hierarchy = {}
        self._nomenclate = nomenclate.Nom(name_tokens or {})

    def build_root_hierarchy(self):
        root = self.add_node(nt.Transform, 'group_root')
        for main_group_type in ['model', 'joint', 'controls', 'nodes', 'world']:
            self.add_node(nt.Transform, 'group_%s' % main_group_type, parent=root)
        self.add_node(nt.Control, 'control_universal', parent = self.find_node('group_controls'))

    def rename(self, *input_dicts, **name_tokens):
        for input_dict in input_dicts:
            name_tokens.update(input_dict)
        self._nomenclate.merge_dict(name_tokens)

        self._nomenclate.type = 'group'
        self.find_node('group_root').rename(self._nomenclate.get(childtype='rig'))
        for main_group_type in ['model', 'joint', 'controls', 'nodes', 'world']:
            self.find_node('group_%s' % main_group_type).rename(self._nomenclate.get(childtype=main_group_type))

        self.find_node('control_universal').rename(self._nomenclate.get(childtype='universal', type='control'))

    def build_layout(self):
        for sub_rig_member in self.hierarchy:
            sub_rig_member.build_layout()

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
            return super(Rig, self).__getattribute__('hierarchy').find_member(item)
        except AttributeError:
            return super(Rig, self).__getattribute__(item)
