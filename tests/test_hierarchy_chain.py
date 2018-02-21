import anvil.node_types as nt
import anvil.runtime as rt
import anvil
from base_test import TestBase
import anvil.config as cfg


class TestBaseHierarchyChain(TestBase):
    joints = None
    joints_mixed = None
    joints_third = None
    group = None
    joints_total = None

    @classmethod
    def build_dependencies(cls, num_joints=6, joint_flags=None):
        joint_flags = joint_flags or {}
        joints = []
        for i in range(num_joints):
            joint = nt.Joint.build(**joint_flags)
            rt.dcc.scene.position(joint, translation=[0, i, 0])
            joints.append(joint)
        cls.joints = joints

        cls.joints_second = rt.dcc.scene.duplicate(joints, renameChildren=True)
        cls.joints_third = rt.dcc.scene.duplicate(joints, renameChildren=True)
        group = nt.Transform.build(parent=cls.joints_second[-1])
        rt.dcc.scene.parent(cls.joints_third[0], group)
        cls.joints_mixed = cls.joints_second
        cls.group = group
        cls.joints_third = cls.joints_third
        cls.joints_total = cls.joints_second + [group] + cls.joints_third


class TestHierarchyChainInit(TestBaseHierarchyChain):
    @TestBase.delete_created_nodes
    def test_empty_input(self):
        self.assertRaises(TypeError, nt.LinearHierarchyNodeSet)

    @TestBase.delete_created_nodes
    def test_none_input(self):
        self.assertRaises(IOError, nt.LinearHierarchyNodeSet, None)

    @TestBase.delete_created_nodes
    def test_full_list(self):
        nt.LinearHierarchyNodeSet(self.joints[0])

    @TestBase.delete_created_nodes
    def test_only_joints(self):
        nt.LinearHierarchyNodeSet(self.joints[0])

    @TestBase.delete_created_nodes
    def test_mixed_joints_and_transforms(self):
        nt.LinearHierarchyNodeSet(self.joints_mixed[0])

    @TestBase.delete_created_nodes
    def test_duplicate(self):
        self.assertEqual(len(list(nt.LinearHierarchyNodeSet(self.joints_total[0], self.joints_total[-3], duplicate=True))),
                         len(self.joints_total) - 2)

    @TestBase.delete_created_nodes
    def test_duplicate_no_end_specified(self):
        self.assertEqual(len(nt.LinearHierarchyNodeSet(self.joints_total[0], duplicate=True,
                                                       node_filter=[cfg.JOINT_TYPE, cfg.TRANSFORM_TYPE])),
                         len(self.joints_total))

    @TestBase.delete_created_nodes
    def test_pynode_input(self):
        import pymel.core as pm
        nodes = [pm.createNode('joint')]
        nodes.append(pm.createNode('joint', parent=nodes[0]))
        self.checkEqual([str(f) for f in list(nt.LinearHierarchyNodeSet(nodes[0]))],
                        [str(f) for f in list(nodes)])

    @TestBase.delete_created_nodes
    def test_str_input(self):
        import maya.cmds as mc
        nodes = [mc.createNode('joint')]
        nodes.append(mc.createNode('joint', parent=nodes[0]))
        self.checkEqual([str(f) for f in list(nt.LinearHierarchyNodeSet(nodes[0]))],
                        nodes)

    @TestBase.delete_created_nodes
    def test_anvil_input(self):
        nodes = [nt.Joint.build()]
        nodes.append(nt.Joint.build(parent=nodes[0]))
        self.checkEqual([str(f) for f in list(nt.LinearHierarchyNodeSet(str(nodes[0])))],
                        [str(f) for f in list(nodes)])


class TestHierarchyChainGetHierarchy(TestBaseHierarchyChain):
    @TestBase.delete_created_nodes
    def test_joints_only(self):
        chain = nt.LinearHierarchyNodeSet(self.joints[0])
        self.assertListEqual(self.joints, chain.get_hierarchy(as_list=True))

    @TestBase.delete_created_nodes
    def test_joints_mixed(self):
        chain = nt.LinearHierarchyNodeSet(self.joints_mixed[0])
        self.assertEqual(chain.get_hierarchy(as_list=True), [anvil.factory(j) for j in self.joints_total])

    @TestBase.delete_created_nodes
    def test_with_filter(self):
        chain = nt.LinearHierarchyNodeSet(self.joints_mixed[0], node_filter=[cfg.JOINT_TYPE, cfg.TRANSFORM_TYPE])
        self.assertEqual(chain.get_hierarchy(as_list=True), self.joints_total)


