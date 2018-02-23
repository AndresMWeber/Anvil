import anvil.node_types as nt
from base_test import TestBase, clean_up_scene


class TestBaseTransform(TestBase):
    pass


class TestTransformBuild(TestBaseTransform):
    @clean_up_scene
    def test_empty_input(self):
        nt.Transform.build()

    @clean_up_scene
    def test_full_input(self):
        nt.Transform.build()

    @clean_up_scene
    def test_partial_input(self):
        nt.Transform.build()


class TestTransformDelegation(TestBaseTransform):
    @clean_up_scene
    def test_get_parent(self):
        self.assertEquals(nt.Transform.build().getParent(), None)

    @clean_up_scene
    def test_set_parent(self):
        a = nt.Transform.build()
        b = nt.Transform.build()
        a.parent(b)
        self.assertEquals(a.getParent(), b)
