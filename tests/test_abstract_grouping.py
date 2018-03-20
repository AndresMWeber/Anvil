import anvil.node_types as nt
import anvil.config as cfg
from base_test import TestBase, clean_up_scene, sanitize_scene


class TestBaseAbstractGrouping(TestBase):
    def build_dependencies(cls):
        pass


class TestAbstractGroupingInit(TestBaseAbstractGrouping):
    @clean_up_scene
    def test_meta_data(self):
        test_meta_data = {'blah': 'fart'}
        rig = nt.AbstractGrouping(meta_data=test_meta_data, top_node=None, layout_joints=None, parent=None)
        test_meta_data.update(nt.AbstractGrouping.BUILT_IN_META_DATA)
        self.assertEqual(rig.meta_data, test_meta_data)

    @clean_up_scene
    def test_meta_data_nomenclate(self):
        test_meta_data = {'blah': 'fart'}
        rig = nt.AbstractGrouping(meta_data={'blah': 'fart'}, top_node=None, layout_joints=None, parent=None)
        tokens = rig._nomenclate.token_dict.to_json()
        self.assertEquals({k: tokens[k]['label'] for k in tokens if k == 'blah'}, test_meta_data)

    @clean_up_scene
    def test_top_node(self):
        test_top_node = nt.Transform.build()
        rig = nt.AbstractGrouping(meta_data=None, top_node=test_top_node, layout_joints=None, parent=None)
        self.assertEquals(rig.root, test_top_node)

    @clean_up_scene
    def test_layout(self):
        layout = 'test'
        rig = nt.AbstractGrouping(meta_data=None, top_node=None, layout_joints=layout, parent=None)
        self.assertEquals(rig.layout_joints, layout)

    @clean_up_scene
    def test_parent_with_top_node(self):
        test_top_node = nt.Transform.build()
        test_parent_node = nt.Transform.build()
        rig = nt.AbstractGrouping(meta_data=None, top_node=test_top_node, layout_joints=None, parent=test_parent_node)
        self.assertEquals(rig.root.getParent(), test_parent_node)

    @clean_up_scene
    def test_parent_without_top_node(self):
        test_parent_node = nt.Transform.build()
        rig = nt.AbstractGrouping(meta_data=None, top_node=None, layout_joints=None, parent=test_parent_node)
        self.assertEquals(rig.root, None)

    @clean_up_scene
    def test_all(self):
        test_parent_node = nt.Transform.build()
        layout = 'test'
        test_top_node = nt.Transform.build()
        test_meta_data = {'blah': 'fart'}
        nt.AbstractGrouping(meta_data=test_meta_data, top_node=test_top_node, layout_joints=layout,
                            parent=test_parent_node)

    @clean_up_scene
    def test_kwargs(self):
        test_flags = {'blah': 'fart'}
        rig = nt.AbstractGrouping(meta_data=None, top_node=None, layout_joints=None, parent=None, **test_flags)
        self.assertEqual(rig.build_kwargs, test_flags)


class TestAbstractGroupingParent(TestBaseAbstractGrouping):
    @clean_up_scene
    def test_empty_string(self):
        test_xform = nt.Transform.build()
        rig = nt.AbstractGrouping(top_node=test_xform)
        was_parented = rig.parent('')
        self.assertFalse(was_parented)

    @clean_up_scene
    def test_exists_but_no_top_node(self):
        test_xform = nt.Transform.build()
        rig = nt.AbstractGrouping()
        was_parented = rig.parent(test_xform)
        self.assertFalse(was_parented)

    @clean_up_scene
    def test_both_exist(self):
        test_xform = nt.Transform.build()
        test_top_node = nt.Transform.build()
        rig = nt.AbstractGrouping(top_node=test_top_node)
        was_parented = rig.parent(test_xform)
        self.assertTrue(was_parented)


class TestAbstractGroupingBuildNode(TestBaseAbstractGrouping):
    @clean_up_scene
    def test_built_node_registered_autosorted(self):
        grouping = nt.AbstractGrouping()
        report = grouping.build_node(nt.Transform)
        self.assertEqual(report[cfg.NODE_TYPE][cfg.DEFAULT], grouping.hierarchy.node.default)

    def test_built_node_registered_control(self):
        grouping = nt.AbstractGrouping()
        report = grouping.build_node(nt.Control)
        self.assertEqual(report[cfg.CONTROL_TYPE][cfg.DEFAULT], grouping.hierarchy.control.default)

    def test_built_node_registered_joint(self):
        grouping = nt.AbstractGrouping()
        report = grouping.build_node(nt.Joint)
        self.assertEqual(report[cfg.JOINT_TYPE][cfg.DEFAULT], grouping.hierarchy.joint.default)


