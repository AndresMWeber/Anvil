import string
import anvil.config as cfg
from base import SubRigTemplate
import digits
import anvil.objects.attribute as at

class Hand(SubRigTemplate):
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
        num_fingers = len(self.layout_joints)
        self.LOG.info('Building %s: %r with %d digits' % (self.__class__.__name__, self, num_fingers))

        base_names = self.DEFAULT_NAMES if num_fingers == 5 else [cfg.FINGER + letter for letter in
                                                                  string.uppercase[:num_fingers]]
        for layout_joints, base_name in zip(self.layout_joints, base_names):
            self.LOG.info('Building digit %s from joints %r' % (base_name, layout_joints))
            digit_instance = digits.Digit(layout_joints, meta_data=self.meta_data + {cfg.NAME: base_name})
            digit_instance.build(parent=self.root, solver=cfg.IK_SC_SOLVER, **self.build_kwargs)
            self.digits.append(digit_instance)

        self.rename()

    def rename(self, *input_dicts, **name_tokens):
        super(Hand, self).rename(*input_dicts, **name_tokens)

        for digit in self.digits:
            digit.meta_data.merge(self.meta_data, ignore_keys=cfg.NAME)
            digit.rename()

    def set_up_fist_pose(self):
        pass

    def set_up_spread_pose(self):
        pass

    def set_up_curl_pose(self):
        pass
