from six import iteritems
import base
import anvil
import anvil.objects as ot
import sub_rig
import control
import inspect
from collections import OrderedDict


class Rig(base.AbstractGrouping):
    """ A fully functional and self-contained rig with all requirements implemented that
        require it to give a performance.  A collection of SubRig(s)
    """
    LOG = anvil.log.obtainLogger(__name__)
    SUB_RIG_BUILD_ORDER = []
    SUB_RIG_BUILD_TABLE = OrderedDict()
    ORDERED_SUB_RIG_KEYS = []

    def __init__(self, sub_rig_dict=None, **kwargs):
        super(Rig, self).__init__(**kwargs)
        self._nomenclate.format = 'side_location_nameDecoratorVar_childtype_purpose_rig_type'
        self.sub_rigs = OrderedDict.fromkeys(self.ORDERED_SUB_RIG_KEYS)
        if sub_rig_dict:
            self.register_sub_rigs_from_dict(sub_rig_dict)

    def rename(self, *input_dicts, **name_tokens):
        super(Rig, self).rename(*input_dicts, **name_tokens)
        for sub_rig_key, sub_rig in iteritems(self.sub_rigs):
            sub_rig.rename()

    def _validate_dict(self, sub_rig_dict):
        if sub_rig_dict is None or not isinstance(sub_rig_dict, dict):
            raise IOError('Must input sub-rig parts as a dictionary')

    def register_sub_rigs_from_dict(self, sub_rig_dict):
        self._validate_dict(sub_rig_dict)
        for sub_rig_name, sub_rig_construction_data in iteritems(self.SUB_RIG_BUIlD_TABLE):
            if sub_rig_dict.get(sub_rig_name):
                sub_rig_class, sub_rig_metadata = self.SUB_RIG_BUIlD_TABLE[sub_rig_name]
                sub_rig_kwargs = sub_rig_dict.get(sub_rig_name)
                sub_rig_kwargs = sub_rig_kwargs if isinstance(sub_rig_kwargs, dict) else {
                    'layout_joints': sub_rig_kwargs}
                self.register_sub_rig(sub_rig_name, sub_rig_class, meta_data=sub_rig_metadata, **sub_rig_kwargs)

    def register_sub_rig(self, sub_rig_key, sub_rig_candidate=sub_rig.SubRig, meta_data=None, **kwargs):
        if inspect.isclass(sub_rig_candidate) and issubclass(sub_rig_candidate, sub_rig.SubRig):
            self.LOG.info('Registering %s.[%s] = %s(%s)' % (self, sub_rig_key, sub_rig_candidate.__name__, kwargs))
            self.sub_rigs[sub_rig_key] = sub_rig_candidate(meta_data=meta_data, **kwargs)
            return self.sub_rigs[sub_rig_key]

    def build_sub_rigs(self):
        for sub_rig_key, sub_rig_member in iteritems(self.sub_rigs):
            if not sub_rig_member.is_built:
                self.LOG.info('Building sub-rig %s on rig %s' % (sub_rig_member, self))
                sub_rig_member.build()
            anvil.runtime.dcc.scene.parent(sub_rig_member.root, self.group_sub_rigs)

    def build(self, meta_data=None, parent=None, **kwargs):
        self.LOG.info('Building rig %s' % self)
        if not self.root:
            self.build_node(ot.Transform,
                            'group_top',
                            meta_data=self.merge_dicts(self.meta_data, {'rig': 'rig', 'type': 'group'}),
                            **kwargs)

        self.build_node(control.Control,
                        'control_universal',
                        parent=self.group_top,
                        meta_data=self.merge_dicts(self.meta_data, {'childtype': 'universal'}))

        for main_group_type in ['extras', 'model', 'sub_rigs']:
            group_name = 'group_%s' % main_group_type
            self.build_node(ot.Transform,
                            group_name,
                            parent=self.control_universal.connection_group,
                            meta_data=self.merge_dicts(self.meta_data,
                                                       {'childtype': main_group_type, 'type': 'group'}))

        self.root = self.group_top
        self.LOG.info('Building sub rigs...')
        self.build_sub_rigs()
        self.assign_rendering_delegate(self.control_universal.control)

        if parent:
            self.parent(parent)
        self.rename()

    def __getattr__(self, item):
        try:
            return super(Rig, self).__getattribute__('sub_rigs')[item]
        except KeyError:
            return super(Rig, self).__getattr__(item)