class TestAbstractGroupingRegisterNode(TestBaseAbstractGrouping):
    @classmethod
    def setUpClass(cls):
        cls.grouping = nt.AbstractGrouping()
        super(TestAbstractGroupingRegisterNode, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        sanitize_scene()
        super(TestAbstractGroupingRegisterNode, cls).tearDownClass()

    def test_register_joint(self):
        node = nt.Joint.build()
        report = self.grouping.register_node(node)
        self.assertEqual(report[cfg.JOINT_TYPE][cfg.DEFAULT], self.grouping.hierarchy.joint.default)
        self.assertEqual(node, self.grouping.hierarchy.joint.default[-1])

    def test_register_control(self):
        node = nt.Control.build()
        report = self.grouping.register_node(node)
        self.assertEqual(report[cfg.CONTROL_TYPE][cfg.DEFAULT], self.grouping.hierarchy.control.default)
        self.assertEqual(node, self.grouping.hierarchy.control.default[-1])

    def test_register_transform(self):
        node = nt.Transform.build()
        report = self.grouping.register_node(node)
        self.assertEqual(node, self.grouping.hierarchy.node.default[-1])
        self.assertEqual(report[cfg.NODE_TYPE][cfg.DEFAULT][-1], self.grouping.hierarchy.node.default[-1])

    def test_register_non_linear_hierarchy_node_set_of_transforms(self):
        node = nt.NodeSet([nt.Transform.build() for _ in range(10)])
        report = self.grouping.register_node(node)

        print(node, self.grouping.hierarchy)
        print('original report:')
        print(report)
        print(report[cfg.NODE_TYPE][cfg.DEFAULT])
        print('hierarchy...')
        print(self.grouping.hierarchy.node)
        print(self.grouping.hierarchy.node.default)
        print(self.grouping.hierarchy.node['default'])

        self.assertTrue(all(a in self.grouping.hierarchy.node.default for a in report[cfg.NODE_TYPE][cfg.DEFAULT]))
        self.assertEqual(node, self.grouping.hierarchy.node.default[-1])

    def test_register_non_linear_hierarchy_node_set_of_controls(self):
        node = nt.NodeSet([nt.Control.build() for _ in range(10)])
        report = self.grouping.register_node(node)
        print(node, self.grouping.hierarchy)
        print('original report:')
        print(report)
        print(report[cfg.NODE_TYPE][cfg.DEFAULT])
        print('hierarchy...')
        print(self.grouping.hierarchy.node)
        print(self.grouping.hierarchy.node.default)

        self.assertTrue(all(a in self.grouping.hierarchy.control.default for a in report[cfg.CONTROL_TYPE][cfg.DEFAULT]))
        self.assertEqual(node, self.grouping.hierarchy.control.default[-1])

    def test_register_non_linear_hierarchy_node_set_of_joints(self):
        node = nt.NodeSet([nt.Joint.build() for _ in range(10)])
        report = self.grouping.register_node(node)
        print(node, self.grouping.hierarchy)
        print('original report:')
        print(report)
        print(report[cfg.JOINT_TYPE][cfg.DEFAULT])
        print('hierarchy...')
        from pprint import pprint
        pprint(self.grouping.hierarchy)
        print(self.grouping.hierarchy.joint)
        print(self.grouping.hierarchy.joint.default)

        self.assertTrue(all(a in self.grouping.hierarchy.joint.default for a in report[cfg.JOINT_TYPE][cfg.DEFAULT]))
        self.assertEqual(node, self.grouping.hierarchy.joint.default[-1])

    def test_register_linear_hierarchy_node_set(self):
        node = nt.NodeChain([nt.Joint.build() for _ in range(10)])
        report = self.grouping.register_node(node)
        print(node, self.grouping.hierarchy)
        print('original report:')
        print(report)
        print(report[cfg.JOINT_TYPE][cfg.DEFAULT])
        print('hierarchy...')
        print(self.grouping.hierarchy.joint)
        print(self.grouping.hierarchy.joint.default)

        self.assertTrue(all(a in self.grouping.hierarchy.joint.default for a in report[cfg.JOINT_TYPE][cfg.DEFAULT]))
        self.assertEqual(node, self.grouping.hierarchy.joint.default[-1])
