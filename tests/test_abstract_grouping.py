import anvil.node_types as nt
import anvil.runtime as rt
import nomenclate
from base_test import TestBase
import sys

class TestBaseAbstractGrouping(TestBase):
    def build_test_dependencies(cls):
        pass


class TestAbstractGroupingInit(TestBaseAbstractGrouping):
    @TestBase.delete_created_nodes
    def test_meta_data(self):
        test_meta_data = {'blah': 'fart'}
        rig = nt.AbstractGrouping(meta_data={'blah': 'fart'}, top_node=None, layout=None, parent=None)
        test_meta_data.update(nt.AbstractGrouping.BUILT_IN_META_DATA)
        self.assertDictEqual(rig.meta_data, test_meta_data)

    @TestBase.delete_created_nodes
    def test_meta_data_nomenclate(self):
        test_meta_data = {'blah': 'fart'}
        rig = nt.AbstractGrouping(meta_data={'blah': 'fart'}, top_node=None, layout=None, parent=None)
        import nomenclate
        print nomenclate.__file__
        tokens = rig._nomenclate.token_dict.to_json()
        self.assertEquals({k: tokens[k]['label'] for k in tokens if k=='blah'}, test_meta_data)

    @TestBase.delete_created_nodes
    def test_top_node(self):
        test_top_node = nt.Transform.build()
        rig = nt.AbstractGrouping(meta_data=None, top_node=test_top_node, layout=None, parent=None)
        self.assertEquals(rig.top_node, test_top_node)

    @TestBase.delete_created_nodes
    def test_layout(self):
        layout = 'test'
        rig = nt.AbstractGrouping(meta_data=None, top_node=None, layout=layout, parent=None)
        self.assertEquals(rig.layout, layout)

    @TestBase.delete_created_nodes
    def test_parent_with_top_node(self):
        test_top_node = nt.Transform.build()
        test_parent_node = nt.Transform.build()
        rig = nt.AbstractGrouping(meta_data=None, top_node=test_top_node, layout=None, parent=test_parent_node)
        self.assertEquals(rig.top_node.getParent(), test_parent_node)

    @TestBase.delete_created_nodes
    def test_parent_without_top_node(self):
        test_parent_node = nt.Transform.build()
        rig = nt.AbstractGrouping(meta_data=None, top_node=None, layout=None, parent=test_parent_node)
        self.assertEquals(rig.top_node, None)

    @TestBase.delete_created_nodes
    def test_all(self):
        test_parent_node = nt.Transform.build()
        layout = 'test'
        test_top_node = nt.Transform.build()
        test_meta_data = {'blah': 'fart'}
        nt.AbstractGrouping(meta_data=test_meta_data, top_node=test_top_node, layout=layout, parent=test_parent_node)

    @TestBase.delete_created_nodes
    def test_kwargs(self):
        test_flags = {'blah': 'fart'}
        rig = nt.AbstractGrouping(meta_data=None, top_node=None, layout=None, parent=None, **test_flags)
        self.assertDictEqual(rig.flags, test_flags)


class TestAbstractGroupingMergeDicts(TestBaseAbstractGrouping):
    @TestBase.delete_created_nodes
    def test_meta_data_double(self):
        test_meta_data = {'foo': 'moo'}
        test_other_meta_data = {'bar': 'larp'}
        actual = {}
        actual.update(test_meta_data)
        actual.update(test_other_meta_data)
        merged_dict = nt.AbstractGrouping.merge_dicts(test_meta_data, test_other_meta_data)
        self.assertEquals(merged_dict, actual)

    @TestBase.delete_created_nodes
    def test_meta_data_single(self):
        test_meta_data = {'foo': 'moo'}
        actual = {}
        actual.update(test_meta_data)
        merged_dict = nt.AbstractGrouping.merge_dicts(test_meta_data)
        self.assertEquals(merged_dict, actual)

    @TestBase.delete_created_nodes
    def test_meta_data_empty(self):
        test_meta_data = {}
        actual = {}
        actual.update(test_meta_data)
        merged_dict = nt.AbstractGrouping.merge_dicts(test_meta_data)
        self.assertEquals(merged_dict, actual)

    @TestBase.delete_created_nodes
    def test_meta_data_none(self):
        test_meta_data = None
        merged_dict = nt.AbstractGrouping.merge_dicts(test_meta_data)
        self.assertEquals(merged_dict, {})


class TestAbstractGroupingParent(TestBaseAbstractGrouping):
    @TestBase.delete_created_nodes
    def test_empty_string(self):
        test_xform = nt.Transform.build()
        rig = nt.AbstractGrouping(top_node=test_xform)
        was_parented = rig.parent('')
        self.assertFalse(was_parented)

    @TestBase.delete_created_nodes
    def test_exists_but_no_top_node(self):
        test_xform = nt.Transform.build()
        rig = nt.AbstractGrouping()
        was_parented = rig.parent(test_xform)
        self.assertFalse(was_parented)

    @TestBase.delete_created_nodes
    def test_both_exist(self):
        test_xform = nt.Transform.build()
        test_top_node = nt.Transform.build()
        rig = nt.AbstractGrouping(top_node=test_top_node)
        was_parented = rig.parent(test_xform)
        self.assertTrue(was_parented)
