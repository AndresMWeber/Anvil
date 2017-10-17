import anvil
import anvil.node_types as nt
from base_test import TestBase


class TestBaseRig(TestBase):
    pass


class TestRigEyeBuild(TestBaseRig):
    @TestBase.delete_created_nodes
    def test_default(self):
        test_rig = nt.Rig([])
        test_rig.build()
        test_rig.rename(name='eye', purpose='mvp')
        anvil.LOG.debug('test_rig.hierarchy = %s' % test_rig.hierarchy)
        anvil.LOG.debug('test_rig.control_universal = %s' % test_rig.find_node('control_universal'))
        anvil.LOG.info('Universal was created with name %s' % str(test_rig.find_node('control_universal')))
