import anvil.node_types as nt
import anvil
from six import iteritems
from base_test import TestBase


class TestBaseControl(TestBase):
    pass


class TestControlInit(TestBaseControl):
    pass


class TestControlBuild(TestBaseControl):
    @TestBase.delete_created_nodes
    def test_empty_input(self):
        nt.Control.build()

    @TestBase.delete_created_nodes
    def test_full_input(self):
        nt.Control.build()

    @TestBase.delete_created_nodes
    def test_partial_input(self):
        nt.Control.build()

    @TestBase.delete_created_nodes
    def test_shape_input(self):
        nt.Control.build(shape='cube')


class TestControlRename(TestBaseControl):
    @TestBase.delete_created_nodes
    def rename_runner(self, desired_output, *input_dicts, **input_kwargs):
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
        _ = 'larry'
        self.rename_runner({'control': '%s_CTR' % _, 'offset_group': '%s_OGP' % _, 'connection_group': '%s_CGP' % _},
                           {'name': 'larry', 'childtype': 'group'})

    def test_dict_input_extra(self):
        _ = 'maybe'
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
        _ = 'johnny'
        self.rename_runner({'control': '%s_CTR' % _, 'offset_group': '%s_OGP' % _, 'connection_group': '%s_CGP' % _},
                           {'name': 'johnny'}, childtype='group', face='bat')

    def test_combined_input_extra_dict_key(self):
        _ = 'april'
        self.rename_runner({'control': '%s_CTR' % _, 'offset_group': '%s_OGP' % _, 'connection_group': '%s_CGP' % _},
                           {'name': 'april', 'face': 'bat'}, childtype='group', face='bat')

    def test_combined_input_overlapping(self):
        _ = 'sarah'
        self.rename_runner({'control': '%s_CTR' % _, 'offset_group': '%s_OGP' % _, 'connection_group': '%s_CGP' % _},
                           {'name': 'oneil'}, name='sarah')

    def test_multi_dict(self):
        _ = 'john_position'
        self.rename_runner({'control': '%s_CTR' % _, 'offset_group': '%s_OGP' % _, 'connection_group': '%s_CGP' % _},
                           {'name': 'john'},
                           {'childtype': 'position'})
