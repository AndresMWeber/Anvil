import anvil.node_types as nt

from base_test import TestBase


class TestBaseSubRig(TestBase):
    def build_dependencies(cls):
        cls.test_rig = nt.SubRig([])
        cls.test_rig.build()


class TestSubRigBuild(TestBaseSubRig):
    @TestBase.delete_created_nodes
    def test_default(self):
        nt.SubRig().build()

    @TestBase.delete_created_nodes
    def test_meta_data(self):
        sub_rig = nt.SubRig(meta_data={'meta': 'data'}, top_node=None, layout=None, parent=None)
        sub_rig.build()
        for node in list(sub_rig.hierarchy):
            node = sub_rig.hierarchy[node]
            self.assertTrue(node.exists())
            self.assertTrue(isinstance(node, nt.Transform))

    @TestBase.delete_created_nodes
    def test_top_node(self):
        top_node = nt.Transform.build()
        sub_rig = nt.SubRig(meta_data=None, top_node=top_node, layout=None, parent=None)
        sub_rig.build()
        self.assertEquals(sub_rig.root, top_node)

    @TestBase.delete_created_nodes
    def test_layout(self):
        sub_rig = nt.SubRig(meta_data=None, top_node=None, layout='test layout', parent=None)
        sub_rig.build()
        self.assertEquals(sub_rig.layout, 'test layout')

    @TestBase.delete_created_nodes
    def test_parent(self):
        parent = nt.Transform.build()
        sub_rig = nt.SubRig(meta_data=None, top_node=None, layout=None)
        sub_rig.build(parent=parent)
        self.assertEquals(sub_rig.root.getParent(), parent)
