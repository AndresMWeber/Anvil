from six import iteritems
import anvil.node_types as nt
from anvil.sub_rig_templates import BipedFoot
import base_test


class TestBaseTemplateRigs(base_test.TestBase):
    name_tokens = {'name': 'eye', 'purpose': 'mvp'}
    test_rig = None
    TEMPLATE_CLASS = None


class TestBuildBipedFoot(TestBaseTemplateRigs):
    @classmethod
    def from_template_file(cls, template_file, **kwargs):
        cls.import_template_files(template_file)
        rig_instance = BipedFoot(layout_joints=[nt.Transform(n) for n in ['foot', 'ball', 'toe', 'end']],
                                 heel=nt.Transform('heel'))
        rig_instance.build(**kwargs)
        return rig_instance

    def test_build_no_kwargs(self):
        with base_test.cleanup_nodes():
            self.from_template_file(self.FOOT)

    def test_build_with_parent(self):
        with base_test.cleanup_nodes():
            parent = nt.Transform.build(name='test')
            rig_instance = self.from_template_file(self.FOOT, parent=parent)
            self.assertEqual(str(rig_instance.root.get_parent()), str(parent))

    def test_number_of_controls(self):
        with base_test.cleanup_nodes():
            parent = nt.Transform.build(name='test')
            rig_instance = self.from_template_file(self.FOOT, parent=parent)
            self.assertEqual(
                len(list([node for key, node in iteritems(rig_instance.hierarchy) if isinstance(node, nt.Control)])), 4)

    def test_control_positions_match(self):
        with base_test.cleanup_nodes():
            parent = nt.Transform.build(name='test')
            rig_instance = self.from_template_file(self.FOOT, parent=parent)
            components = [BipedFoot.TOE_TOKEN, BipedFoot.BALL_TOKEN, BipedFoot.ANKLE_TOKEN, BipedFoot.HEEL_TOKEN]
            for component in components:
                control = getattr(rig_instance, 'control_%s' % component)
                joint = getattr(rig_instance, component)
                self.assertEqual([round(p, 5) for p in control.offset_group.get_world_position()],
                                 [round(p, 5) for p in joint.get_world_position()])
