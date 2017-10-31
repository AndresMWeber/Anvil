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
        self.meta_data['rig'] = 'rig'

    def rename(self, *input_dicts, **name_tokens):
        super(Rig, self).rename(*input_dicts, **name_tokens)
        for sub_rig_key, sub_rig in iteritems(self.sub_rigs):
            sub_rig.rename(**self.meta_data)

    def register_sub_rig(self, sub_rig_candidate, sub_rig_key, meta_data=None, **flags):
        if inspect.isclass(sub_rig_candidate) and issubclass(sub_rig_candidate, sub_rig.SubRig):
            anvil.LOG.info('Registering sub-rig %s with rig %s.%s' % (sub_rig_candidate, self, sub_rig_key))
            self.sub_rigs[sub_rig_key] = sub_rig_candidate(meta_data=meta_data, **flags)
            return self.sub_rigs[sub_rig_key]

    def build_sub_rigs(self):
        for sub_rig_key, sub_rig_member in iteritems(self.sub_rigs):
            anvil.LOG.info('Creating sub-rig %s on rig %s' % (sub_rig_member, self))
            if sub_rig_member.top_node is None:
                anvil.LOG.info('Building sub-rig %s on rig %s' % (sub_rig_member, self))
                sub_rig_member.build()
            anvil.runtime.dcc.scene.parent(sub_rig_member.top_node, self.group_sub_rigs)

    def build(self, meta_data=None, **flags):
        anvil.LOG.info('Building rig %s' % self)
        self.build_node(ot.Transform,
                        'group_top',
                        meta_data={'type': 'group'}, **flags)

        self.build_node(control.Control,
                        'control_universal',
                        parent=self.group_top,
                        meta_data={'childtype': 'universal'})

        for main_group_type in ['extras', 'model', 'sub_rigs']:
            group_name = 'group_%s' % main_group_type
            self.build_node(ot.Transform,
                            group_name,
                            parent=self.control_universal.connection_group,
                            meta_data={'childtype': main_group_type, 'type': 'group'})
            getattr(self, group_name).inheritsTransform.set(False)

        self.top_node = self.group_top
        anvil.LOG.info('Building sub rigs...%s' % self)
        self.build_sub_rigs()

    def __getattr__(self, item):
        try:
            return super(Rig, self).__getattribute__('sub_rigs')[item]
        except KeyError:
            return super(Rig, self).__getattr__(item)
