from base_test import TestBase
import anvil
import anvil.core.objects.node_types as nt


class TestBaseCurve(TestBase):
    def setUp(self):
        super(TestBaseCurve, self).setUp()
        self.null_transform = nt.Transform.build()


class TestCurveBuild(TestBaseCurve):
    def test_empty_input(self):
        nt.Curve.build()

    def test_full_input(self):
        nt.Curve.build()

    def test_partial_input(self):
        nt.Curve.build()

    def test_with_parent(self):
        nt.Curve.build(parent=self.null_transform)

class TestCurveRename(TestBaseCurve):
    pass