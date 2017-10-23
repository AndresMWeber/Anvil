from six import iteritems
import base
import anvil
import anvil.objects as ot
import control


class Rig(base.AbstractGrouping):
    """ A fully functional and self-contained rig with all requirements implemented that
        require it to give a performance.  A collection of SubRig(s)

    """

    def __init__(self, sub_rigs=None, **kwargs):
        super(Rig, self).__init__(**kwargs)
        self.sub_rigs = sub_rigs or {}

    def build_subgroups(self):
        for sub_rig_key, sub_rig_member in iteritems(self.sub_rigs):
            anvil.LOG.info('Creating sub-rig %s on rig %s' % (sub_rig_member, self))
            sub_rig_member.build_layout()

    @classmethod
    def build(cls, meta_data=None, **flags):
        instance = cls(meta_data=meta_data, **flags)
        instance.top_node = instance.build_node(ot.Transform, 'group_top',
                                                meta_data={'childtype': 'rig', 'type': 'group'}, **flags)

        for main_group_type in ['model', 'joints', 'controls', 'nodes', 'world']:
            group_name = 'group_%s' % main_group_type
            instance.build_node(ot.Transform, group_name, parent=instance.top_node,
                                meta_data={'childtype': main_group_type, 'type': 'group'})

        instance.build_node(control.Control, 'control_universal', parent=instance.group_controls,
                            meta_data={'childtype': 'universal'})

        return instance
