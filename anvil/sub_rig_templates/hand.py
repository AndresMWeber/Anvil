import string
import anvil.config as cfg
from base_sub_rig_template import SubRigTemplate
import anvil.objects.attribute as at


class Hand(SubRigTemplate):
    BUILT_IN_NAME_TOKENS = SubRigTemplate.BUILT_IN_NAME_TOKENS.merge({"name": "hand"}, new=True)
    DEFAULT_NAMES = ["thumb", "index", "middle", "ring", "pinky"]
    BUILT_IN_ATTRIBUTES = {
        "curl_bias": at.PM_1_KWARGS,
        "curl": at.PM_10_KWARGS,
        "spread": at.PM_10_KWARGS,
        "fist": at.PM_10_KWARGS,
        "cup": at.PM_10_KWARGS,
        cfg.IKFK_BLEND: at.ZERO_TO_ONE_KWARGS,
    }

    def __init__(self, layout_joints, has_ik=True, has_fk=True, has_thumb=True, **kwargs):
        """ General class for a hand.

        :param layout_joints: anvil.node_types.Hierarchy, hierarchy chain of joints to use.
        :param has_thumb: bool or int, if this is true will use the first digit as a thumb, if int uses that index
        :param has_fk: bool or int, if this is true will build fk setup
        :param has_ik: bool or int, if this is true will build ik setup
        :param finger_joints: [nt.HierarchyChain or str]: list joint chains to build the fingers on.
        """
        super(Hand, self).__init__(layout_joints=layout_joints, **kwargs)
        self.has_thumb = has_thumb
        self.has_ik = has_ik
        self.has_fk = has_fk
        self.digits = []

    def build(self, parent=None, solver=None, meta_data=None, **kwargs):
        super(Hand, self).build(meta_data=meta_data, parent=parent, **kwargs)
        self.build_kwargs['solver'] = solver or cfg.IK_SC_SOLVER


        for index, digit_info in enumerate(zip(self.layout_joints, self.get_finger_base_names())):
            layout_joints, label = digit_info
            self.build_digit(layout_joints, index, name_tokens={cfg.NAME: label}, **self.build_kwargs)

        self.rename()

    def build_digit(self, digit_joints, index, **kwargs):
        kwargs[cfg.SKIP_REGISTER] = True
        kwargs[cfg.SKIP_REPORT] = True
        fk_chain = None
        ik_chain = None

        if self.has_fk:
            fk_chain, fk_controls = self.build_fk_chain(digit_joints,
                                                        parent=[self.group_joints, self.group_controls],
                                                        shape='pyramid_pin', **kwargs)
            self.register_node(fk_chain, hierarchy_id='%s_chain_%s' % (cfg.FK, index))
            self.register_node(fk_controls, hierarchy_id='%s_%s_%s' % (cfg.FK, cfg.CONTROL_TYPE, index))

        if self.has_ik:

            ik_chain, ik_controls, handle, effector = self.build_ik_chain(digit_joints,
                                                                          parent=[self.group_joints,
                                                                                  self.group_nodes,
                                                                                  self.group_controls,
                                                                                  self.group_controls,
                                                                                  self.group_nodes],
                                                                          shape='cube', **kwargs)
            self.register_node(ik_chain, hierarchy_id='%s_chain_%s' % (cfg.IK, index))
            self.register_node(ik_controls, hierarchy_id='%s_%s_%s' % (cfg.IK, cfg.CONTROL_TYPE, index))
            self.register_node(handle, hierarchy_id='%s_%s_%s' % (cfg.IK, cfg.IK_HANDLE, index))
            self.register_node(effector, hierarchy_id='%s_%s_%s' % (cfg.IK, cfg.IK_EFFECTOR, index))

        if self.has_fk and self.has_ik:
            blend_chain = self.build_blend_chain(digit_joints, [fk_chain, ik_chain],
                                                 parent=self.group_joints,
                                                 **kwargs)
            self.register_node(blend_chain, hierarchy_id='%s_chain_%s' % (cfg.BLEND, index))

    def get_finger_base_names(self):
        num_fingers = len(self.layout_joints)
        if (num_fingers <= 5 and self.has_thumb) or (num_fingers <= 4 and not self.has_thumb):
            return self.DEFAULT_NAMES[0 if self.has_thumb else 1:num_fingers + (1 * int(not self.has_thumb))]
        else:
            return [cfg.FINGER + c for c in string.uppercase[:num_fingers]]

    def rename(self, *input_dicts, **name_tokens):
        super(Hand, self).rename(*input_dicts, **name_tokens)

    def set_up_fist_pose(self):
        # for now just hook it up to the controls
        pass

    def set_up_spread_pose(self):
        # for now just hook it up to the controls
        pass

    def set_up_curl_pose(self):
        # for now just hook it up to the controls
        pass

    def connect_curl_fist(self, control, axis=cfg.X):
        phalanges = self.fk_chain if hasattr(self, '%s_chain' % cfg.FK) else self.blend_chain
        control.add_attr('curl', defaultValue=0, attributeType=cfg.FLOAT)
        for phalanges in phalanges[:-1]:
            pass
        print(axis)
