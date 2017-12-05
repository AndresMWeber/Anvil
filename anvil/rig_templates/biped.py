import anvil.node_types as nt
import anvil.config as cfg
import anvil.sub_rig_templates as sub_rig_templates
from collections import OrderedDict


class Biped(nt.Rig):
    SUB_RIG_BUIlD_TABLE = OrderedDict(
        [(cfg.SPINE, [sub_rig_templates.Spine, {cfg.NAME: cfg.SPINE}]),
         (cfg.NECK, [sub_rig_templates.Neck, {cfg.NAME: cfg.NECK}]),
         (cfg.HEAD, [sub_rig_templates.Head, {cfg.NAME: cfg.HEAD}]),
         (cfg.LEFT + '_' + cfg.ARM, [sub_rig_templates.BipedArm, {cfg.NAME: cfg.ARM, cfg.SIDE: cfg.LEFT}]),
         (cfg.RIGHT + '_' + cfg.ARM, [sub_rig_templates.BipedArm, {cfg.NAME: cfg.ARM, cfg.SIDE: cfg.RIGHT}]),
         (cfg.LEFT + '_' + cfg.LEG, [sub_rig_templates.BipedLeg, {cfg.NAME: cfg.LEG, cfg.SIDE: cfg.LEFT}]),
         (cfg.RIGHT + '_' + cfg.LEG, [sub_rig_templates.BipedLeg, {cfg.NAME: cfg.LEG, cfg.SIDE: cfg.RIGHT}]),
         (cfg.LEFT + '_' + cfg.HAND, [sub_rig_templates.Hand, {cfg.NAME: cfg.HAND, cfg.SIDE: cfg.LEFT}]),
         (cfg.RIGHT + '_' + cfg.HAND, [sub_rig_templates.Hand, {cfg.NAME: cfg.HAND, cfg.SIDE: cfg.RIGHT}]),
         (cfg.LEFT + '_' + cfg.FOOT, [sub_rig_templates.BipedFoot, {cfg.NAME: cfg.FOOT, cfg.SIDE: cfg.LEFT}]),
         (cfg.RIGHT + '_' + cfg.FOOT, [sub_rig_templates.BipedFoot, {cfg.NAME: cfg.FOOT, cfg.SIDE: cfg.RIGHT}]),
         ]
    )

    def __init__(self, sub_rig_dict=None, meta_data=None, **kwargs):
        super(Biped, self).__init__(sub_rig_dict=sub_rig_dict, meta_data=meta_data, **kwargs)

    def build(self, meta_data=None, **kwargs):
        super(Biped, self).build(meta_data=meta_data, **kwargs)

    def setup_sub_rig_connections(self):
        pass

    def rename(self, input_dicts, **name_tokens):
        super(Biped, self).rename(input_dicts, **name_tokens)
