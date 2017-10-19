import base
import anvil
import anvil.objects as ot
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

        for sub_node_key, sub_node in iteritems(self.hierarchy):
            anvil.LOG.info('Rig %r renaming sub_node %r...' % (self, sub_node))
            self._nomenclate.merge_dict(sub_node.meta_data)
            #sub_node.meta_data.update(name_tokens)

            # Sub node is going to be either subtype of grouping or objects.
            if issubclass(type(sub_node), base.AbstractGrouping):
                sub_node.rename(sub_node.meta_data)
            else:
                sub_node.rename(self._nomenclate.get())
            anvil.LOG.info('Renamed sub_node to %r...' % (sub_node))

    def build(self):
        self.build_layout()
        for sub_rig_key, sub_rig_member in iteritems(self.sub_rigs):
            anvil.LOG.info('Creating sub-rig %s on rig %s' % (sub_rig_member, self))
            sub_rig_member.build_layout()

    def build_layout(self):
        self.add_node(ot.Transform, 'group_root', meta_data={'childtype': 'rig'})

        for main_group_type in ['model', 'joint', 'controls', 'nodes', 'world']:
            group_name = 'group_%s' % main_group_type
            self.add_node(ot.Transform, group_name, parent=self.group_root, meta_data={'child_type': main_group_type})

        self.add_node(control.Control, 'control_universal', parent=self.find_node('group_controls'),
                      meta_data={'childtype': 'universal'})
