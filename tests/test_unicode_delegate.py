import anvil.node_types as nt

from base_test import TestBase


class TestBaseUnicodeDelegate(TestBase):
    pass


class TestUnicodeDelegateBuild(TestBaseUnicodeDelegate):
    @TestBase.delete_created_nodes
    def test_empty_input(self):
        self.assertRaises(NotImplementedError, nt.DagNode.build)

    @TestBase.delete_created_nodes
    def test_full_input(self):
        self.assertRaises(NotImplementedError, nt.DagNode.build)

    @TestBase.delete_created_nodes
    def test_partial_input(self):
        self.assertRaises(NotImplementedError, nt.DagNode.build)
