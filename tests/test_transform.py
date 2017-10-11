from base_test import TestBase
import anvil
import anvil.core.objects.node_types as nt


class TestBaseTransform(TestBase):
    def setUp(self):
        super(TestBaseTransform, self).setUp()

    @staticmethod
    def encapsulation_node_creation():
        return {'node_dag': anvil.core.objects.curve.Curve.build(),
                'control_offset_grp': anvil.core.objects.transform.Transform.build(),
                'control_con_grp': anvil.core.objects.transform.Transform.build()
                }


class TestTransformBuild(TestBaseTransform):
    def test_empty_input(self):
        nt.Transform.build()

    def test_full_input(self):
        nt.Transform.build()

    def test_partial_input(self):
        nt.Transform.build()

class TestTransformRename(TestBaseTransform):
    pass