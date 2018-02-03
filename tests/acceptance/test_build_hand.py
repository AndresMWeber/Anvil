from six import iteritems
import anvil.node_types as nt
from anvil.sub_rig_templates import Hand
from tests.base_test import TestBase, cleanup_nodes
import anvil.runtime as rt


class TestBuildHand(TestBase):
    name_tokens = {'name': 'hoof', 'purpose': 'mvp'}
    HAND_MERC = {'file': "test_skeleton_hand.fbx",
                 'joints': ['j_pa_r', 'j_ra_r', 'j_ia_r', 'j_ma_r', 'j_ta_r']}

    @classmethod
    def from_template_file(cls, template_file, finger_start_joints=None, **kwargs):
        rt.dcc.scene.fileop(template_file,
                            i=True,
                            type="FBX",
                            ignoreVersion=True,
                            ra=True,
                            mergeNamespacesOnClash=False,
                            options="fbx",
                            pr=True)

        finger_joints = []
        for finger in finger_start_joints:
            finger_joints.append(list(nt.HierarchyChain(finger)))

        rig_instance = Hand(layout_joints=finger_joints, **kwargs)
        rig_instance.build(**kwargs)
        return rig_instance

    def test_build_no_kwargs_no_errors(self):
        with cleanup_nodes():
            self.from_template_file(self.HAND_MERC['file'], self.HAND_MERC['joints'])

    def test_build_with_parent(self):
        with cleanup_nodes():
            parent = nt.Transform.build(name='test')
            rig_instance = self.from_template_file(self.HAND_MERC['file'], self.HAND_MERC['joints'], parent=parent)
            self.assertEqual(str(rig_instance.root.get_parent()), str(parent))

    def test_number_of_controls(self):
        with cleanup_nodes():
            parent = nt.Transform.build(name='test')
            rig_instance = self.from_template_file(self.HAND_MERC['file'], self.HAND_MERC['joints'], parent=parent)
            self.assertEqual(
                len(list([node for key, node in iteritems(rig_instance.hierarchy) if isinstance(node, nt.Control)])),
                4)

    def test_control_positions_match(self):
        with cleanup_nodes():
            parent = nt.Transform.build(name='test')
            rig_instance = self.from_template_file(self.HAND_MERC['file'], self.HAND_MERC['joints'], parent=parent)
            components = [Hand.TOE_TOKEN, Hand.BALL_TOKEN, Hand.ANKLE_TOKEN, Hand.HEEL_TOKEN]
            for component in components:
                control = getattr(rig_instance, 'control_%s' % component)
                joint = getattr(rig_instance, component)
                self.assertEqual([round(p, 5) for p in control.offset_group.get_world_position()],
                                 [round(p, 5) for p in joint.get_world_position()])
