from six import iteritems
import anvil.node_types as nt
from anvil.utils.scene import print_scene_tree
from anvil.sub_rig_templates import Hand
from tests.base_test import TestBase, clean_up_scene
import string
from pprint import pprint


class TestHandBase(TestBase):
    hand = None
    name_tokens = {'name': 'hoof', 'purpose': 'mvp'}
    HAND_MERC_JOINTS = ['j_pa_r', 'j_ra_r', 'j_ia_r', 'j_ma_r', 'j_ta_r']
    TEMPLATE_CLASS = Hand

    @classmethod
    def from_template_file(cls, template_file, finger_start_joints=None, **kwargs):
        cls.import_template_files(template_file)

        finger_joints = []
        for finger in finger_start_joints:
            finger_joints.append(list(nt.LinearHierarchyNodeSet(finger)))

        rig_instance = cls.TEMPLATE_CLASS(layout_joints=finger_joints, **kwargs)
        rig_instance.build(**kwargs)
        return rig_instance


class TestBuildHand(TestHandBase):
    @classmethod
    def setUpClass(cls):
        super(TestBuildHand, cls).setUpClass()
        try:
            cls.hand = cls.from_template_file(cls.HAND_MERC, cls.HAND_MERC_JOINTS)
        except (IndexError, KeyError) as e:
            print_scene_tree()
            raise e

    def test_build_no_kwargs_no_errors(self):
        self.assertIsNotNone(self.hand)

    def test_number_of_controls(self):

        controls = [node for node in self.hand._flat_hierarchy() if isinstance(node, nt.Control)]
        self.assertEqual(len(controls), 15)

    def test_number_of_control_top_groups(self):
        pprint(self.hand.hierarchy)
        self.assertEqual(len(self.hand.group_controls.get_children()), 10)

    def test_number_of_joint_chains(self):
        pprint(self.hand.hierarchy)
        self.assertEqual(len(self.hand.group_joints.get_children()), 15)

    def test_number_of_nodes(self):
        pprint(self.hand.hierarchy)
        self.assertEqual(len(self.hand.group_nodes.get_children()), 5)


class TestBuildDefaultHand(TestHandBase):
    @clean_up_scene
    def test_build_with_parent(self):
        parent = nt.Transform.build(name='test')
        rig_instance = self.from_template_file(self.HAND_MERC, self.HAND_MERC_JOINTS, parent=parent)
        self.assertEqual(str(rig_instance.root.get_parent()), str(parent))


class TestGetFingerBaseNames(TestHandBase):
    @classmethod
    def setUpClass(cls):
        super(TestGetFingerBaseNames, cls).setUpClass()
        cls.hand = Hand(cls.HAND_MERC_JOINTS)

    def test_default_with_thumb_from_fbx(self):
        self.hand.layout_joints = self.HAND_MERC_JOINTS
        self.hand.has_thumb = True
        self.assertEqual(self.hand.get_finger_base_names(), Hand.DEFAULT_NAMES)

    def test_no_thumb_4(self):
        self.hand.layout_joints = ['a' * x for x in range(4)]
        self.hand.has_thumb = False
        self.assertEqual(self.hand.get_finger_base_names(), Hand.DEFAULT_NAMES[1:5])

    def test_no_thumb_5(self):
        self.hand.layout_joints = ['a' * x for x in range(5)]
        self.hand.has_thumb = False
        self.assertEqual(self.hand.get_finger_base_names(), ['fingerA', 'fingerB', 'fingerC', 'fingerD', 'fingerE'])

    def test_no_thumb_under_5(self):
        self.hand.layout_joints = ['a' * x for x in range(3)]
        self.hand.has_thumb = False
        self.assertEqual(self.hand.get_finger_base_names(), Hand.DEFAULT_NAMES[1:4])

    def test_no_thumb_over_5(self):
        self.hand.layout_joints = ['a' * x for x in range(10)]
        self.has_thumb = False
        self.assertEqual(self.hand.get_finger_base_names(),
                         ['finger' + string.ascii_uppercase[i] for i in range(10)])

    def test_thumb_under_5(self):
        self.hand.layout_joints = ['a' * x for x in range(4)]
        self.hand.has_thumb = True
        self.assertEqual(self.hand.get_finger_base_names(), Hand.DEFAULT_NAMES[:4])

    def test_thumb_over_5(self):
        self.hand.layout_joints = ['a' * x for x in range(10)]
        self.hand.has_thumb = True
        self.assertEqual(self.hand.get_finger_base_names(), ['finger' + string.ascii_uppercase[i] for i in range(10)])
