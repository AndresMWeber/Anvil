import anvil.node_types as nt
import anvil
import anvil.config as cfg
from six import iteritems
from base_test import TestBase, clean_up_scene


class TestBaseControl(TestBase):
    pass


class TestControlInit(TestBaseControl):
    @clean_up_scene
    def test_empty_input(self):
        nt.Control()


class TestControlBuild(TestBaseControl):
    @clean_up_scene
    def test_empty_input(self):
        nt.Control.build()

    @clean_up_scene
    def test_full_input(self):
        nt.Control.build()

    @clean_up_scene
    def test_partial_input(self):
        nt.Control.build()

    @clean_up_scene
    def test_shape_input(self):
        nt.Control.build(shape='cube')

    @clean_up_scene
    def test_hierarchy_meta_data_control(self):
        control = nt.Control.build()
        self.assertEqual(control.controller.meta_data.get(cfg.TYPE), cfg.CONTROL_TYPE)
        self.assertEqual(control.controller.meta_data.get(cfg.NAME), 'untitled')

    @clean_up_scene
    def test_hierarchy_meta_data_offset(self):
        control = nt.Control.build()
        self.assertEqual(control.offset_group.meta_data.get(cfg.TYPE), cfg.OFFSET_GROUP)
        self.assertEqual(control.offset_group.meta_data.get(cfg.NAME), 'untitled')

    @clean_up_scene
    def test_hierarchy_meta_data_connection(self):
        control = nt.Control.build()
        self.assertEqual(control.connection_group.meta_data.get(cfg.TYPE), cfg.CONNECTION_GROUP)
        self.assertEqual(control.connection_group.meta_data.get(cfg.NAME), 'untitled')

    @clean_up_scene
    def test_hierarchy_meta_data_control_preexisting_meta_data(self):
        control = nt.Control.build(meta_data={cfg.NAME: 'bob', cfg.CHILD_TYPE: 'lisa'})
        self.assertEqual(control.controller.meta_data.get(cfg.TYPE), cfg.CONTROL_TYPE)
        self.assertEqual(control.controller.meta_data.get(cfg.NAME), 'bob')
        self.assertEqual(control.controller.meta_data.get(cfg.CHILD_TYPE), 'lisa')

    @clean_up_scene
    def test_hierarchy_meta_data_offset_preexisting_meta_data(self):
        control = nt.Control.build(meta_data={cfg.NAME: 'bob', cfg.CHILD_TYPE: 'lisa'})
        self.assertEqual(control.offset_group.meta_data.get(cfg.TYPE), cfg.OFFSET_GROUP)
        self.assertEqual(control.offset_group.meta_data.get(cfg.NAME), 'bob')
        self.assertEqual(control.offset_group.meta_data.get(cfg.CHILD_TYPE), 'lisa')

    @clean_up_scene
    def test_hierarchy_meta_data_connection_preexisting_meta_data(self):
        control = nt.Control.build(meta_data={cfg.NAME: 'bob', cfg.CHILD_TYPE: 'lisa'})
        self.assertEqual(control.connection_group.meta_data.get(cfg.TYPE), cfg.CONNECTION_GROUP)
        self.assertEqual(control.connection_group.meta_data.get(cfg.NAME), 'bob')
        self.assertEqual(control.connection_group.meta_data.get(cfg.CHILD_TYPE), 'lisa')

    @clean_up_scene
    def test_hierarchy_name_token_type_default(self):
        control = nt.Control.build()
        self.assertEqual(control.controller.meta_data.get(cfg.TYPE), cfg.CONTROL_TYPE)
        self.assertEqual(control.offset_group.meta_data.get(cfg.TYPE), cfg.OFFSET_GROUP)
        self.assertEqual(control.connection_group.meta_data.get(cfg.TYPE), cfg.CONNECTION_GROUP)

    @clean_up_scene
    def test_hierarchy_name_token_type_preexisting(self):
        control = nt.Control.build(meta_data={'name': 'bob', 'childtype': 'lisa'})
        self.assertEqual(control.controller.meta_data.get(cfg.TYPE), cfg.CONTROL_TYPE)
        self.assertEqual(control.offset_group.meta_data.get(cfg.TYPE), cfg.OFFSET_GROUP)
        self.assertEqual(control.connection_group.meta_data.get(cfg.TYPE), cfg.CONNECTION_GROUP)


class TestControlRename(TestBaseControl):
    @clean_up_scene
    def rename_runner(self, desired_output, *input_dicts, **input_kwargs):
        control = nt.Control.build()
        control.rename(*input_dicts, **input_kwargs)

        if 'standalone' not in anvil.runtime.dcc.ENGINE and desired_output:
            self.assertDictEqual(control.hierarchy.node, desired_output)

    def test_empty_input(self):
        self.rename_runner(None)

    def test_dict_input(self):
        _ = 'larry_group'
        self.rename_runner({'control': '%s_CTR' % _, 'offset_group': '%s_OGP' % _, 'connection_group': '%s_CGP' % _},
                           {'name': 'larry', 'childtype': 'group'})

    def test_dict_input_extra(self):
        _ = 'maybe_group'
        self.rename_runner({'control': '%s_CTR' % _, 'offset_group': '%s_OGP' % _, 'connection_group': '%s_CGP' % _},
                           {'name': 'maybe', 'childtype': 'group', 'face': 'pretty'})

    def test_dict_input_only_extra(self):
        _ = 'untitled'
        self.rename_runner({'control': '%s_CTR' % _, 'offset_group': '%s_OGP' % _, 'connection_group': '%s_CGP' % _},
                           {'blah': 'face'})

    def test_kwargs_input(self):
        _ = 'test_joint'
        self.rename_runner({'control': '%s_CTR' % _, 'offset_group': '%s_OGP' % _, 'connection_group': '%s_CGP' % _},
                           name='test', childtype='joint')

    def test_kwargs_input_extra(self):
        _ = 'test_mountain'
        self.rename_runner({'control': '%s_CTR' % _, 'offset_group': '%s_OGP' % _, 'connection_group': '%s_CGP' % _},
                           name='test', childtype='mountain', rotten='tomato')

    def test_kwargs_input_only_extra(self):
        self.rename_runner(None, fame='test', mild='hier', rotten='tomato')

    def test_combined_input(self):
        _ = 'john_blah'
        self.rename_runner({'control': '%s_CTR' % _, 'offset_group': '%s_OGP' % _, 'connection_group': '%s_CGP' % _},
                           {'name': 'john'}, childtype='blah')

    def test_combined_input_extra_kwarg(self):
        _ = 'johnny_group'
        self.rename_runner({'control': '%s_CTR' % _, 'offset_group': '%s_OGP' % _, 'connection_group': '%s_CGP' % _},
                           {'name': 'johnny'}, childtype='group', face='bat')

    def test_combined_input_extra_dict_key(self):
        _ = 'april_child'
        self.rename_runner({'control': '%s_CTR' % _, 'offset_group': '%s_OGP' % _, 'connection_group': '%s_CGP' % _},
                           {'name': 'april', 'face': 'bat'}, childtype='child', face='bat')

    def test_combined_input_overlapping(self):
        _ = 'sarah'
        self.rename_runner({'control': '%s_CTR' % _, 'offset_group': '%s_OGP' % _, 'connection_group': '%s_CGP' % _},
                           {'name': 'oneil'}, name='sarah')

    def test_multi_dict(self):
        _ = 'john_position'
        self.rename_runner({'control': '%s_CTR' % _, 'offset_group': '%s_OGP' % _, 'connection_group': '%s_CGP' % _},
                           {'name': 'john'},
                           {'childtype': 'position'})
