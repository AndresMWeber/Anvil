from base_test import TestBase
from anvil.utils.generic import Map


class TestBaseMap(TestBase):
    simple = {'test': 1}
    simple_values = [1]
    nested = {'test': {'fest': 4}}
    nested_values = [4]
    nested_complex = {'test': {'fest': 4},
                      'fart': {'blest':
                                   {'mesh':
                                        4}},
                      4: 3}
    nested_complex_values = [4, 4, 3]
    nested_complex_values_depth_two = [3, 4, {'mesh': 4}]

    def setUp(self):
        self.map = Map()


class TestDeepUpdate(TestBaseMap):
    def test_empty(self):
        self.map.deep_update({})
        self.assertEqual(self.map, {})

    def test_simple_dict(self):
        self.map.deep_update(self.simple)
        self.assertEqual(self.map, self.simple)

    def test_nested_dict(self):
        self.map.deep_update(self.nested)
        self.assertEqual(self.map, self.nested)

    def test_nested_complex(self):
        self.map.deep_update(self.nested_complex)
        self.assertEqual(self.map, self.nested_complex)


class TestEq(TestBaseMap):
    def test_empty(self):
        self.assertTrue(Map({}) == {})

    def test_simple_dict(self):
        self.assertTrue(Map(self.simple) == self.simple)

    def test_nested_dict(self):
        self.assertTrue(Map(self.nested) == self.nested)

    def test_nested_complex(self):
        self.assertTrue(Map(self.nested_complex) == self.nested_complex)


class TestFlatten(TestBaseMap):
    def test_empty(self):
        self.assertItemsEqual(Map({}).flatten(), {})

    def test_simple_dict(self):
        self.assertItemsEqual(Map(self.simple).flatten(), self.simple_values)

    def test_nested_dict(self):
        self.assertItemsEqual(Map(self.nested).flatten(), self.nested_values)

    def test_nested_complex(self):
        self.assertItemsEqual(Map(self.nested_complex).flatten(), self.nested_complex_values_depth_two)


class TestToValueList(TestBaseMap):
    def test_empty(self):
        self.assertItemsEqual(Map({}), [])

    def test_simple_dict(self):
        self.assertItemsEqual(Map(self.simple).to_value_list(), self.simple_values)

    def test_nested_dict(self):
        self.assertItemsEqual(Map(self.nested).to_value_list(), self.nested_values)

    def test_nested_complex(self):
        self.assertItemsEqual(Map(self.nested_complex).to_value_list(), self.nested_complex_values)


class TestToFlatDict(TestBaseMap):
    def test_empty(self):
        self.assertEqual(Map({}).to_flat_dict(), {})

    def test_simple_dict(self):
        self.assertEqual(Map(self.simple).to_flat_dict(), self.simple)

    def test_nested_dict(self):
        self.assertEqual(Map(self.nested).to_flat_dict(), self.nested['test'])

    def test_nested_complex(self):
        self.assertEqual(Map(self.nested_complex).to_flat_dict(),
                         {'fest': 4, 'mesh': 4, 4: 3})
