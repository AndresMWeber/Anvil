from six import iteritems
import anvil.node_types as nt
from anvil.sub_rig_templates import BipedFoot
from tests.base_test import TestBase, cleanup_nodes
import anvil.config as cfg


class TestBaseTemplateRigs(TestBase):
    name_tokens = {'name': 'eye', 'purpose': 'mvp'}
    test_rig = None
    TEMPLATE_CLASS = BipedFoot


class TestBuildBipedFoot(TestBaseTemplateRigs):

    @classmethod
    def from_template_file(cls, template_file, pre_build_hook=None, post_build_hook=None, **kwargs):
        default_return_func = lambda: {}
        pre_build_hook = pre_build_hook or default_return_func
        post_build_hook = post_build_hook or default_return_func

        cls.import_template_files(template_file)

        kwargs.update(pre_build_hook())

        rig_instance = cls.TEMPLATE_CLASS(layout_joints=map(nt.Transform, ['foot', 'ball', 'toe']),
                                          heel=nt.Transform('heel'),
                                          outsole='outsole',
                                          insole='insole')
        rig_instance.build(**kwargs)

        post_build_hook()

        return rig_instance

    def test_build_no_kwargs(self):
        with cleanup_nodes():
            self.from_template_file(self.FOOT)

    def test_build_with_parent(self):
        with cleanup_nodes():
            parent = nt.Transform.build(name='test')
            rig_instance = self.from_template_file(self.FOOT, parent=parent)
            self.assertEqual(str(rig_instance.root.get_parent()), str(parent))

    def test_build_with_leg_ik_and_soles(self):
        with cleanup_nodes():
            rig_instance = self.from_template_file(self.FOOT_WITH_LEG_AND_SOLES, insole='insole', outsole='outsole',
                                                   pre_build_hook=self.build_leg_ik)

            #self.assertEqual([round(p, 5) for p in control.offset_group.get_world_position()],
            #                 [round(p, 5) for p in joint.get_world_position()])

    def test_build_with_leg_ik(self):
        with cleanup_nodes():
            parent = nt.Transform.build(name='test')
            rig_instance = self.from_template_file(self.FOOT_WITH_LEG, parent=parent, pre_build_hook=self.build_leg_ik)
            self.assertEqual(str(rig_instance.root.get_parent()), str(parent))

    @staticmethod
    def build_leg_ik():
        foot_ball_result = TestBuildBipedFoot.TEMPLATE_CLASS.build_ik(nt.HierarchyChain('hip', 'foot',
                                                                                        node_filter=cfg.JOINT_TYPE),
                                                                      solver=cfg.IK_RP_SOLVER)
        return {'leg_ik': foot_ball_result[cfg.NODE_TYPE][0]}


class TestBuildBipedFootHierarchy(TestBaseTemplateRigs):
    @classmethod
    def setUpClass(cls):
        cls.rig = cls.from_template_file(cls.FOOT)

    def test_number_of_controls(self):
        self.assertEqual(
            len(list([node for key, node in iteritems(self.rig.hierarchy) if isinstance(node, nt.Control)])), 4)

    def test_control_positions_match(self):
        components = [self.TEMPLATE_CLASS.TOE_TOKEN,
                      self.TEMPLATE_CLASS.BALL_TOKEN,
                      self.TEMPLATE_CLASS.ANKLE_TOKEN,
                      self.TEMPLATE_CLASS.HEEL_TOKEN]
        for component in components:
            control = getattr(self.rig, 'control_%s' % component)
            joint = getattr(self.rig, component)
            self.assertEqual([round(p, 5) for p in control.offset_group.get_world_position()],
                             [round(p, 5) for p in joint.get_world_position()])
