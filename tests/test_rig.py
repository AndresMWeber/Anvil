import anvil.node_types as nt

from base_test import TestBase


class TestBaseRig(TestBase):
    def setUp(self):
        super(TestBaseRig, self).setUp()


class TestRigBuild(TestBaseRig):
    def test_default(self):
        test_rig = nt.Rig([])

    def test_curve(self):
        point = {'point': [[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 3, 0]]}
        nt.Curve.build(flags=point)

