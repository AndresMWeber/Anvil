import string
import anvil
import anvil.config as cfg
from base import SubRigTemplate
import digits
import anvil.objects.attribute as at


class Hand(digits.Digit):
    BUILT_IN_NAME_TOKENS = SubRigTemplate.BUILT_IN_NAME_TOKENS.merge({"name": "hand"}, new=True)
    DEFAULT_NAMES = ["thumb", "index", "middle", "ring", "pinky"]
    BUILT_IN_ATTRIBUTES = {
        "curl_bias": at.PM_1_KWARGS,
        "curl": at.PM_10_KWARGS,
        "spread": at.PM_10_KWARGS,
        "fist": at.PM_10_KWARGS,
        "cup": at.PM_10_KWARGS,
    }

    def __init__(self, has_thumb=False, finger_joints=None, **kwargs):
        """ General class for a hand.

        :param has_thumb: bool or int, if this is true will use the first digit as a thumb, if int uses that index
        :param finger_joints: [nt.HierarchyChain or str]: list joint chains to build the fingers on.
        """
        super(Hand, self).__init__(**kwargs)
        self.layout_joints = finger_joints or []
        self.has_thumb = has_thumb
        self.digits = []

    def build(self, parent=None, use_layout=True, build_ik=True, build_fk=True, meta_data=None, **kwargs):
        super(Hand, self).build(meta_data=meta_data, parent=parent, **kwargs)
        anvil.LOG.info('Building %s: %r with %d digits' % (self.__class__.__name__, self, len(self.layout_joints)))

        for layout_joints, base_name in zip(self.layout_joints,  self.get_finger_base_names()):
            self.build_digit(layout_joints, solver=cfg.IK_SC_SOLVER, **self.build_kwargs)

        self.rename()

    def build_digit(self,digit_joints, build_ik=True, build_fk=True, parent=None, **kwargs):
        if build_fk:
            self.build_kwargs['shape'] = 'pyramid_pin'
            self.build_fk_chain(digit_joints, **self.build_kwargs)

        if build_ik:
            self.build_kwargs['shape'] = 'cube'
            self.build_ik_chain(digit_joints, **self.build_kwargs)

        self.build_blend_chain(digit_joints, **self.build_kwargs)

    def get_finger_base_names(self):
        num_fingers = len(self.layout_joints)
        if num_fingers == 5:
            names = self.DEFAULT_NAMES
        else:
            names = [cfg.FINGER + letter for letter in string.uppercase[:num_fingers]]
        return names

    def rename(self, *input_dicts, **name_tokens):
        super(Hand, self).rename(*input_dicts, **name_tokens)

        for digit in self.digits:
            digit.rename()

    def set_up_fist_pose(self):
        # for now just hook it up to the controls
        pass

    def set_up_spread_pose(self):
        # for now just hook it up to the controls
        pass

    def set_up_curl_pose(self):
        # for now just hook it up to the controls
        pass
