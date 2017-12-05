import anvil
import anvil.runtime as rt
import anvil.node_types as nt
import anvil.sub_rig_templates.spine as spine
import anvil.sub_rig_templates.biped_arm as biped_arm
import base_test
from pprint import pprint


class TestBaseTemplates(base_test.TestBase):
    name_tokens = {'name': 'eye', 'purpose': 'mvp'}
    test_rig = None
    TEMPLATE_CLASS = None

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
        pprint(anvil.runtime.dcc.scene.get_scene_tree())
        return sub_rig_instance


class TestBuildSpine(TestBaseTemplates):
    TEMPLATE_CLASS = spine.Spine

    def test_build(self):
        self.runner()

    @base_test.TestBase.delete_created_nodes
    def test_build_with_parent(self):
        parent = nt.Transform.build(name='test')
        sub_rig_instance = self.runner(template_flags={'parent': parent})
        self.assertEqual(str(sub_rig_instance.group_top.get_parent()), str(parent))


class TestBuildBipedArm(TestBaseTemplates):
    TEMPLATE_CLASS = biped_arm.BipedArm


    @classmethod
    def from_template_file(cls, template_file):
        cls.import_template_files(template_file)
        l_arm = nt.HierarchyChain('l_armA_JNT')
        r_arm = nt.HierarchyChain('r_armA_JNT')
        l_sub_rig_instance = cls.runner(template_args=l_arm.get_hierarchy_as_list(),
                                        template_flags={'meta_data': {'side': 'left'}})
        r_sub_rig_instance = cls.runner(template_args=r_arm.get_hierarchy_as_list(),
                                        template_flags={'meta_data': {'side': 'right'}})
        return l_sub_rig_instance, r_sub_rig_instance

    @base_test.TestBase.delete_created_nodes
    def test_build(self):
        rig = self.runner()
        self.assertIsNotNone(rig)

    @base_test.TestBase.delete_created_nodes
    def test_build_with_parent(self):
        parent = nt.Transform.build(name='test')
        sub_rig_instance = self.runner(template_flags={'parent': parent})
        self.assertEqual(str(sub_rig_instance.group_top.get_parent()), str(parent))

    @base_test.TestBase.delete_created_nodes
    def test_build_with_imported_skeleton_t_pose(self):
        l_arm, r_arm = self.from_template_file(self.TPOSE)

    @base_test.TestBase.delete_created_nodes
    def test_build_with_imported_skeleton_a_pose(self):
        l_arm, r_arm = self.from_template_file(self.APOSE)
