import anvil.node_types as nt
import anvil.config as cfg
import anvil.sub_rig_templates as sub_rig_templates


class Hexapod(nt.Rig):
    SUB_RIG_BUIlD_TABLE = {
        cfg.LEFT + '_' + cfg.ARM: [sub_rig_templates.BipedArm, {cfg.NAME: cfg.ARM, cfg.SIDE: cfg.LEFT}],
        cfg.RIGHT + '_' + cfg.ARM: [sub_rig_templates.BipedArm, {cfg.NAME: cfg.ARM, cfg.SIDE: cfg.RIGHT}],
        cfg.LEFT + '_' + cfg.HAND: [sub_rig_templates.Hand, {cfg.NAME: cfg.HAND, cfg.SIDE: cfg.LEFT}],
        cfg.RIGHT + '_' + cfg.HAND: [sub_rig_templates.Hand, {cfg.NAME: cfg.HAND, cfg.SIDE: cfg.RIGHT}],
        cfg.LEFT + '_' + cfg.LEG: [sub_rig_templates.BipedLeg, {cfg.NAME: cfg.LEG, cfg.SIDE: cfg.LEFT}],
        cfg.RIGHT + '_' + cfg.LEG: [sub_rig_templates.BipedLeg, {cfg.NAME: cfg.LEG, cfg.SIDE: cfg.RIGHT}],
        cfg.LEFT + '_' + cfg.FOOT: [sub_rig_templates.BipedFoot, {cfg.NAME: cfg.FOOT, cfg.SIDE: cfg.LEFT}],
        cfg.RIGHT + '_' + cfg.FOOT: [sub_rig_templates.BipedFoot, {cfg.NAME: cfg.FOOT, cfg.SIDE: cfg.RIGHT}],
        cfg.SPINE: [sub_rig_templates.Spine, {cfg.NAME: cfg.SPINE}],
        cfg.NECK: [sub_rig_templates.Neck, {cfg.NAME: cfg.NECK}],
        cfg.HEAD: [sub_rig_templates.Head, {cfg.NAME: cfg.HEAD}],
    }
    REFLECTABLE_SUB_RIGS = [cfg.ARM, cfg.HAND, cfg.LEG, cfg.FOOT, cfg.DIGITS]
    SUB_RIG_BUILD_ORDER = [cfg.SPINE, cfg.NECK, cfg.HEAD, cfg.ARM, cfg.LEG, cfg.HAND, cfg.FOOT, cfg.DIGITS]
    ORDERED_SUB_RIG_KEYS = [[key for key in SUB_RIG_BUIlD_TABLE if sub_rig_name in key] for sub_rig_name in
                            SUB_RIG_BUILD_ORDER]

    def setup_sub_rig_connections(self):
        pass

    def rename(self, input_dicts, **name_tokens):
        super(Hexapod, self).rename(input_dicts, **name_tokens)
