import anvil
import anvil.runtime as rt
import anvil.node_types as nt
import anvil.templates.sub_rig.spine as spine
from base_test import TestBase


class TestBaseTemplates(TestBase):
    name_tokens = {'name': 'eye', 'purpose': 'mvp'}
    test_rig = None


class TestSpineBuild(TestBaseTemplates):
    @staticmethod
    def runner(num_joints=6, spine_flags=None, joint_flags=None):
        spine_flags = {} if spine_flags is None else spine_flags
        joint_flags = {} if joint_flags is None else joint_flags

        joints = []
        for i in range(num_joints):
            joint = nt.Joint.build(**joint_flags)
            rt.dcc.scene.position(joint, translation=[0, i, 0])
            joints.append(joint)

        sub_rig_instance = spine.Spine(joints)
        sub_rig_instance.build(**spine_flags)
        return sub_rig_instance

    @TestBase.delete_created_nodes
    def test_build(self):
        self.runner()

    @TestBase.delete_created_nodes
    def test_build_with_parent(self):
        parent = nt.Transform.build(name='test')
        print(parent)
        sub_rig_instance = self.runner(spine_flags={'parent': parent})
        print(type(sub_rig_instance.group_top))
        print(sub_rig_instance.group_top.get_parent())
        self.assertEqual(str(sub_rig_instance.group_top.get_parent()), str(parent))
