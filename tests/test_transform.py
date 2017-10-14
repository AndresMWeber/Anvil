import anvil.node_types as nt

from base_test import TestBase


class TestBaseTransform(TestBase):
    def setUp(self):
        super(TestBaseTransform, self).setUp()


class TestTransformBuild(TestBaseTransform):
    def test_empty_input(self):
        nt.Transform.build()

    def test_full_input(self):
        nt.Transform.build()

    def test_partial_input(self):
        nt.Transform.build()

class TestTransformRename(TestBaseTransform):
    pass