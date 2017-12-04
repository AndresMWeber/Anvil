import anvil.node_types as nt
import anvil.templates.sub_rig as sub_rig_template


class Biped(nt.Rig):
    def __init__(self,
                 left_arm=None,
                 right_arm=None,
                 left_hand=None,
                 right_hand=None,
                 left_leg=None,
                 right_leg=None,
                 left_foot=None,
                 right_foot=None,
                 spine=None,
                 neck=None,
                 head=None,
                 layout=None,
                 name_tokens=None):
        sub_rigs = [left_arm, right_arm, left_leg, right_leg, spine, neck, head]
        super(Biped, self).__init__(sub_rigs=sub_rigs, layout=layout, name_tokens=name_tokens)

    @classmethod
    def create(cls):
        center_of_mass = sub_rig_template.CenterOfMass()
        left_arm = sub_rig_template.BipedArm()
        right_arm = sub_rig_template.BipedArm()
        left_leg = sub_rig_template.BipedLeg()
        right_leg = sub_rig_template.BipedLeg()
        spine = sub_rig_template.Spine()
        neck = sub_rig_template.Neck()
        head = sub_rig_template.Head()

    def setup_sub_rig_connections(self):
        pass

    def rename(self):
        pass
