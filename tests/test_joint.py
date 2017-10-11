from base_test import TestBase
import anvil
import anvil.core.objects.node_types as nt


class TestBaseJoint(TestBase):
    def setUp(self):
        super(TestBaseJoint, self).setUp()

    @staticmethod
    def encapsulation_node_creation():
        return {'node_dag': anvil.core.objects.curve.Curve.build(),
                'control_offset_grp': anvil.core.objects.transform.Transform.build(),
                'control_con_grp': anvil.core.objects.transform.Transform.build()
                }


class TestJointBuild(TestBaseJoint):
    def test_empty_input(self):
        nt.Joint.build()

    def test_full_input(self):
        nt.Joint.build()

    def test_partial_input(self):
        nt.Joint.build()

class TestJointRename(TestBaseJoint):
    pass