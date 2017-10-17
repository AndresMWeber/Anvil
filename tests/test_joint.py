import anvil.node_types as nt

from base_test import TestBase


class TestBaseJoint(TestBase):
    pass


class TestJointBuild(TestBaseJoint):
    @TestBase.delete_created_nodes
    def test_empty_input(self):
        nt.Joint.build()

    @TestBase.delete_created_nodes
    def test_full_input(self):
        nt.Joint.build()

    @TestBase.delete_created_nodes
    def test_partial_input(self):
        nt.Joint.build()
