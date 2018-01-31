import anvil.node_types as nt
import anvil.config as cfg
from base_test import TestBase
import unittest


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
        sub_rig = nt.SubRig(meta_data=None, top_node=None, layout_joints='test layout', parent=None)
        sub_rig.build()
        self.assertEquals(sub_rig.layout_joints, 'test layout')

    @TestBase.delete_created_nodes
    def test_parent(self):
        parent = nt.Transform.build()
        sub_rig = nt.SubRig(meta_data=None, top_node=None, layout=None)
        sub_rig.build(parent=parent)
        self.assertEquals(sub_rig.root.getParent(), parent)


class TestSubRigBuildPoleVector(TestBase):
    def build_dependencies(cls):
        cls.sub_rig = nt.SubRig()
        cls.sub_rig.build()
        b = nt.Joint.build()
        c = nt.Joint.build()
        d = nt.Joint.build()
        c.translate_node([0, 2.5, 0])
        d.translate_node([0, 5, 0])
        cls.joint_chain = nt.HierarchyChain(b, d)
        cls.handle, cls.effector = cls.joint_chain.build_ik()

    @TestBase.delete_created_nodes
    def test_build(self):
        self.sub_rig.build_pole_vector_control(self.joint_chain, self.handle)


class TestSubRigNameTokensIntact(TestBase):
    @TestBase.delete_created_nodes
    def test_register_previously_created_with_name_tokens(self):
        self.sub_rig = nt.SubRig()
        self.sub_rig.build()
        b = nt.Joint.build(name_tokens={'name': 'bob'})
        self.sub_rig.register_node('test', b, name_tokens=None)
        # This test will override the previous name because it now should inherit the new sub rig tokens.
        self.assertDictEqual(b.name_tokens,
                             {cfg.NAME: 'untitled', cfg.SUB_RIG_TOKEN: cfg.SUB_RIG_TOKEN, cfg.TYPE: cfg.JOINT_TYPE})
        self.assertDictEqual(b.meta_data, {})

    @TestBase.delete_created_nodes
    def test_register_previously_created_with_name_tokens_overwrite(self):
        self.sub_rig = nt.SubRig()
        self.sub_rig.build()
        b = nt.Joint.build(name_tokens={'name': 'bob'})
        self.sub_rig.register_node('test', b, name_tokens={'name': 'silvia', cfg.SUB_RIG_TOKEN: 'muggle'})
        self.assertDictEqual(b.name_tokens,
                             {'name': 'silvia',
                              cfg.SUB_RIG_TOKEN: 'muggle',
                              cfg.TYPE: cfg.JOINT_TYPE})
        self.assertDictEqual(b.meta_data, {})

    @TestBase.delete_created_nodes
    def test_register_previously_created_add_name_tokens(self):
        self.sub_rig = nt.SubRig()
        self.sub_rig.build()
        b = nt.Joint.build()
        self.sub_rig.register_node('test', b, name_tokens={'name': 'silvia'})
        self.assertDictEqual(b.name_tokens,
                             {'name': 'silvia',
                              cfg.SUB_RIG_TOKEN: cfg.SUB_RIG_TOKEN,
                              cfg.TYPE: cfg.JOINT_TYPE})

    @TestBase.delete_created_nodes
    def test_build_with_sub_rig_init_name_tokens_and_build_name_tokens(self):
        self.sub_rig = nt.SubRig(name_tokens={'name': 'silvia'})
        self.sub_rig.build()
        self.sub_rig.build_node(nt.Joint, 'test', name_tokens={'blah': 'meta'})
        self.assertDictEqual(self.sub_rig.test.name_tokens,
                             {'name': 'silvia',
                              'blah': 'meta',
                              cfg.SUB_RIG_TOKEN: cfg.SUB_RIG_TOKEN,
                              cfg.TYPE: cfg.JOINT_TYPE})

    @TestBase.delete_created_nodes
    def test_build_with_sub_rig_previous_name_tokens(self):
        self.sub_rig = nt.SubRig()
        self.sub_rig.build(name_tokens={'name': 'silvia'})
        self.sub_rig.build_node(nt.Joint, 'test')
        self.assertDictEqual(self.sub_rig.test.name_tokens,
                             {'name': 'silvia',
                              cfg.SUB_RIG_TOKEN: cfg.SUB_RIG_TOKEN,
                              cfg.TYPE: cfg.JOINT_TYPE})

    @TestBase.delete_created_nodes
    def test_build_with_sub_rig_previous_name_tokens_and_build_name_tokens(self):
        self.sub_rig = nt.SubRig()
        self.sub_rig.build(name_tokens={'name': 'silvia'})
        self.sub_rig.build_node(nt.Joint, 'test', name_tokens={'blah': 'meta'})
        self.assertDictEqual(self.sub_rig.test.name_tokens,
                             {'name': 'silvia',
                              'blah': 'meta',
                              cfg.SUB_RIG_TOKEN: cfg.SUB_RIG_TOKEN,
                              cfg.TYPE: cfg.JOINT_TYPE})

    @TestBase.delete_created_nodes
    def test_build_add_name_tokens(self):
        self.sub_rig = nt.SubRig()
        self.sub_rig.build()
        self.sub_rig.build_node(nt.Joint, 'test', name_tokens={'name': 'silvia'}, meta_data=None)
        print(self.sub_rig.test.name_tokens)
        self.assertDictEqual(self.sub_rig.test.name_tokens,
                             {cfg.NAME: 'untitled', cfg.SUB_RIG_TOKEN: cfg.SUB_RIG_TOKEN, cfg.TYPE: cfg.JOINT_TYPE})


class TestSubRigMetaDataIntact(TestBase):
    @TestBase.delete_created_nodes
    def test_register_previously_created_with_meta_data(self):
        self.sub_rig = nt.SubRig()
        self.sub_rig.build()
        b = nt.Joint.build(meta_data={'name': 'bob'})
        self.sub_rig.register_node('test', b, meta_data=None)
        self.assertDictEqual(b.meta_data, {'name': 'bob', 'type': 'joint'})
        self.assertDictEqual(b.name_tokens, {cfg.NAME: 'untitled', cfg.TYPE: cfg.JOINT_TYPE})

    @TestBase.delete_created_nodes
    def test_register_previously_created_with_meta_data_overwrite(self):
        self.sub_rig = nt.SubRig()
        self.sub_rig.build()
        b = nt.Joint.build(meta_data={'name': 'bob'})
        self.sub_rig.register_node('test', b, meta_data={'name': 'silvia'})
        self.assertDictEqual(b.meta_data, {'name': 'silvia', cfg.SUB_RIG_TOKEN: cfg.SUB_RIG_TOKEN})
        self.assertDictEqual(b.name_tokens, {cfg.NAME: 'untitled', cfg.TYPE: cfg.JOINT_TYPE})
