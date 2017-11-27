import anvil
import anvil.runtime as rt
import anvil.node_types as nt
import anvil.templates.sub_rig.spine as spine
import anvil.templates.sub_rig.biped_arm as biped_arm
from base_test import TestBase
from pprint import pprint


class TestBaseTemplates(TestBase):
    name_tokens = {'name': 'eye', 'purpose': 'mvp'}
    test_rig = None
    TEMPLATE_CLASS = None

    @classmethod
    def runner(cls, num_joints=6, template_flags=None, joint_flags=None):
        try:
            template_flags = {} if template_flags is None else template_flags
            joint_flags = {} if joint_flags is None else joint_flags

            joints = []
            for i in range(num_joints):
                joint = nt.Joint.build(**joint_flags)
                rt.dcc.scene.position(joint, translation=[0, i, 0])
                joints.append(joint)

            sub_rig_instance = cls.TEMPLATE_CLASS(joints)
            sub_rig_instance.build(**template_flags)
            pprint(anvil.runtime.dcc.scene.get_scene_tree())
            return sub_rig_instance
        except:
            pprint(anvil.runtime.dcc.scene.get_scene_tree())

class TestSpineBuild(TestBaseTemplates):
    TEMPLATE_CLASS = spine.Spine

    @TestBase.delete_created_nodes
    def test_build(self):
        self.runner()

    @TestBase.delete_created_nodes
    def test_build_with_parent(self):
        parent = nt.Transform.build(name='test')
        sub_rig_instance = self.runner(template_flags={'parent': parent})
        self.assertEqual(str(sub_rig_instance.group_top.get_parent()), str(parent))


class TestBipedArmBuild(TestBaseTemplates):
    TEMPLATE_CLASS = biped_arm.BipedArm

    @TestBase.delete_created_nodes
    def test_build(self):
        self.runner()

    @TestBase.delete_created_nodes
    def test_build_with_parent(self):
        parent = nt.Transform.build(name='test')
        sub_rig_instance = self.runner(template_flags={'parent': parent})
        self.assertEqual(str(sub_rig_instance.group_top.get_parent()), str(parent))