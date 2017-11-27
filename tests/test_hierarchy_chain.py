import anvil.node_types as nt
import anvil.runtime as rt
from base_test import TestBase
from pprint import pprint
import anvil.config as cfg
import nomenclate.core.tools as ts

class TestBaseHierarchyChain(TestBase):
    joints = None
    joints_mixed = None
    joints_third = None
    group = None
    joints_total = None

    @classmethod
    def build_dependencies(cls, num_joints=6, joint_flags=None):
        try:
            joint_flags = joint_flags if joint_flags is not None else {}
            joints = []
            for i in range(num_joints):
                joint = nt.Joint.build(**joint_flags)
                rt.dcc.scene.position(joint, translation=[0, i, 0])
                joints.append(joint)
            cls.joints = joints

            joints_second = rt.dcc.scene.duplicate(joints, renameChildren=True)
            joints_third = rt.dcc.scene.duplicate(joints, renameChildren=True)
            group = nt.Transform.build(parent=joints_second[-1])
            rt.dcc.scene.parent(joints_third[0], group)
            cls.joints_mixed = joints_second
            cls.group = group
            cls.joints_third = joints_third
            cls.joints_total = joints_second + [group] + joints_third
            pprint(rt.dcc.scene.get_scene_tree())
        except:
            pprint(rt.dcc.scene.get_scene_tree())


class TestHierarchyChainInit(TestBaseHierarchyChain):
    @TestBase.delete_created_nodes
    def test_empty_input(self):
        self.assertRaises(TypeError, nt.HierarchyChain)

    @TestBase.delete_created_nodes
    def test_none_input(self):
        self.assertRaises(RuntimeError, nt.HierarchyChain, None)

    @TestBase.delete_created_nodes
    def test_full_list(self):
        nt.HierarchyChain(self.joints[0])

    @TestBase.delete_created_nodes
    def test_only_joints(self):
        nt.HierarchyChain(self.joints[0])

    @TestBase.delete_created_nodes
    def test_mixed_joints_and_transforms(self):
        nt.HierarchyChain(self.joints_mixed[0])


class TestHierarchyChainGetHierarchy(TestBaseHierarchyChain):
    @TestBase.delete_created_nodes
    def test_joints_only(self):
        chain = nt.HierarchyChain(self.joints[0])
        self.assertListEqual(self.joints, chain.get_hierarchy_as_list())

    @TestBase.delete_created_nodes
    def test_joints_mixed(self):
        chain = nt.HierarchyChain(self.joints_mixed[0])
        self.assertEqual(chain.get_hierarchy_as_list(), self.joints_mixed)

    @TestBase.delete_created_nodes
    def test_with_filter(self):
        chain = nt.HierarchyChain(self.joints_mixed[0], node_filter=[cfg.JOINT_TYPE, cfg.TRANSFORM_TYPE])
        self.assertEqual(chain.get_hierarchy_as_list(), self.joints_total)
