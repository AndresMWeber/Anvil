import anvil
import anvil.node_types as nt
from base_test import TestBase


class TestBaseRig(TestBase):
    def setUp(self):
        super(TestBaseRig, self).setUp()


class TestRigEyeBuild(TestBaseRig):
    def test_default(self):
        test_rig = nt.Rig([])
        test_rig.build()
        anvil.LOG.debug('test_rig.hierarchy = %s' % test_rig.hierarchy)
        anvil.LOG.debug('test_rig.control_universal = %s' % test_rig.find_node('control_universal'))
        anvil.LOG.info('Universal was created with name %s' % str(test_rig.find_node('control_universal')))
