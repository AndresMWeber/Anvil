from six import iteritems
import base
import anvil
import anvil.objects as ot
import sub_rig
import control
import inspect


class Rig(base.AbstractGrouping):
    """ A fully functional and self-contained rig with all requirements implemented that
        require it to give a performance.  A collection of SubRig(s)

    """

    def __init__(self, sub_rigs=None, **kwargs):
        super(Rig, self).__init__(**kwargs)
        self.sub_rigs = sub_rigs or {}

    def rename(self, *input_dicts, **name_tokens):
        super(Rig, self).rename(*input_dicts, **name_tokens)
        for sub_rig_key, sub_rig in iteritems(self.sub_rigs):
            sub_rig.rename(**self.meta_data)

    def build_sub_rig(self, sub_rig_type, sub_rig_key, meta_data=None, **flags):
        sub_rig_instance = sub_rig_type.build(meta_data=None, **flags)
        self.register_sub_rig(sub_rig_instance, sub_rig_key)
        return sub_rig_instance

    def register_sub_rig(self, sub_rig, sub_rig_key, meta_data=None, **flags):
        if inspect.isclass(sub_rig) and issubclass(sub_rig, sub_rig.SubRig):
            sub_rig = self.build_sub_rig(sub_rig, sub_rig_key, meta_data=meta_data, **flags)

        if isinstance(sub_rig, sub_rig.SubRig):
            anvil.LOG.info('Registering sub-rig %s with rig %s.%s' % (sub_rig, self, sub_rig_key))
            self.sub_rigs[sub_rig_key] = sub_rig
            anvil.runtime.dcc.scene.parent(sub_rig.top_node, self.top_node)

    def build_sub_rigs(self):
        for sub_rig_key, sub_rig_member in iteritems(self.sub_rigs):
            anvil.LOG.info('Creating sub-rig %s on rig %s' % (sub_rig_member, self))

            self.register_sub_rig(sub_rig_member.build(), sub_rig_key)

    @classmethod
    def build(cls, meta_data=None, **flags):
        instance = cls(meta_data=meta_data, **flags)
        instance.build_node(ot.Transform,
                            'group_top',
                            meta_data={'childtype': 'rig', 'type': 'group'}, **flags)

        instance.build_node(control.Control,
                            'control_universal',
                            parent=instance.group_top,
                            meta_data={'childtype': 'universal'})

        for main_group_type in ['extras', 'model', 'sub_rigs']:
            group_name = 'group_%s' % main_group_type
            instance.build_node(ot.Transform,
                                group_name,
                                parent=instance.control_universal.connection_group,
                                meta_data={'childtype': main_group_type, 'type': 'group'})
            getattr(instance, group_name).inheritsTransform.set(False)
        instance.top_node = instance.group_top
        instance.build_sub_rigs()
        return instance
