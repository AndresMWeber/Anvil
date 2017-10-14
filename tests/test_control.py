import  anvil.node_types as nt

from base_test import TestBase


class TestBaseControl(TestBase):
    def setUp(self):
        super(TestBaseControl, self).setUp()
        self.node_dag = nt.Curve.build()
        self.control_offset_grp = nt.Transform.build()
        self.control_con_grp = nt.Transform.build()


class TestControlInit(TestBaseControl):
    pass


class TestControlBuild(TestBaseControl):
    def test_empty_input(self):
        nt.Control.build()

    def test_full_input(self):
        nt.Control.build()

    def test_partial_input(self):
        nt.Control.build()

    def test_shape_input(self):
        nt.Control.build(shape='cube')


class TestControlRename(TestBaseControl):
    pass
