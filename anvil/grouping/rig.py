import base
import anvil
import anvil.objects as objects
import control
from six import iteritems


class Rig(base.AbstractGrouping):
    """ A fully functional and self-contained rig with all requirements implemented that
        require it to give a performance.  A collection of SubRig(s)

    """

    def __init__(self, sub_rigs=None, layout=None, name_tokens=None):
        super(Rig, self).__init__()
        self.sub_rigs = sub_rigs or {}

    def rename(self, *input_dicts, **name_tokens):
        for input_dict in input_dicts:
            name_tokens.update(input_dict)
        self._nomenclate.merge_dict(name_tokens)

        self._nomenclate.type = 'group'
        self.find_node('group_root').rename(self._nomenclate.get(childtype='rig'))
        for main_group_type in ['model', 'joint', 'controls', 'nodes', 'world']:
            self.find_node('group_%s' % main_group_type).rename(self._nomenclate.get(childtype=main_group_type))

        self.find_node('control_universal').rename(name_tokens, childtype='universal', type='control')

    def build(self):
        self.build_layout()
        for sub_rig_key, sub_rig_member in iteritems(self.sub_rigs):
            anvil.LOG.info('Creating sub-rig %s on rig %s' % (sub_rig_member, self))
            sub_rig_member.build_layout()

    def build_layout(self):
        root = self.add_node(objects.Transform, 'group_root')
        for main_group_type in ['model', 'joint', 'controls', 'nodes', 'world']:
            self.add_node(objects.Transform, 'group_%s' % main_group_type, parent=root)
        self.add_node(control.Control, 'control_universal', parent=self.find_node('group_controls'))
