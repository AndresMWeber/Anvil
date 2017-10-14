import anvil.node_types as nt

from base_test import TestBase


class TestBaseJoint(TestBase):
    def setUp(self):
        super(TestBaseJoint, self).setUp()



class TestJointBuild(TestBaseJoint):
    def test_empty_input(self):
        nt.Joint.build()

    def test_full_input(self):
        nt.Joint.build()

    def test_partial_input(self):
        nt.Joint.build()

class TestJointRename(TestBaseJoint):
    pass