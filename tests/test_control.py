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
        self.rename_runner({'control': 'larry_CTR', 'offset_group': 'larry_OGP', 'connection_group': 'larry_CGP'},
                           {'name': 'larry', 't ype': 'group'})

    def test_dict_input_extra(self):
        self.rename_runner({'control': 'maybe_CTR', 'offset_group': 'maybe_OGP', 'connection_group': 'maybe_CGP'},
                           {'name': 'maybe', 'type': 'group', 'face': 'pretty'})

    def test_dict_input_only_extra(self):
        self.rename_runner({'control': 'CTR', 'offset_group': 'OGP', 'connection_group': 'CGP'},
                           {'blah': 'face'})

    def test_kwargs_input(self):
        self.rename_runner({'control': 'test_joint_CTR',
                            'offset_group': 'test_joint_OGP',
                            'connection_group': 'test_joint_CGP'},
                           name='test', childtype='joint')

    def test_kwargs_input_extra(self):
        self.rename_runner({'control': 'test_mountain_CTR',
                            'offset_group': 'test_mountain_OGP',
                            'connection_group': 'test_mountain_CGP'},
                           name='test', childtype='mountain', rotten='tomato')

    def test_kwargs_input_only_extra(self):
        self.rename_runner(None, fame='test', mild='hier', rotten='tomato')

    def test_combined_input(self):
        self.rename_runner({'control': 'john_CTR', 'offset_group': 'john_OGP', 'connection_group': 'john_CGP'},
                           {'name': 'john'}, type='group')

    def test_combined_input_extra_kwarg(self):
        self.rename_runner({'control': 'johnny_CTR', 'offset_group': 'johnny_OGP', 'connection_group': 'johnny_CGP'},
                           {'name': 'johnny'}, type='group', face='bat')

    def test_combined_input_extra_dict_key(self):
        self.rename_runner({'control': 'april_CTR', 'offset_group': 'april_OGP', 'connection_group': 'april_CGP'},
                           {'name': 'april', 'face': 'bat'}, type='group', face='bat')

    def test_combined_input_overlapping(self):
        self.rename_runner({'control': 'sarah_CTR', 'offset_group': 'sarah_OGP', 'connection_group': 'sarah_CGP'},
                           {'name': 'oneil'}, name='sarah')

    def test_multi_dict(self):
        self.rename_runner({'control': 'john_position_CTR',
                            'offset_group': 'john_position_OGP',
                            'connection_group': 'john_position_CGP'},
                           {'name': 'john'},
                           {'childtype': 'position'})