class TestHierarchyChainIteration(TestBaseHierarchyChain):
    @TestBase.delete_created_nodes
    def test_first_member(self):
        chain = nt.LinearHierarchyNodeSet(self.joints[0])
        self.assertEquals(chain[0], self.joints[0])

    @TestBase.delete_created_nodes
    def test_negative_indexing(self):
        chain = nt.LinearHierarchyNodeSet(self.joints[0])
        self.assertEquals(chain[-1], self.joints[-1])

    @TestBase.delete_created_nodes
    def test_invalid_index(self):
        chain = nt.LinearHierarchyNodeSet(self.joints[0])
        with self.assertRaises(IndexError) as exception_context_manager:
            f = chain[40]
        exception = exception_context_manager.exception

    @TestBase.delete_created_nodes
    def test_all_members(self):
        chain = nt.LinearHierarchyNodeSet(self.joints[0])
        self.checkEqual(chain, self.joints)

    @TestBase.delete_created_nodes
    def test_specified_end_node(self):
        chain = nt.LinearHierarchyNodeSet(self.joints_total[0], self.joints_second[-1])
        self.checkEqual(chain, self.joints_second)

    @TestBase.delete_created_nodes
    def test_specified_end_node_with_node_filter(self):
        chain = nt.LinearHierarchyNodeSet(self.joints_mixed[0], self.joints_total[-3], node_filter=cfg.JOINT_TYPE)
        self.checkEqual(chain, self.joints)

    @TestBase.delete_created_nodes
    def test_specified_end_node_with_node_filter_all(self):
        chain = nt.LinearHierarchyNodeSet(self.joints_mixed[0], self.joints_total[-3],
                                          node_filter=[cfg.JOINT_TYPE, cfg.TRANSFORM_TYPE])
        self.checkEqual(chain, self.joints_total[:-3])


class TestHierarchyChainDepth(TestBaseHierarchyChain):
    @TestBase.delete_created_nodes
    def test_joints_only(self):
        chain = nt.LinearHierarchyNodeSet(self.joints[0])
        self.assertEqual(chain.depth(), len(self.joints) - 1)

    @TestBase.delete_created_nodes
    def test_joints_mixed(self):
        chain = nt.LinearHierarchyNodeSet(self.joints_mixed[0])
        self.assertEqual(chain.depth(), len(self.joints_total) - 1)

    @TestBase.delete_created_nodes
    def test_with_filter(self):
        chain = nt.LinearHierarchyNodeSet(self.joints_mixed[0], node_filter=[cfg.JOINT_TYPE, cfg.TRANSFORM_TYPE])
        self.assertEqual(chain.depth(), len(self.joints_total) - 1)


class TestHierarchyGetLevel(TestBaseHierarchyChain):
    @TestBase.delete_created_nodes
    def test_joints_only(self):
        chain = nt.LinearHierarchyNodeSet(self.joints[0])
        self.assertEqual(chain.get_level(4), nt.LinearHierarchyNodeSet(self.joints[4]).get_hierarchy())

    @TestBase.delete_created_nodes
    def test_joints_mixed(self):
        chain = nt.LinearHierarchyNodeSet(self.joints_mixed[0])
        self.assertDictEqual(chain.get_level(4), nt.LinearHierarchyNodeSet(self.joints_mixed[4]).get_hierarchy())

    @TestBase.delete_created_nodes
    def test_with_filter(self):
        filter = [cfg.JOINT_TYPE, cfg.TRANSFORM_TYPE]
        chain = nt.LinearHierarchyNodeSet(self.joints_total[0], node_filter=filter)
        self.assertDictEqual(chain.get_level(8),
                             nt.LinearHierarchyNodeSet(self.joints_total[8], node_filter=filter).get_hierarchy())
