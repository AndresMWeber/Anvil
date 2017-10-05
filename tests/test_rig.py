from base_test import TestBase
import anvil


class TestBaseRig(TestBase):
    def setUp(self):
        super(TestBaseRig, self).setUp()

    @staticmethod
    def encapsulation_node_creation():
        return {'node_dag': anvil.core.objects.curve.Curve.build(),
                'control_offset_grp': anvil.core.objects.transform.Transform.build(),
                'control_con_grp': anvil.core.objects.transform.Transform.build()
                }

class TestRigBuild(TestBaseRig):
    def test_default(self):
        anvil.core.collections.rig.Rig.build()
