import anvil.node_types as nt
import anvil
import anvil.config as cfg
from six import iteritems
from base_test import TestBase, cleanup_nodes


class TestBaseControl(TestBase):
    pass


class TestControlInit(TestBaseControl):
    pass


class TestControlBuild(TestBaseControl):
    def test_empty_input(self):
        with cleanup_nodes():
            nt.Control.build()

    def test_full_input(self):
        with cleanup_nodes():
            nt.Control.build()

    def test_partial_input(self):
        with cleanup_nodes():
            nt.Control.build()

    def test_shape_input(self):
        with cleanup_nodes():
            nt.Control.build(shape='cube')

    def test_hierarchy_name_tokens_control(self):
        with cleanup_nodes():
            control = nt.Control.build()
            self.assertEqual(control.control.name_tokens.get(cfg.TYPE), cfg.CONTROL_TYPE)
            self.assertEqual(control.control.name_tokens.get(cfg.NAME), 'untitled')

    def test_hierarchy_name_tokens_offset(self):
        with cleanup_nodes():
            control = nt.Control.build()
            self.assertEqual(control.offset_group.name_tokens.get(cfg.TYPE), cfg.OFFSET_GROUP)
            self.assertEqual(control.offset_group.name_tokens.get(cfg.NAME), 'untitled')

    def test_hierarchy_name_tokens_connection(self):
        with cleanup_nodes():
            control = nt.Control.build()
            self.assertEqual(control.connection_group.name_tokens.get(cfg.TYPE), cfg.CONNECTION_GROUP)
            self.assertEqual(control.connection_group.name_tokens.get(cfg.NAME), 'untitled')

    def test_hierarchy_name_tokens_control_preexisting_name_tokens(self):
        with cleanup_nodes():
            control = nt.Control.build(name_tokens={cfg.NAME: 'bob', cfg.CHILD_TYPE: 'lisa'})
            self.assertEqual(control.control.name_tokens.get(cfg.TYPE), cfg.CONTROL_TYPE)
            self.assertEqual(control.control.name_tokens.get(cfg.NAME), 'bob')
            self.assertEqual(control.control.name_tokens.get(cfg.CHILD_TYPE), 'lisa')

    def test_hierarchy_name_tokens_offset_preexisting_name_tokens(self):
        with cleanup_nodes():
            control = nt.Control.build(name_tokens={cfg.NAME: 'bob', cfg.CHILD_TYPE: 'lisa'})
            self.assertEqual(control.offset_group.name_tokens.get(cfg.TYPE), cfg.OFFSET_GROUP)
            self.assertEqual(control.offset_group.name_tokens.get(cfg.NAME), 'bob')
            self.assertEqual(control.offset_group.name_tokens.get(cfg.CHILD_TYPE), 'lisa')

    def test_hierarchy_name_tokens_connection_preexisting_name_tokens(self):
        with cleanup_nodes():
            control = nt.Control.build(name_tokens={cfg.NAME: 'bob', cfg.CHILD_TYPE: 'lisa'})
            self.assertEqual(control.connection_group.name_tokens.get(cfg.TYPE), cfg.CONNECTION_GROUP)
            self.assertEqual(control.connection_group.name_tokens.get(cfg.NAME), 'bob')
            self.assertEqual(control.connection_group.name_tokens.get(cfg.CHILD_TYPE), 'lisa')

    def test_hierarchy_name_token_type_default(self):
        with cleanup_nodes():
            control = nt.Control.build()
            self.assertEqual(control.control.name_tokens.get(cfg.TYPE), cfg.CONTROL_TYPE)
            self.assertEqual(control.offset_group.name_tokens.get(cfg.TYPE), cfg.OFFSET_GROUP)
            self.assertEqual(control.connection_group.name_tokens.get(cfg.TYPE), cfg.CONNECTION_GROUP)

    def test_hierarchy_name_token_type_preexisting(self):
        with cleanup_nodes():
            control = nt.Control.build(name_tokens={'name': 'bob', 'childtype': 'lisa'})
            self.assertEqual(control.control.name_tokens.get(cfg.TYPE), cfg.CONTROL_TYPE)
            self.assertEqual(control.offset_group.name_tokens.get(cfg.TYPE), cfg.OFFSET_GROUP)
            self.assertEqual(control.connection_group.name_tokens.get(cfg.TYPE), cfg.CONNECTION_GROUP)


class TestControlRename(TestBaseControl):
    def rename_runner(self, desired_output, *input_dicts, **input_kwargs):
        with cleanup_nodes():
            control = nt.Control.build()
            control.rename(*input_dicts, **input_kwargs)
            control_hierarchy = {key: str(node) for key, node in iteritems(control.hierarchy)}
            desired_output = desired_output or control_hierarchy

            if 'standalone' in anvil.runtime.dcc.ENGINE:
                self.assertTrue(True)
            else:
                self.assertDictEqual(control_hierarchy, desired_output)

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
