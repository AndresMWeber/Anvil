from anvil.sub_rig_templates import base_sub_rig_template
from base_test import TestBase, clean_up_scene
import anvil.node_types as nt
import anvil.config as cfg


class TestBaseSubRig(TestBase):
    instance = None


class TestSubRigTemplateBuildIk(TestBaseSubRig):
    def setUp(self):
        if self.instance is None:
            self.instance = base_sub_rig_template.SubRigTemplate()
            self.instance.build()
            b = nt.Joint.build()
            c = nt.Joint.build()
            d = nt.Joint.build()
            c.translate_node([0, 2.5, 0])
            d.translate_node([0, 5, 0])
            self.joint_chain = nt.NodeChain(b, d)
            result = self.instance.build_ik(self.joint_chain)
            self.handle, self.effector = result[cfg.NODE_TYPE][cfg.DEFAULT]

    def test_build_pole_vector_control(self):
        self.instance.build_pole_vector_control(self.joint_chain, self.handle)


class TestSubRigNameTokens(TestBaseSubRig):
    input_tokens = {'name': 'bob', 'var': 1, 'purpose': 'holy', 'type': 'group'}

    def setUp(self):
        if self.instance is None:
            self.instance = base_sub_rig_template.SubRigTemplate(meta_data=self.input_tokens)
            self.instance.build()

    def test_default_meta_data_exist(self):
        self.assertEqual(self.instance.meta_data, self.input_tokens)

    def test_build_keeps_meta_data_passed_as_dict(self):
        node = self.instance.build_node(nt.Transform, meta_data=self.input_tokens, skip_report=True, skip_register=True)
        self.assertEqual(node.meta_data, self.input_tokens)

    def test_build_keeps_meta_data_passed_as_splat(self):
        node = self.instance.build_node(nt.Transform, skip_report=True, skip_register=True, **self.input_tokens)
        self.assertEqual(node.meta_data, self.input_tokens)


    def test_build_keeps_meta_data_assigned_later(self):
        node = self.instance.build_node(nt.Transform, skip_report=True, skip_register=True, **self.input_tokens)
        self.assertEqual(node.meta_data, self.input_tokens)

    def test_build_keeps_meta_data_without_adding(self):
        node = self.instance.build_node(nt.Transform, skip_report=True, skip_register=True)
        self.assertEqual(node.meta_data, self.input_tokens)
