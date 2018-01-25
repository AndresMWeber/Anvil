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

class TestJointApiNodeDelegation(TestBaseJoint):
    @TestBase.delete_created_nodes
    def test_instance_exists(self):
        joint = nt.Joint.build()
        self.assertIsNotNone(joint._api_class_instance)

    @TestBase.delete_created_nodes
    def test_attr_set(self):
        joint = nt.Joint.build()
        joint.jointOrient.set([0,0,0])
        self.assertEqual(joint.jointOrient.get().get(), (0,0,0))

    @TestBase.delete_created_nodes
    def test_use_method(self):
        joint = nt.Joint.build()
        name = joint.shortName()
        self.assertEqual(name, joint.name())

    @TestBase.delete_created_nodes
    def test_encapsulate(self):
        joint = nt.Joint.build()
        joint = nt.Joint(str(joint))
        name = joint.shortName()
        self.assertEqual(name, joint.name())
