from six import iteritems
import base
import anvil
from anvil.meta_data import MetaData, cls_merge_name_tokens_and_meta_data
import anvil.config as cfg
import anvil.objects as ot
import sub_rig
import control as ct
import inspect
from collections import OrderedDict


class Rig(base.AbstractGrouping):
    """ A fully functional and self-contained rig with all requirements implemented that
        require it to give a performance.  A collection of SubRig(s)
    """
    LOG = anvil.log.obtainLogger(__name__)
    BUILT_IN_NAME_TOKENS = MetaData(base.AbstractGrouping.BUILT_IN_NAME_TOKENS)
    SUB_RIG_BUILD_ORDER = []
    SUB_RIG_BUILD_TABLE = OrderedDict()
    ORDERED_SUB_RIG_KEYS = []
    SUB_GROUPINGS = ['extras', 'model', 'sub_rigs']

    ROOT_NAME_TOKENS = {cfg.RIG_TYPE: cfg.RIG_TYPE, cfg.TYPE: cfg.GROUP_TYPE}
    UNIV_NAME_TOKENS = {cfg.CHILD_TYPE: cfg.UNIVERSAL}

    def __init__(self, character=None, sub_rig_dict=None, *args, **kwargs):
        self.sub_rigs = OrderedDict.fromkeys(self.ORDERED_SUB_RIG_KEYS)
        super(Rig, self).__init__(*args, **kwargs)
        self.name_tokens[cfg.CHARACTER] = character or self.name_tokens.get(cfg.CHARACTER, '')
        self.register_sub_rigs_from_dict(sub_rig_dict)

    def rename(self, *input_dicts, **name_tokens):
        super(Rig, self).rename(*input_dicts, **name_tokens)
        for sub_rig_key, sub_rig in iteritems(self.sub_rigs):
            sub_rig.rename() #*input_dicts, **name_tokens)

    def register_sub_rigs_from_dict(self, sub_rig_dict):
        """ Only accepts dictionary with keys that match the built in SUB_RIG_BUILD_TABLE for the given Rig.
            Rig will initialize sub-rigs from the key, value and look up the proper sub-rig class from the build table.
            This is meant to rebuild a rig from a deserialized rig.

        :param sub_rig_dict: dict, key must be in SUB_RIG_BUILD_TABLE and value must be dict or list of joints.
        """
        if sub_rig_dict is None or not isinstance(sub_rig_dict, dict):
            self.info('Empty or invalid sub rig dict %s...pass.', sub_rig_dict)
            return

        for sub_rig_name, sub_rig_data in iteritems(sub_rig_dict):
            try:
                self.info('Registering sub rig %s: %s.', sub_rig_name, sub_rig_data)
                sub_rig_construction_data = self.SUB_RIG_BUILD_TABLE.get(sub_rig_name)
                sub_rig_class, default_name_tokens = sub_rig_construction_data
                sub_rig_kwargs = sub_rig_data if isinstance(sub_rig_data, dict) else {cfg.LAYOUT: sub_rig_data}
                self.build_sub_rig(sub_rig_name, sub_rig_class, name_tokens=default_name_tokens, **sub_rig_kwargs)
            except TypeError:
                self.warning('Sub rig table entry %r not found in input dict %s', sub_rig_name, sub_rig_dict)

    def build_sub_rig(self, sub_rig_key, sub_rig_candidate=sub_rig.SubRig, **kwargs):
        """ Initializes the given sub rig candidate class with kwargs and stores it in property sub_rigs under the key.

        :param sub_rig_key: str, key to store the sub rig under on the rig.
        :param sub_rig_candidate: anvil.sub_rig, a class that inherits from anvil.sub_rig.
        """
        kwargs[cfg.NAME_TOKENS] = MetaData(self.name_tokens, kwargs.get(cfg.NAME_TOKENS, {}))
        kwargs[cfg.META_DATA] = MetaData(self.meta_data, kwargs.get(cfg.META_DATA, {}))
        if inspect.isclass(sub_rig_candidate) and issubclass(sub_rig_candidate, sub_rig.SubRig):
            self.info('Registering %s.[%s] = %s(%s)', self, sub_rig_key, sub_rig_candidate.__name__, kwargs)
            layout_joints = kwargs.pop('layout_joints')
            self.sub_rigs[sub_rig_key] = sub_rig_candidate(layout_joints, **kwargs)
            return self.sub_rigs[sub_rig_key]

    def build_sub_rigs(self):
        for sub_rig_key, sub_rig_member in iteritems(self.sub_rigs):
            self.info('Building sub-rig %s on rig %s', sub_rig_member, self)
            sub_rig_member.build(parent=self.group_sub_rigs)

    def auto_color(self):
        super(Rig, self).auto_color()
        for key, sub_rig in iteritems(self.sub_rigs):
            sub_rig.auto_color()

    def build(self, parent=None, name_tokens=None, **kwargs):
        self.info('Building %s(%r) with parent: %s, name_tokens: %s, and kwargs: %s',
                  self.__class__.__name__, self, parent, name_tokens, kwargs)
        self.name_tokens.update(name_tokens)

        self.build_node(ot.Transform,
                        cfg.TOP_GROUP,
                        name_tokens=self.ROOT_NAME_TOKENS,
                        **kwargs)

        self.build_node(ct.Control,
                        cfg.UNIVERSAL_CONTROL,
                        parent=self.group_top,
                        shape=cfg.DEFAULT_UNIVERSAL_SHAPE,
                        scale=5,
                        name_tokens=self.UNIV_NAME_TOKENS,
                        **kwargs)

        for main_group_type in self.SUB_GROUPINGS:
            group_name = '%s_%s' % (cfg.GROUP_TYPE, main_group_type)
            self.build_node(ot.Transform, group_name, parent=getattr(self.control_universal, cfg.CONNECTION_GROUP),
                            name_tokens={cfg.CHILD_TYPE: main_group_type, cfg.TYPE: cfg.GROUP_TYPE})

        self.root = self.group_top

        self.info('Building sub rigs on rig %r(%d): %s', self, len(list(self.sub_rigs)), list(self.sub_rigs))
        self.build_sub_rigs()
        self.initialize_sub_rig_attributes(self.control_universal.control)
        self.connect_rendering_delegate(self.control_universal.control)

        self.parent(parent)
        self.rename()
        self.auto_color()

    def __getattr__(self, item):
        try:
            return super(Rig, self).__getattribute__('sub_rigs')[item]
        except KeyError:
            return super(Rig, self).__getattr__(item)
