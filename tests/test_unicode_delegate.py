from base_test import TestBase
import anvil
import anvil.runtime as runtime
import anvil.core.objects.node_types as nt


class TestBaseUnicodeDelegate(TestBase):
    def setUp(self):
        super(TestBaseUnicodeDelegate, self).setUp()

    @staticmethod
    def encapsulation_node_creation():
        return {'node_dag': anvil.core.objects.curve.Curve.build(),
                'control_offset_grp': anvil.core.objects.transform.Transform.build(),
                'control_con_grp': anvil.core.objects.transform.Transform.build()
                }


class TestUnicodeDelegateBuild(TestBaseUnicodeDelegate):
    def test_empty_input(self):
        self.assertRaises(nt.DagNode.build, None, KeyError)

    def test_full_input(self):
        self.assertRaises(nt.DagNode.build, None, KeyError)

    def test_partial_input(self):
        self.assertRaises(nt.DagNode.build, None, KeyError)

class TestUnicodeDelegateRename(TestBaseUnicodeDelegate):
    pass