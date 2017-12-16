import anvil.node_types as nt
from base_test import TestBase

class TestBaseAbstractGrouping(TestBase):
    def build_dependencies(cls):
        pass


class TestAbstractGroupingInit(TestBaseAbstractGrouping):
    @TestBase.delete_created_nodes
    def test_meta_data(self):
        test_meta_data = {'blah': 'fart'}
        rig = nt.AbstractGrouping(meta_data=test_meta_data, top_node=None, layout_joints=None, parent=None)
        test_meta_data.update(nt.AbstractGrouping.BUILT_IN_META_DATA)
        self.assertDictEqual(rig.meta_data, test_meta_data)

    @TestBase.delete_created_nodes
    def test_meta_data_nomenclate(self):
        test_meta_data = {'blah': 'fart'}
        rig = nt.AbstractGrouping(meta_data={'blah': 'fart'}, top_node=None, layout_joints=None, parent=None)
        tokens = rig._nomenclate.token_dict.to_json()
        self.assertEquals({k: tokens[k]['label'] for k in tokens if k=='blah'}, test_meta_data)

    @TestBase.delete_created_nodes
    def test_top_node(self):
        test_top_node = nt.Transform.build()
        rig = nt.AbstractGrouping(meta_data=None, top_node=test_top_node, layout_joints=None, parent=None)
        self.assertEquals(rig.root, test_top_node)

    @TestBase.delete_created_nodes
    def test_layout(self):
        layout = 'test'
        rig = nt.AbstractGrouping(meta_data=None, top_node=None, layout_joints=layout, parent=None)
        self.assertEquals(rig.layout_joints, layout)

    @TestBase.delete_created_nodes
    def test_parent_with_top_node(self):
        test_top_node = nt.Transform.build()
        test_parent_node = nt.Transform.build()
        rig = nt.AbstractGrouping(meta_data=None, top_node=test_top_node, layout_joints=None, parent=test_parent_node)
        self.assertEquals(rig.root.getParent(), test_parent_node)

    @TestBase.delete_created_nodes
    def test_parent_without_top_node(self):
        test_parent_node = nt.Transform.build()
        rig = nt.AbstractGrouping(meta_data=None, top_node=None, layout_joints=None, parent=test_parent_node)
        self.assertEquals(rig.root, None)

    @TestBase.delete_created_nodes
    def test_all(self):
        test_parent_node = nt.Transform.build()
        layout = 'test'
        test_top_node = nt.Transform.build()
        test_meta_data = {'blah': 'fart'}
        nt.AbstractGrouping(meta_data=test_meta_data, top_node=test_top_node, layout_joints=layout, parent=test_parent_node)

    @TestBase.delete_created_nodes
    def test_kwargs(self):
        test_flags = {'blah': 'fart'}
        rig = nt.AbstractGrouping(meta_data=None, top_node=None, layout_joints=None, parent=None, **test_flags)
        self.assertDictEqual(rig.build_kwargs, test_flags)



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
