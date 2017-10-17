import anvil.node_types as nt

from base_test import TestBase


class TestBaseRig(TestBase):
    pass


class TestRigBuild(TestBaseRig):
    @TestBase.delete_created_nodes
    def test_default(self):
        test_rig = nt.Rig([])
        test_rig.build()


