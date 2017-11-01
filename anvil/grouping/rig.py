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
    LOG = anvil.log.obtainLogger(__name__)

    def __init__(self, sub_rigs=None, **kwargs):
        super(Rig, self).__init__(**kwargs)
        self._nomenclate.format = 'side_location_nameDecoratorVar_childtype_purpose_rig_type'
        self.sub_rigs = sub_rigs or {}

    def rename(self, *input_dicts, **name_tokens):
        super(Rig, self).rename(*input_dicts, **name_tokens)
        for sub_rig_key, sub_rig in iteritems(self.sub_rigs):
            sub_rig.rename()  # **self.meta_data)

    def register_sub_rig(self, sub_rig_key, sub_rig_candidate=sub_rig.SubRig, meta_data=None, **flags):
        if inspect.isclass(sub_rig_candidate) and issubclass(sub_rig_candidate, sub_rig.SubRig):
            self.LOG.info('Registering sub-rig %s with rig %s.%s' % (sub_rig_candidate, self, sub_rig_key))
            self.sub_rigs[sub_rig_key] = sub_rig_candidate(meta_data=meta_data, **flags)
            return self.sub_rigs[sub_rig_key]

    def build_sub_rigs(self):
        for sub_rig_key, sub_rig_member in iteritems(self.sub_rigs):
            if not sub_rig_member.is_built:
                self.LOG.info('Building sub-rig %s on rig %s' % (sub_rig_member, self))
                sub_rig_member.build()
            anvil.runtime.dcc.scene.parent(sub_rig_member.top_node, self.group_sub_rigs)

    def build(self, meta_data=None, **flags):
        self.LOG.info('Building rig %s' % self)
        self.build_node(ot.Transform,
                        'group_top',
                        meta_data=self.merge_dicts(self.meta_data, {'rig': 'rig', 'type': 'group'}),
                        **flags)

        self.build_node(control.Control,
                        'control_universal',
                        parent=self.group_top,
                        meta_data=self.merge_dicts(self.meta_data, {'childtype': 'universal'}))

        for main_group_type in ['extras', 'model', 'sub_rigs']:
            group_name = 'group_%s' % main_group_type
            node = self.build_node(ot.Transform,
                                   group_name,
                                   parent=self.control_universal.connection_group,
                                   meta_data=self.merge_dicts(self.meta_data,
                                                              {'childtype': main_group_type, 'type': 'group'}))
            node.inheritsTransform.set(False)

        self.top_node = self.group_top
        self.LOG.info('Building sub rigs...')
        self.build_sub_rigs()

    def __getattr__(self, item):
        try:
            return super(Rig, self).__getattribute__('sub_rigs')[item]
        except KeyError:
            return super(Rig, self).__getattr__(item)
