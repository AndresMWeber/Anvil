import anvil.node_types as nt

from base_test import TestBase


class TestBaseSubRig(TestBase):
    def build_test_deps(cls):
        cls.test_rig = nt.SubRig([])
        cls.test_rig.build()


class TestSubRigBuild(TestBaseSubRig):
    @TestBase.delete_created_nodes
    def test_default(self):
        print(self.test_rig.hierarchy)


