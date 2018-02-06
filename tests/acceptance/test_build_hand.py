from six import iteritems
import anvil.node_types as nt
from anvil.sub_rig_templates import Hand
from tests.base_test import TestBase, cleanup_nodes
import anvil.runtime as rt
import string

class TestHandBase(TestBase):
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


class TestBuildHand(TestHandBase):
    @classmethod
    def setUpClass(cls):
        cls.rig = cls.from_template_file(cls.HAND_MERC['file'], cls.HAND_MERC['joints'])

    @classmethod
    def tearDownClass(cls):
        cleanup_nodes()

    def test_build_no_kwargs_no_errors(self):
        self.assertIsNotNone(self.rig)

    def test_build_with_parent(self):
        with cleanup_nodes():
            parent = nt.Transform.build(name='test')
            rig_instance = self.from_template_file(self.HAND_MERC['file'], self.HAND_MERC['joints'], parent=parent)
            self.assertEqual(str(rig_instance.root.get_parent()), str(parent))

    def test_number_of_controls(self):
        self.assertEqual(
            len(list([node for key, node in iteritems(self.rig.hierarchy) if isinstance(node, nt.Control)])),
            4)

    def test_control_positions_match(self):
        components = [Hand.TOE_TOKEN, Hand.BALL_TOKEN, Hand.ANKLE_TOKEN, Hand.HEEL_TOKEN]

        for component in components:
            control = getattr(self.rig, 'control_%s' % component)
            joint = getattr(self.rig, component)
            self.assertEqual([round(p, 5) for p in control.offset_group.get_world_position()],
                             [round(p, 5) for p in joint.get_world_position()])

    def test_number_of_joint_chains(self):
        self.assertEqual(
            len(list([node for key, node in iteritems(self.rig.hierarchy) if isinstance(node, nt.Joint)])),
            24)


class TestGetFingerBaseNames(TestHandBase):
    def test_default_with_thumb_from_fbx(self):
        hand = Hand(self.HAND_MERC['joints'])
        self.assertEqual(hand.get_finger_base_names(), Hand.DEFAULT_NAMES)

    def test_no_thumb_4(self):
        hand = Hand(['a' * x for x in range(4)], has_thumb=False)
        self.assertEqual(hand.get_finger_base_names(),  Hand.DEFAULT_NAMES[1:5])

    def test_no_thumb_5(self):
        hand = Hand(['a' * x for x in range(5)], has_thumb=False)
        self.assertEqual(hand.get_finger_base_names(), ['fingerA', 'fingerB', 'fingerC', 'fingerD', 'fingerE'])

    def test_no_thumb_under_5(self):
        hand = Hand(['a' * x for x in range(3)], has_thumb=False)
        self.assertEqual(hand.get_finger_base_names(), Hand.DEFAULT_NAMES[1:4])

    def test_no_thumb_over_5(self):
        hand = Hand(['a' * x for x in range(10)], has_thumb=False)
        self.assertEqual(hand.get_finger_base_names(),
                         ['finger'+string.ascii_uppercase[i] for i in range(10)])

    def test_thumb_under_5(self):
        hand = Hand(['a' * x for x in range(4)])
        self.assertEqual(hand.get_finger_base_names(), Hand.DEFAULT_NAMES[:4])

    def test_thumb_over_5(self):
        hand = Hand(['a' * x for x in range(10)])
        self.assertEqual(hand.get_finger_base_names(), ['finger'+string.ascii_uppercase[i] for i in range(10)])
