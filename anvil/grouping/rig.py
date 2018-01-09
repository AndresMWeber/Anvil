from six import iteritems
import base
import anvil
from anvil.meta_data import MetaData, cls_merge_name_tokens_and_meta_data
import anvil.config as cfg
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
    BUILT_IN_NAME = MetaData({cfg.RIG: cfg.RIG}, base.AbstractGrouping.BUILT_IN_NAME)
    SUB_RIG_BUILD_ORDER = []
    SUB_RIG_BUILD_TABLE = OrderedDict()
    ORDERED_SUB_RIG_KEYS = []
    SUB_GROUPINGS = ['extras', 'model', 'sub_rigs']

    def __init__(self, character_name=None, sub_rig_dict=None, **kwargs):
        super(Rig, self).__init__(**kwargs)
        self.name_tokens[cfg.CHARACTER] = character_name or 'robert'
        self.sub_rigs = OrderedDict.fromkeys(self.ORDERED_SUB_RIG_KEYS)
        self.register_sub_rigs_from_dict(sub_rig_dict)

    def rename(self, *input_dicts, **name_tokens):
        super(Rig, self).rename(*input_dicts, **name_tokens)
        for sub_rig_key, sub_rig in iteritems(self.sub_rigs):
            sub_rig.rename()

    def register_sub_rigs_from_dict(self, sub_rig_dict):
        """ Only accepts dictionary with keys that match the built in SUB_RIG_BUILD_TABLE for the given Rig.
            Rig will initialize sub-rigs from the key, value and look up the proper sub-rig class from the build table.
            This is meant to rebuild a rig from a deserialized rig.

        :param sub_rig_dict: dict, key must be in SUB_RIG_BUILD_TABLE and value must be dict or list of joints.
        """
        if sub_rig_dict is None or not isinstance(sub_rig_dict, dict):
            self.LOG.info('Empty sub rig dict...pass.')
            return

        for sub_rig_name, sub_rig_construction_data in iteritems(self.SUB_RIG_BUILD_TABLE):
            if sub_rig_dict.get(sub_rig_name):
                sub_rig_class, default_name_tokens = sub_rig_construction_data
                sub_rig_kwargs = sub_rig_dict.get(sub_rig_name)
                sub_rig_kwargs = sub_rig_kwargs if isinstance(sub_rig_kwargs, dict) else {cfg.LAYOUT: sub_rig_kwargs}
                self.register_sub_rig(sub_rig_name, sub_rig_class, name_tokens=default_name_tokens, **sub_rig_kwargs)

    def register_sub_rig(self, sub_rig_key, sub_rig_candidate=sub_rig.SubRig, **kwargs):
        """ Initializes the given sub rig candidate class with kwargs and stores it in property sub_rigs under the key.

        :param sub_rig_key: str, key to store the sub rig under on the rig.
        :param sub_rig_candidate: anvil.sub_rig, a class that inherits from anvil.sub_rig.
        """
        kwargs[cfg.NAME_TOKENS] = MetaData(self.name_tokens, kwargs.get(cfg.NAME_TOKENS, {}))
        kwargs[cfg.META_DATA] = MetaData(self.meta_data, kwargs.get(cfg.META_DATA, {}))
        if inspect.isclass(sub_rig_candidate) and issubclass(sub_rig_candidate, sub_rig.SubRig):
            self.LOG.info('Registering %s.[%s] = %s(%s)' % (self, sub_rig_key, sub_rig_candidate.__name__, kwargs))
            self.sub_rigs[sub_rig_key] = sub_rig_candidate(**kwargs)
            return self.sub_rigs[sub_rig_key]

    def build_sub_rigs(self):
        for sub_rig_key, sub_rig_member in iteritems(self.sub_rigs):
            if not sub_rig_member.is_built:
                anvil.LOG.info('Building sub-rig %s on rig %s' % (sub_rig_member, self))
                sub_rig_member.build()
            anvil.runtime.dcc.scene.parent(sub_rig_member.root, self.group_sub_rigs)

    def auto_color(self):
        super(Rig, self).auto_color()
        for key, sub_rig in iteritems(self.sub_rigs):
            sub_rig.auto_color()

    @cls_merge_name_tokens_and_meta_data()
    def build(self, parent=None, **kwargs):
        anvil.LOG.info('Building rig %r' % self)
        if not self.root:
            self.build_node(ot.Transform,
                            'group_top',
                            name_tokens={cfg.RIG: cfg.RIG, cfg.TYPE: cfg.GROUP_TYPE},
                            **kwargs)

        self.build_node(control.Control,
                        '%s_universal' % cfg.CONTROL_TYPE,
                        parent=self.group_top,
                        shape=cfg.DEFAULT_UNIVERSAL_SHAPE,
                        scale=5,
                        name_tokens={cfg.CHILD_TYPE: 'universal'})

        for main_group_type in self.SUB_GROUPINGS:
            group_name = '%s_%s' % (cfg.GROUP_TYPE, main_group_type)
            self.build_node(ot.Transform,
                            group_name,
                            parent=self.control_universal.connection_group,
                            name_tokens={cfg.CHILD_TYPE: main_group_type, cfg.TYPE: cfg.GROUP_TYPE})

        self.root = self.group_top
        anvil.LOG.info('Building sub rigs on rig %r(%d): %s' % (self, len(list(self.sub_rigs)), list(self.sub_rigs)))
        self.build_sub_rigs()
        self.initialize_sub_rig_attributes(self.control_universal.control)
        self.connect_rendering_delegate(self.control_universal.control)

        if parent:
            self.parent(parent)
        self.rename()
        self.auto_color()

    def __getattr__(self, item):
        try:
            return super(Rig, self).__getattribute__('sub_rigs')[item]
        except KeyError:
            return super(Rig, self).__getattr__(item)
