import anvil.node_types as nt
import anvil.runtime as rt
from base_test import TestBase


class TestBaseCurve(TestBase):
    def setUp(self):
        super(TestBaseCurve, self).setUp()
        self.null_transform = nt.Transform.build()


class TestCurveBuild(TestBaseCurve):
    @TestBase.delete_created_nodes
    def test_empty_input(self):
        nt.Curve.build()

    @TestBase.delete_created_nodes
    def test_full_input(self):
        nt.Curve.build(name='test_curve',
                       append=False,
                       bezier=True,
                       degree=3,
                       objectSpace=False,
                       periodic=False,
                       point=[[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 3, 0]],
                       replace=False,
                       worldSpace=True)

    @TestBase.delete_created_nodes
    def test_partial_input(self):
        nt.Curve.build(bezier=True,
                       worldSpace=True,
                       point=[[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 3, 0]])

    @TestBase.delete_created_nodes
    def test_point_input(self):
        curve = nt.Curve.build(point=[[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 3, 0]])
        try:
            self.assertEqual(curve.getShape().numCVs(), 4)
        except AttributeError:
            self.assertIsNotNone(curve)

    @TestBase.delete_created_nodes
    def test_shape_input(self):
        curve = nt.Curve.build(shape='jack')
        print(nt.Curve.SHAPE_CACHE)
        try:
            self.assertEqual(curve.getShape().numCVs(), len(nt.Curve.SHAPE_CACHE['jack']['point']))
        except AttributeError:
            self.assertIsNotNone(curve)

    @TestBase.delete_created_nodes
    def test_with_parent(self):
        curve = nt.Curve.build(parent=nt.Transform.build())
        if 'standalone' in rt.dcc.ENGINE:
            self.assertTrue(curve.get_parent() == 'curve')
        else:
            self.assertTrue(self.null_transform == curve.get_parent())


class TestCurveGetShapeConstructor(TestBaseCurve):
    @TestBase.delete_created_nodes
    def existing_shape(self):
        shape_lambda = nt.Curve._get_shape_constructor('star')
        shape_lambda()

    @TestBase.delete_created_nodes
    def existing_shape_positions(self):
        positions_dict = nt.Curve._get_shape_constructor('star', return_positions=True)
        self.assertListEqual(list(positions_dict), ['point', 'degree'])

    @TestBase.delete_created_nodes
    def non_existing_shape(self):
        self.assertIsNone(nt.Curve._get_shape_constructor('corndog'))


class TestCurvePopulateShapeFileData(TestBaseCurve):
    @TestBase.delete_created_nodes
    def existing_shape_file(self):
        self.assertIsNotNone(nt.Curve._populate_shape_file_data().SHAPE_CACHE)

    @TestBase.delete_created_nodes
    def non_existing_shape_file(self):
        nt.Curve.SHAPE_CACHE = None
        self.assertEquals(nt.Curve._populate_shape_file_data('not a file').SHAPE_CACHE, {})
