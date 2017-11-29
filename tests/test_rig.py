import anvil.node_types as nt

from base_test import TestBase


class TestBaseRig(TestBase):
    def build_dependencies(cls):
        cls.test_rig = nt.Rig([])
        cls.test_rig.build()


class TestRigBuild(TestBaseRig):
    @TestBase.delete_created_nodes
    def test_default(self):
        # self.test_rig.hierarchy)
        pass
