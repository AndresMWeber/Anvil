import anvil.meta_data as md
from base_test import TestBase


class TestBaseMetaData(TestBase):
    def build_dependencies(cls):
        pass


class TestMetaDataMergeDicts(TestBaseMetaData):
    @TestBase.delete_created_nodes
    def test_meta_data_double(self):
        test_meta_data = {'foo': 'moo'}
        test_other_meta_data = {'bar': 'larp'}
        actual = {}
        actual.update(test_meta_data)
        actual.update(test_other_meta_data)
        merged_dict = md.MetaData.merge_dicts(test_meta_data, test_other_meta_data)
        self.assertEquals(merged_dict, actual)

    @TestBase.delete_created_nodes
    def test_meta_data_single(self):
        test_meta_data = {'foo': 'moo'}
        actual = {}
        actual.update(test_meta_data)
        merged_dict = md.MetaData.merge_dicts(test_meta_data)
        self.assertEquals(merged_dict, actual)

    @TestBase.delete_created_nodes
    def test_meta_data_empty(self):
        test_meta_data = {}
        actual = {}
        actual.update(test_meta_data)
        merged_dict = md.MetaData.merge_dicts(test_meta_data)
        self.assertEquals(merged_dict, actual)

    @TestBase.delete_created_nodes
    def test_meta_data_none(self):
        test_meta_data = None
        merged_dict = md.MetaData.merge_dicts(test_meta_data)
        self.assertEquals(merged_dict, {})
