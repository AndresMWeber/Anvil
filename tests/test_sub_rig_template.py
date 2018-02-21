from anvil.sub_rig_templates import base
from base_test import TestBase
import anvil.node_types as nt
import anvil.config as cfg

class TestBaseSubRig(TestBase):
    pass


class TestSubRigTemplateGetShapeList(TestBaseSubRig):
    def test_input_shape_list(self):
        input = ['f', 'g', 'h', 'i']
        self.assertEqual(base.SubRigTemplate.get_shape_list(4, input), input)

    def test_short_shape_list(self):
        input = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.assertEqual(base.SubRigTemplate.get_shape_list(14, input),
                         ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] + ['h'] * 6)

    def test_short_shape_list_by_one(self):
        input = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.assertEqual(base.SubRigTemplate.get_shape_list(9, input),
                         ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'h'])

    def test_over_length_shape_list(self):
        input = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.assertEqual(base.SubRigTemplate.get_shape_list(5, input), input)

    def test_kwarg_shape_input(self):
        self.assertEqual(base.SubRigTemplate.get_shape_list(6, shape='pyramid'), ['pyramid'] * 6)

    def test_no_shape_input(self):
        self.assertEqual(base.SubRigTemplate.get_shape_list(10), [base.SubRigTemplate.DEFAULT_FK_SHAPE] * 10)


class TestSubRigTemplateBuildIk(TestBaseSubRig):
    def build_dependencies(cls):
        cls.sub_rig = base.SubRigTemplate()
        cls.sub_rig.build()
        b = nt.Joint.build()
        c = nt.Joint.build()
        d = nt.Joint.build()
        c.translate_node([0, 2.5, 0])
        d.translate_node([0, 5, 0])
        cls.joint_chain = nt.LinearHierarchyNodeSet(b, d)
        result = cls.sub_rig.build_ik(cls.joint_chain)
        cls.handle, cls.effector = result[cfg.NODE_TYPE]

    @TestBase.delete_created_nodes
    def test_build(self):
        self.sub_rig.build_pole_vector_control(self.joint_chain, self.handle)
