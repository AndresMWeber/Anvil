import anvil.meta_data as md
from base_test import TestBase


class TestBaseMetaData(TestBase):
    test_meta_data = {'foo': 'moo'}
    test_other_meta_data = {'bar': 'larp'}

    test_combined = {}
    test_combined.update(test_meta_data)
    test_combined.update(test_other_meta_data)

    test_total_meta_data_overwrite = {'foo': 'boo', 'bar': 'farp'}
    test_other_meta_data_overwrite = {'bar': 'marp'}

    test_overwritten = test_combined.copy()
    test_overwritten.update(test_other_meta_data_overwrite)

    def build_dependencies(cls):
        pass


class TestMetaDataMergeDicts(TestBaseMetaData):
    def test_meta_data_double(self):
        merged_dict = md.MetaData().merge(self.test_meta_data, self.test_other_meta_data)
        self.assertEquals(merged_dict, self.test_combined)

    def test_meta_data_single(self):
        merged_dict = md.MetaData().merge(self.test_meta_data)
        self.assertEquals(merged_dict, self.test_meta_data)

    def test_meta_data_empty(self):
        test_meta_data = {}
        actual = {}
        actual.update(test_meta_data)
        merged_dict = md.MetaData().merge(test_meta_data)
        self.assertEquals(merged_dict, actual)

    def test_meta_data_none(self):
        test_meta_data = None
        merged_dict = md.MetaData().merge(test_meta_data)
        self.assertEquals(merged_dict, {})


class TestKeys(TestBaseMetaData):
    def test_default_merge(self):
        meta_data_object = md.MetaData()
        meta_data_object.merge(self.test_meta_data, self.test_other_meta_data)
        self.assertEquals(meta_data_object.keys(), list(self.test_combined))

    def test_initialize_with_dicts(self):
        meta_data_object = md.MetaData(self.test_meta_data, self.test_other_meta_data)
        self.assertEquals(meta_data_object.keys(), list(self.test_combined))

    def test_initialize_with_dict_and_splat(self):
        meta_data_object = md.MetaData(self.test_meta_data, **self.test_other_meta_data)
        self.assertEquals(meta_data_object.keys(), list(self.test_combined))


class TestSplatting(TestBaseMetaData):
    @staticmethod
    def single_splat_returner(*args):
        return args

    @staticmethod
    def double_splat_returner(**kwargs):
        return kwargs

    def test_single_from_merge(self):
        meta_data_object = md.MetaData()
        meta_data_object.merge(self.test_meta_data, self.test_other_meta_data)
        self.assertEquals(tuple(meta_data_object.keys()), self.single_splat_returner(*meta_data_object))

    def test_double_from_init(self):
        meta_data_object = md.MetaData(self.test_meta_data, self.test_other_meta_data)
        self.assertEquals(meta_data_object, self.double_splat_returner(**meta_data_object.to_dict()))


class TestMerge(TestBaseMetaData):
    def test_default_merge(self):
        meta_data_object = md.MetaData()
        meta_data_object.merge(self.test_meta_data, self.test_other_meta_data)
        self.assertEquals(meta_data_object, self.test_combined)

    def test_initialize_with_dicts(self):
        meta_data_object = md.MetaData(self.test_meta_data, self.test_other_meta_data)
        self.assertEquals(meta_data_object, self.test_combined)

    def test_initialize_with_dict_and_splat(self):
        meta_data_object = md.MetaData(self.test_meta_data, **self.test_other_meta_data)
        self.assertEquals(meta_data_object, self.test_combined)


class TestProtection(TestBaseMetaData):
    def test_overwrite_merge(self):
        meta_data_object = md.MetaData(self.test_combined)
        meta_data_object.merge(self.test_other_meta_data_overwrite)
        self.assertEquals(meta_data_object, self.test_overwritten)

    def test_protected_merge_force(self):
        meta_data_object = md.MetaData(self.test_combined, protected='bar')
        meta_data_object.merge(self.test_other_meta_data_overwrite, force=True)
        self.assertEquals(meta_data_object, self.test_overwritten)

    def test_protected_multi_merge_force(self):
        meta_data_object = md.MetaData(self.test_combined, protected=['foo', 'bar'])
        meta_data_object.merge(self.test_total_meta_data_overwrite, force=True)
        self.assertEquals(meta_data_object, self.test_total_meta_data_overwrite)

    def test_protected_single_merge_force(self):
        meta_data_object = md.MetaData(self.test_combined, protected=['foo'])
        meta_data_object.merge(self.test_total_meta_data_overwrite, force=True)
        self.assertEquals(meta_data_object, self.test_total_meta_data_overwrite)

    def test_protected_merge(self):
        meta_data_object = md.MetaData(self.test_combined, protected='bar')
        meta_data_object.merge(self.test_other_meta_data_overwrite)
        self.assertEquals(meta_data_object, self.test_combined)

    def test_protected_merge_as_list(self):
        meta_data_object = md.MetaData(self.test_combined, protected=['bar'])
        meta_data_object.merge(self.test_other_meta_data_overwrite)
        self.assertEquals(meta_data_object, self.test_combined)

    def test_add_protection_via_method(self):
        meta_data_object = md.MetaData(self.test_combined, protected=['bar'])
        meta_data_object.merge(self.test_other_meta_data_overwrite)
        self.assertEquals(meta_data_object, self.test_combined)

    def test_add_protection_manually(self):
        meta_data_object = md.MetaData(self.test_combined)
        meta_data_object.protected |= {'bar'}
        meta_data_object.merge(self.test_other_meta_data_overwrite)
        self.assertEquals(meta_data_object, self.test_combined)

    def test_add_protection_manually_overwrite(self):
        meta_data_object = md.MetaData(self.test_combined)
        meta_data_object.protected = ['bar']
        meta_data_object.merge(self.test_other_meta_data_overwrite)
        self.assertEquals(meta_data_object, self.test_combined)
