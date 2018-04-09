import anvil.node_types as nt
from base_test import TestBase, clean_up_scene


class TestBaseUnicodeDelegate(TestBase):
    pass


class TestUnicodeDelegateBuild(TestBaseUnicodeDelegate):
    @clean_up_scene
    def test_empty_input(self):
        self.assertRaises(NotImplementedError, nt.DagNode.build)

    @clean_up_scene
    def test_full_input(self):
        self.assertRaises(NotImplementedError, nt.DagNode.build)

    @clean_up_scene
    def test_partial_input(self):
        self.assertRaises(NotImplementedError, nt.DagNode.build)
