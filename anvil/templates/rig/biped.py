from six import iteritems
import anvil.node_types as nt
import anvil.config as cfg
import anvil.templates.sub_rig as sub_rig_template
import anvil.runtime as rt


class Biped(nt.Rig):
    SUB_RIG_BUIlD_TABLE = {
        cfg.LEFT + '_' + cfg.ARM: [sub_rig_template.BipedArm, {cfg.NAME: cfg.ARM, cfg.SIDE: cfg.LEFT}],
        cfg.RIGHT + '_' + cfg.ARM: [sub_rig_template.BipedArm, {cfg.NAME: cfg.ARM, cfg.SIDE: cfg.RIGHT}],
        cfg.LEFT + '_' + cfg.HAND: [sub_rig_template.Hand, {cfg.NAME: cfg.HAND, cfg.SIDE: cfg.LEFT}],
        cfg.RIGHT + '_' + cfg.HAND: [sub_rig_template.Hand, {cfg.NAME: cfg.HAND, cfg.SIDE: cfg.RIGHT}],
        cfg.LEFT + '_' + cfg.LEG: [sub_rig_template.BipedLeg, {cfg.NAME: cfg.LEG, cfg.SIDE: cfg.LEFT}],
        cfg.RIGHT + '_' + cfg.LEG: [sub_rig_template.BipedLeg, {cfg.NAME: cfg.LEG, cfg.SIDE: cfg.RIGHT}],
        cfg.LEFT + '_' + cfg.FOOT: [sub_rig_template.BipedFoot, {cfg.NAME: cfg.FOOT, cfg.SIDE: cfg.LEFT}],
        cfg.RIGHT + '_' + cfg.FOOT: [sub_rig_template.BipedFoot, {cfg.NAME: cfg.FOOT, cfg.SIDE: cfg.RIGHT}],
        cfg.SPINE: [sub_rig_template.Spine, {cfg.NAME: cfg.SPINE}],
        cfg.NECK: [sub_rig_template.Neck, {cfg.NAME: cfg.NECK}],
        cfg.HEAD: [sub_rig_template.Head, {cfg.NAME: cfg.HEAD}],
    }

    REFLECTABLE_SUB_RIGS = [cfg.ARM, cfg.HAND, cfg.LEG, cfg.FOOT, cfg.DIGITS]
    SUB_RIG_BUILD_ORDER = [cfg.SPINE, cfg.NECK, cfg.HEAD, cfg.ARM, cfg.LEG, cfg.HAND, cfg.FOOT, cfg.DIGITS]
    ORDERED_SUB_RIGS = [any(key.startswith(sub_rig_name) for key in SUB_RIG_BUIlD_TABLE) for sub_rig_name in
                        SUB_RIG_BUILD_ORDER]

    def __init__(self, sub_rig_dict, name_tokens=None):
        if sub_rig_dict is None or not isinstance(sub_rig_dict, dict):
            raise IOError('Must input sub-rig parts as a dictionary')

        for sub_rig_name, sub_rig_construction_data in iteritems(self.SUB_RIG_BUIlD_TABLE):
            if sub_rig_dict.get(sub_rig_name):
                sub_rig_class, sub_rig_metadata = self.SUB_RIG_BUIlD_TABLE[sub_rig_name]
                sub_rig_kwargs = sub_rig_dict.get(sub_rig_name)
                self.register_sub_rig(sub_rig_name, sub_rig_class, meta_data=sub_rig_metadata, **sub_rig_kwargs)

        super(Biped, self).__init__(sub_rigs=self.sub_rigs, name_tokens=name_tokens)

    def build(self, meta_data=None, **kwargs):
        super(Biped, self).build(meta_data=meta_data, **kwargs)

    def build_sub_rigs(self):

        for sub_rig_name in ordered_sub_rigs:
            sub_rig_member = self.sub_rigs[sub_rig_name]
            if not sub_rig_member.is_built:
                self.LOG.info('Building sub-rig %s on rig %s' % (sub_rig_member, self))
                sub_rig_member.build()
                rt.dcc.scene.parent(sub_rig_member.root, self.group_sub_rigs)

    def setup_sub_rig_connections(self):
        pass

    def rename(self):
        pass
