import anvil.node_types as nt

from base_test import TestBase


class TestBaseUnicodeDelegate(TestBase):
    def setUp(self):
        super(TestBaseUnicodeDelegate, self).setUp()


class TestUnicodeDelegateBuild(TestBaseUnicodeDelegate):
    def test_empty_input(self):
        self.assertRaises(nt.DagNode.build, None, KeyError)

    def test_full_input(self):
        self.assertRaises(nt.DagNode.build, None, KeyError)

    def test_partial_input(self):
        self.assertRaises(nt.DagNode.build, None, KeyError)

class TestUnicodeDelegateRename(TestBaseUnicodeDelegate):
    pass