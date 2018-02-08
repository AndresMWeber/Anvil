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
    def from_template_file(cls, template_file, skip_import=False, **kwargs):
        if not skip_import:
            cls.import_template_files(template_file)
        rig_instance = cls.TEMPLATE_CLASS(layout_joints=[nt.Transform(n) for n in ['foot', 'ball', 'toe']],
                                          heel=nt.Transform('heel'))
        rig_instance.build(**kwargs)
        return rig_instance

    def test_build_no_kwargs(self):
        with cleanup_nodes():
            self.from_template_file(self.FOOT)

    def test_build_with_parent(self):
        with cleanup_nodes():
            parent = nt.Transform.build(name='test')
            rig_instance = self.from_template_file(self.FOOT, parent=parent)
            self.assertEqual(str(rig_instance.root.get_parent()), str(parent))

    def test_build_with_leg_ik(self):
        with cleanup_nodes():
            parent = nt.Transform.build(name='test')
            self.import_template_files(self.FOOT_WITH_LEG)
            foot_ball_result = self.TEMPLATE_CLASS.build_ik(
                nt.HierarchyChain('hip', 'foot', node_filter=cfg.JOINT_TYPE),
                solver=cfg.IK_RP_SOLVER)
            handle, effector = foot_ball_result[cfg.NODE_TYPE]
            rig_instance = self.from_template_file(None, leg_ik=handle, skip_import=True, parent=parent)
            self.assertEqual(str(rig_instance.root.get_parent()), str(parent))


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
