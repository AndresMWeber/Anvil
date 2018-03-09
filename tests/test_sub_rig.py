import anvil.node_types as nt
import anvil.config as cfg
from base_test import TestBase, clean_up_scene


class TestBaseSubRig(TestBase):
    def build_dependencies(cls):
        cls.test_rig = nt.SubRig([])
        cls.test_rig.build()


class TestSubRigBuild(TestBaseSubRig):
    @clean_up_scene
    def test_default(self):
        nt.SubRig().build()

    @clean_up_scene
    def test_all_children_exist(self):
        sub_rig = nt.SubRig(meta_data={'meta': 'data'}, top_node=None, layout=None, parent=None)
        sub_rig.build()
        for node in sub_rig._flat_hierarchy():
            self.assertTrue(node.exists())
            self.assertTrue(isinstance(node, nt.Transform))

    @clean_up_scene
    def test_top_node(self):
        top_node = nt.Transform.build()
        sub_rig = nt.SubRig(meta_data=None, top_node=top_node, layout=None, parent=None)
        sub_rig.build()
        self.assertEquals(sub_rig.root, top_node)

    @clean_up_scene
    def test_layout(self):
        sub_rig = nt.SubRig(meta_data=None, top_node=None, layout_joints='test layout', parent=None)
        sub_rig.build()
        self.assertEquals(sub_rig.layout_joints, 'test layout')

    @clean_up_scene
    def test_parent(self):
        parent = nt.Transform.build()
        sub_rig = nt.SubRig(meta_data=None, top_node=None, layout=None)
        sub_rig.build(parent=parent)
        self.assertEquals(sub_rig.root.getParent(), parent)


class TestSubRigNameTokensIntact(TestBase):
    @clean_up_scene
    def test_register_previously_created_with_name_tokens(self):
        self.sub_rig = nt.SubRig()
        self.sub_rig.build()
        b = nt.Joint.build(name_tokens={'name': 'bob'})
        self.sub_rig.register_node('test', hierarchy_id=b)
        # This test will override the previous name because it now should inherit the new sub rig tokens.
        self.assertDictEqual(b.name_tokens,
                             {cfg.NAME: 'bob', cfg.SUB_RIG_TOKEN: cfg.SUB_RIG_TOKEN, cfg.TYPE: cfg.JOINT_TYPE})
        self.assertDictEqual(b.meta_data, {})

    @clean_up_scene
    def test_register_previously_created_with_name_tokens_overwrite(self):
        self.sub_rig = nt.SubRig()
        self.sub_rig.build()
        b = nt.Joint.build(name_tokens={'name': 'silvia', cfg.SUB_RIG_TOKEN: 'muggle'})
        self.sub_rig.register_node(b, hierarchy_id='test')
        self.assertDictEqual(b.name_tokens,
                             {'name': 'silvia',
                              cfg.SUB_RIG_TOKEN: 'muggle',
                              cfg.TYPE: cfg.JOINT_TYPE})
        self.assertDictEqual(b.meta_data, {})

    @clean_up_scene
    def test_register_previously_created_add_name_tokens(self):
        self.sub_rig = nt.SubRig()
        self.sub_rig.build()
        b = nt.Joint.build(name_tokens={'name': 'silvia'})
        self.sub_rig.register_node(b, hierarchy_id='test')
        self.assertDictEqual(b.name_tokens,
                             {'name': 'silvia',
                              cfg.SUB_RIG_TOKEN: cfg.SUB_RIG_TOKEN,
                              cfg.TYPE: cfg.JOINT_TYPE})

    @clean_up_scene
    def test_build_with_sub_rig_init_name_tokens_and_build_name_tokens(self):
        self.sub_rig = nt.SubRig(name_tokens={'name': 'silvia'})
        self.sub_rig.build()
        self.sub_rig.build_node(nt.Joint, hierarchy_id='test', name_tokens={'blah': 'meta'})
        self.assertDictEqual(self.sub_rig.joint.test.name_tokens,
                             {'name': 'silvia',
                              'blah': 'meta',
                              cfg.SUB_RIG_TOKEN: cfg.SUB_RIG_TOKEN,
                              cfg.TYPE: cfg.JOINT_TYPE})

    @clean_up_scene
    def test_build_with_sub_rig_previous_name_tokens(self):
        self.sub_rig = nt.SubRig()
        self.sub_rig.build(name_tokens={'name': 'silvia'})
        self.sub_rig.build_node(nt.Joint, hierarchy_id='test')
        self.assertDictEqual(self.sub_rig.joint.test.name_tokens,
                             {'name': 'silvia',
                              cfg.SUB_RIG_TOKEN: cfg.SUB_RIG_TOKEN,
                              cfg.TYPE: cfg.JOINT_TYPE})

    @clean_up_scene
    def test_build_with_sub_rig_previous_name_tokens_and_build_name_tokens(self):
        self.sub_rig = nt.SubRig()
        self.sub_rig.build(name_tokens={'name': 'silvia'})
        self.sub_rig.build_node(nt.Joint, hierarchy_id='test', name_tokens={'blah': 'meta'})
        self.assertDictEqual(self.sub_rig.joint.test.name_tokens,
                             {'name': 'silvia',
                              'blah': 'meta',
                              cfg.SUB_RIG_TOKEN: cfg.SUB_RIG_TOKEN,
                              cfg.TYPE: cfg.JOINT_TYPE})

    @clean_up_scene
    def test_build_add_name_tokens(self):
        self.sub_rig = nt.SubRig()
        self.sub_rig.build()
        self.sub_rig.build_node(nt.Joint, hierarchy_id='test', name_tokens={'name': 'silvia'}, meta_data=None)
        self.assertDictEqual(self.sub_rig.joint.test.name_tokens,
                             {cfg.NAME: 'silvia', cfg.SUB_RIG_TOKEN: cfg.SUB_RIG_TOKEN, cfg.TYPE: cfg.JOINT_TYPE})


class TestSubRigMetaDataIntact(TestBase):
    @clean_up_scene
    def test_register_previously_created_with_meta_data(self):
        self.sub_rig = nt.SubRig()
        self.sub_rig.build()
        b = nt.Joint.build(meta_data={'name': 'bob'})
        self.sub_rig.register_node('test', hierarchy_id=b)
        self.assertDictEqual(b.meta_data, {'name': 'bob', 'type': 'joint'})
        self.assertDictEqual(b.name_tokens, {cfg.NAME: 'untitled', cfg.TYPE: cfg.JOINT_TYPE})

    @clean_up_scene
    def test_register_previously_created_with_meta_data_overwrite(self):
        self.sub_rig = nt.SubRig()
        self.sub_rig.build()
        b = nt.Joint.build(meta_data={'name': 'silvia'})
        self.sub_rig.register_node('test', hierarchy_id=b)
        self.assertDictEqual(b.meta_data, {'name': 'silvia', cfg.SUB_RIG_TOKEN: cfg.SUB_RIG_TOKEN})
        self.assertDictEqual(b.name_tokens, {cfg.NAME: 'untitled', cfg.TYPE: cfg.JOINT_TYPE})
