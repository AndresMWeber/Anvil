from base_test import TestBase
import anvil.utils.generic as generic


class TestBaseGeneric(TestBase):
    pass


class TestToSizeList(TestBaseGeneric):
    def test_input_shape_list(self):
        input = ['f', 'g', 'h', 'i']
        self.assertEqual(generic.to_size_list(input, 4), input)

    def test_short_shape_list(self):
        input = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.assertEqual(generic.to_size_list(input, 14),
                         ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] + ['h'] * 6)

    def test_short_shape_list_by_one(self):
        input = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.assertEqual(generic.to_size_list(input, 9),
                         ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'h'])

    def test_over_length_shape_list(self):
        input = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.assertEqual(generic.to_size_list(input, 5), input[:5])

    def test_kwarg_shape_input(self):
        self.assertEqual(generic.to_size_list('pyramid', 6), ['pyramid'] * 6)


class TestToList(TestBaseGeneric):
    def test_list(self):
        self.assertEqual(generic.to_list([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_str(self):
        self.assertEqual(generic.to_list('testy'), ['testy'])

    def test_none(self):
        self.assertEqual(generic.to_list(None), [])

    def test_empty_list(self):
        self.assertEqual(generic.to_list([]), [])

    def test_empty_str(self):
        self.assertEqual(generic.to_list(''), [''])

    def test_empty_dict(self):
        self.assertEqual(generic.to_list({}), [{}])

    def test_int(self):
        self.assertEqual(generic.to_list(5), [5])

    def test_int_zero(self):
        self.assertEqual(generic.to_list(0), [])

    def test_set(self):
        self.assertEqual(generic.to_list({1, 2, 3, 4}), [1, 2, 3, 4])


class TestCamelCase(TestBaseGeneric):
    def test_no_split(self):
        self.assertEqual(generic.to_camel_case('asdf'), 'asdf')

    def test_two_split(self):
        self.assertEqual(generic.to_camel_case('asdf_asdf'), 'asdfAsdf')

    def test_empty(self):
        self.assertEqual(generic.to_camel_case(''), '')

    def test_three_split(self):
        self.assertEqual(generic.to_camel_case('my_little_pony_is_stupid'), 'myLittlePonyIsStupid')
