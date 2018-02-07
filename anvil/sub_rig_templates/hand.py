import string
import anvil.config as cfg
from base import SubRigTemplate
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

        :param has_thumb: bool or int, if this is true will use the first digit as a thumb, if int uses that index
        :param finger_joints: [nt.HierarchyChain or str]: list joint chains to build the fingers on.
        """
        super(Hand, self).__init__(layout_joints=layout_joints, **kwargs)
        self.has_thumb = has_thumb
        self.has_ik = has_ik
        self.has_fk = has_fk
        self.digits = []

    def build(self, parent=None, use_layout=True, solver=None, meta_data=None, **kwargs):
        super(Hand, self).build(meta_data=meta_data, parent=parent, **kwargs)
        solver = solver or cfg.IK_SC_SOLVER

        for layout_joints, base_name in zip(self.layout_joints, self.get_finger_base_names()):
            self.build_digit(layout_joints, solver=solver, name_tokens={cfg.NAME: base_name}, **self.build_kwargs)

        self.rename()

    def build_digit(self, digit_joints, **kwargs):
        if self.has_fk:
            fk_results = self.build_fk_chain(digit_joints, shape='pyramid_pin', **kwargs)
        if self.has_ik:
            ik_results = self.build_ik_chain(digit_joints, shape='cube', **kwargs)
        if self.has_fk and self.has_ik:
            self.build_blend_chain(digit_joints, [ik_results[cfg.JOINT_TYPE], fk_results[cfg.JOINT_TYPE]], **kwargs)

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
