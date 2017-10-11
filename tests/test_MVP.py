from base_test import TestBase
import anvil
import anvil.core.objects.node_types as nt


class TestBaseRig(TestBase):
    def setUp(self):
        super(TestBaseRig, self).setUp()

    @staticmethod
    def encapsulation_node_creation():
        return {'node_dag': anvil.core.objects.curve.Curve.build(),
                'control_offset_grp': anvil.core.objects.transform.Transform.build(),
                'control_con_grp': anvil.core.objects.transform.Transform.build()
                }


class TestRigEyeBuild(TestBaseRig):
    def test_default(self):
        test_rig = anvil.core.collections.rig.Rig([])
        test_rig.build_root_hierarchy()
        anvil.LOG.debug('test_rig.hierarchy = %s' % test_rig.hierarchy)
        anvil.LOG.debug('test_rig.control_universal = %s' % test_rig.find_node('control_universal'))
        try:
            test_rig.find_node('control_universal')._pymel_node.name()
        except:
            pass

