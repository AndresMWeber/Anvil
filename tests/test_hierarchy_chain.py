import anvil.node_types as nt
import anvil.runtime as rt
from base_test import TestBase
from pprint import pprint
import anvil.config as cfg


class TestBaseHierarchyChain(TestBase):
    joints = None
    joints_mixed = None
    joints_third = None
    group = None
    joints_total = None

    @classmethod
    def build_dependencies(cls, num_joints=6, joint_flags=None):
        try:
            joint_flags = joint_flags or {}
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
            pprint('dependencies-built:', rt.dcc.scene.get_scene_tree())
        except:
            pprint('dependencies-build-failed:', rt.dcc.scene.get_scene_tree())


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


class TestHierarchyChainIteration(TestBaseHierarchyChain):
    @TestBase.delete_created_nodes
    def test_first_member(self):
        chain = nt.HierarchyChain(self.joints[0])
        self.assertEquals(chain[0], self.joints[0])

    @TestBase.delete_created_nodes
    def test_negative_indexing(self):
        chain = nt.HierarchyChain(self.joints[0])
        self.assertEquals(chain[-1], self.joints[-1])

    @TestBase.delete_created_nodes
    def test_invalid_index(self):
        chain = nt.HierarchyChain(self.joints[0])
        with self.assertRaises(IndexError) as exception_context_manager:
            f = chain[40]
        exception = exception_context_manager.exception

    @TestBase.delete_created_nodes
    def test_all_members(self):
        chain = nt.HierarchyChain(self.joints[0])
        self.checkEqual(chain, self.joints)

class TestHierarchyChainDepth(TestBaseHierarchyChain):
    @TestBase.delete_created_nodes
    def test_joints_only(self):
        chain = nt.HierarchyChain(self.joints[0])
        self.assertEqual(chain.depth(), len(self.joints) - 1)

    @TestBase.delete_created_nodes
    def test_joints_mixed(self):
        chain = nt.HierarchyChain(self.joints_mixed[0])
        self.assertEqual(chain.depth(), len(self.joints) - 1)

    @TestBase.delete_created_nodes
    def test_with_filter(self):
        chain = nt.HierarchyChain(self.joints_mixed[0], node_filter=[cfg.JOINT_TYPE, cfg.TRANSFORM_TYPE])
        self.assertEqual(chain.depth(), len(self.joints_total) - 1)


class TestHierarchyGetLevel(TestBaseHierarchyChain):
    @TestBase.delete_created_nodes
    def test_joints_only(self):
        chain = nt.HierarchyChain(self.joints[0])
        self.assertEqual(chain.get_level(4), nt.HierarchyChain(self.joints[4]).get_hierarchy())

    @TestBase.delete_created_nodes
    def test_joints_mixed(self):
        chain = nt.HierarchyChain(self.joints_mixed[0])
        self.assertEqual(chain.get_level(4), nt.HierarchyChain(self.joints_mixed[4]).get_hierarchy())

    @TestBase.delete_created_nodes
    def test_with_filter(self):
        filter = [cfg.JOINT_TYPE, cfg.TRANSFORM_TYPE]
        chain = nt.HierarchyChain(self.joints_total[0], node_filter=filter)
        self.assertDictEqual(chain.get_level(8),
                             nt.HierarchyChain(self.joints_total[8], node_filter=filter).get_hierarchy())
