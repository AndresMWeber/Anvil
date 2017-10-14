import anvil.node_types as nt

from base_test import TestBase


class TestBaseDagNode(TestBase):
    def setUp(self):
        super(TestBaseDagNode, self).setUp()


class TestDagNodeBuild(TestBaseDagNode):
    def test_empty_input(self):
        self.assertRaises(nt.DagNode.build, None, KeyError)

    def test_full_input(self):
        self.assertRaises(nt.DagNode.build, None, KeyError)

    def test_partial_input(self):
        self.assertRaises(nt.DagNode.build, None, KeyError)

class TestDagNodeRename(TestBaseDagNode):
    pass