import anvil.runtime as rt
import anvil.node_types as nt
from tests.base_test import TestBase, sanitize
from anvil.sub_rig_templates.base_sub_rig_template import SubRigTemplate
from anvil.sub_rig_templates.spine import Spine
from anvil.sub_rig_templates.biped_arm import BipedArm


class TestBaseTemplates(TestBase):
    meta_data = {'name': 'eye', 'purpose': 'mvp'}
    test_rig = None
    TEMPLATE_CLASS = SubRigTemplate

    @classmethod
    def runner(cls, num_joints=6, template_args=None, template_flags=None, joint_flags=None):
        addtl_template_flags = {} if template_flags is None else template_flags
        joint_flags = {} if joint_flags is None else joint_flags
        template_flags = {'meta_data': {'side': 'center', 'name': 'tripod'}}
        template_flags.update(addtl_template_flags)

        if not template_args:
            import pymel.core as pm
            pm.select(d=True)
            joints = []
            for i in range(num_joints):
                joint = nt.Joint.build(**joint_flags)
                rt.dcc.scene.position(joint, translation=[0, i, 0])
                joints.append(joint)
        else:
            joints = template_args
        sub_rig_instance = cls.TEMPLATE_CLASS(joints)
        sub_rig_instance.build(**template_flags)
        return sub_rig_instance


class TestBuildSpine(TestBaseTemplates):
    TEMPLATE_CLASS = Spine

    def test_build(self):
        self.runner()

    def test_build_with_parent(self):
        with sanitize():
            parent = nt.Transform.build(name='test')
            sub_rig_instance = self.runner(template_flags={'parent': parent})
            self.assertEqual(str(sub_rig_instance.root.get_parent()), str(parent))


class TestBuildBipedArm(TestBaseTemplates):
    TEMPLATE_CLASS = BipedArm

    @classmethod
    def from_template_file(cls, template_file):
        cls.import_template_files(template_file)
        l_arm = nt.NodeChain('l_armA_JNT')
        r_arm = nt.NodeChain('r_armA_JNT')
        l_sub_rig_instance = cls.runner(template_args=l_arm, template_flags={'meta_data': {'side': 'left'}})
        r_sub_rig_instance = cls.runner(template_args=r_arm, template_flags={'meta_data': {'side': 'right'}})
        return l_sub_rig_instance, r_sub_rig_instance

    def test_build(self):
        with sanitize():
            rig = self.runner()
            self.assertIsNotNone(rig)

    def test_build_with_parent(self):
        with sanitize():
            parent = nt.Transform.build(name='test')
            sub_rig_instance = self.runner(template_flags={'parent': parent})
            self.assertEqual(str(sub_rig_instance.root.get_parent()), str(parent))

    def test_build_with_imported_skeleton_t_pose(self):
        with sanitize():
            l_arm, r_arm = self.from_template_file(self.TPOSE)

    def test_build_with_imported_skeleton_a_pose(self):
        with sanitize():
            l_arm, r_arm = self.from_template_file(self.APOSE)
