from anvil.sub_rig_templates import base_sub_rig_template
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
        self.assertEqual(generic.to_size_list(input, 5), input)

    def test_kwarg_shape_input(self):
        self.assertEqual(generic.to_size_list('pyramid', 6), ['pyramid'] * 6)
