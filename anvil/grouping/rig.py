from collections import OrderedDict
from six import iteritems, itervalues
import inspect
import base
import anvil
import anvil.config as cfg
import anvil.objects as ot
import control as ct
from sub_rig import SubRig
from anvil.meta_data import MetaData


class Rig(base.AbstractGrouping):
    """Comprises a full finished character rig with all functionality.

    A fully functional and self-contained rig with all requirements implemented that require it to give a performance.
    A collection of SubRig(s)
    """

    LOG = anvil.log.obtain_logger(__name__)
    BUILT_IN_META_DATA = MetaData(base.AbstractGrouping.BUILT_IN_META_DATA)
    SUB_RIG_BUILD_ORDER = []
    SUB_RIG_BUILD_TABLE = OrderedDict()
    ORDERED_SUB_RIG_KEYS = []
    SUB_GROUPINGS = ['extras', 'model', 'sub_rigs']

    ROOT_META_DATA = {cfg.RIG_TYPE: cfg.RIG_TYPE, cfg.TYPE: cfg.GROUP_TYPE}
    UNIV_META_DATA = {cfg.CHILD_TYPE: cfg.UNIVERSAL}

    def __init__(self, character=None, sub_rig_dict=None, *args, **kwargs):
        self.sub_rigs = OrderedDict.fromkeys(self.ORDERED_SUB_RIG_KEYS)
        super(Rig, self).__init__(*args, **kwargs)
        self.meta_data[cfg.CHARACTER] = character or self.meta_data.get(cfg.CHARACTER, '')
        self.register_sub_rigs_from_dict(sub_rig_dict)

    def rename(self, *input_dicts, **kwargs):
        super(Rig, self).rename(*input_dicts, **kwargs)
        for sub_rig_instance in itervalues(self.sub_rigs):
            sub_rig_instance.rename()

    def register_sub_rigs_from_dict(self, sub_rig_dict):
        """Registers a SubRig to the Rig if it can be found in SUB_RIG_BUILD_TABLE

        Rig will initialize sub-rigs from the key, value and look up the proper sub-rig class from the build table.
        This is meant to rebuild a rig from a deserialized rig.

        :param sub_rig_dict: dict, key must be in SUB_RIG_BUILD_TABLE and value must be dict or list of joints.
        """
        if sub_rig_dict is None or not isinstance(sub_rig_dict, dict):
            return

        for sub_rig_name, sub_rig_data in iteritems(sub_rig_dict):
            sub_rig_construction_data = self.SUB_RIG_BUILD_TABLE.get(sub_rig_name)
            sub_rig_class, default_meta_data = sub_rig_construction_data
            sub_rig_kwargs = sub_rig_data if isinstance(sub_rig_data, dict) else {cfg.LAYOUT: sub_rig_data}
            self.build_sub_rig(sub_rig_name, sub_rig_class, meta_data=default_meta_data, **sub_rig_kwargs)

    def build_sub_rig(self, sub_rig_key, sub_rig_candidate=SubRig, **kwargs):
        """Initializes the given sub rig candidate class with kwargs and stores it in property sub_rigs under the key.

        :param sub_rig_key: str, key to store the sub rig under on the rig.
        :param sub_rig_candidate: anvil.sub_rig, a class that inherits from anvil.sub_rig.
        """
        kwargs[cfg.META_DATA] = MetaData(self.meta_data, kwargs.get(cfg.META_DATA, {}))
        if inspect.isclass(sub_rig_candidate) and issubclass(sub_rig_candidate, SubRig):
            self.sub_rigs[sub_rig_key] = sub_rig_candidate(**kwargs)
            return self.sub_rigs[sub_rig_key]
        else:
            self.warning('Sub rig candidate %s is not a valid anvil template', sub_rig_candidate)

    def build_sub_rigs(self):
        for sub_rig_member in itervalues(self.sub_rigs):
            self.info('Building sub-rig %s on rig %s', sub_rig_member, self)
            sub_rig_member.build()
            anvil.runtime.dcc.scene.parent(sub_rig_member.root, self.node.group_sub_rigs)

    def auto_color(self):
        super(Rig, self).auto_color()
        for sub_rig_instance in itervalues(self.sub_rigs):
            sub_rig_instance.auto_color()

    def build(self, parent=None, meta_data=None, **kwargs):
        self.meta_data.update(meta_data)
        self.build_node(ot.Transform, hierarchy_id='top', meta_data=self.ROOT_META_DATA, **kwargs)
        self.root = self.node.top

        self.build_node(ct.Control,
                        hierarchy_id='universal',
                        parent=self.node.top,
                        shape=cfg.DEFAULT_UNIVERSAL_SHAPE,
                        scale=5,
                        meta_data=self.UNIV_META_DATA,
                        **kwargs)

        for main_group_type in self.SUB_GROUPINGS:
            self.build_node(ot.Transform,
                            hierarchy_id='%s_%s' % (cfg.GROUP_TYPE, main_group_type),
                            parent=self.control.universal.node.connection_group,
                            meta_data={cfg.CHILD_TYPE: main_group_type, cfg.TYPE: cfg.GROUP_TYPE})

        self.build_sub_rigs()
        self.initialize_sub_rig_attributes(self.control.universal.node.control)
        self.connect_rendering_delegate(self.control.universal.node.control)
        self.parent(parent)
        self.rename()
        self.auto_color()

    def __getattr__(self, item):
        """Attempts to return a SubRig if it exists, otherwise default methodology."""
        try:
            return super(Rig, self).__getattribute__('sub_rigs')[item]
        except KeyError:
            return super(Rig, self).__getattr__(item)
