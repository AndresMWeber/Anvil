from six import iteritems, itervalues
import string
import anvil.config as cfg
import anvil.node_types as nt
from anvil.sub_rig_templates import Hand
from tests.base_test import TestBase, clean_up_scene, auto_save_result


class TestHandBase(TestBase):
    hand = None

    name_tokens = {'name': 'hoof', 'purpose': 'mvp'}
    HAND_MERC_JOINTS = ['j_pa_r', 'j_ra_r', 'j_ia_r', 'j_ma_r', 'j_ta_r']
    TEMPLATE_CLASS = Hand

    @classmethod
    def from_template_file(cls, template_file, finger_start_joints=None, **kwargs):
        cls.import_template_files(template_file)
        cls.LOG.info('Successfully imported template file %s' % template_file)

        kwargs['layout_joints'] = []
        for finger in finger_start_joints:
            kwargs['layout_joints'].append(list(nt.NodeChain(finger)))

        rig_instance = cls.TEMPLATE_CLASS(**kwargs)
        rig_instance.build(**kwargs)
        return rig_instance


class TestBuildHand(TestHandBase):
    def setUp(self):
        if self.hand is None:
            self.__class__.hand = self.from_template_file(self.HAND_MERC,
                                                          self.HAND_MERC_JOINTS,
                                                          solver=cfg.IK_RP_SOLVER)

    def test_number_of_controls_from_flat_hierarchy(self):
        self.assertEqual(len(self.hand.hierarchy.control.to_flat_list()), 25)

    def test_number_of_joints_from_flat_hierarchy(self):
        self.assertEqual(len(self.hand.hierarchy.joint.to_flat_list()), 60)

    def test_number_of_joint_top_groups_from_get_children(self):
        self.assertEqual(len(self.hand.group_joints.get_children()), 15)

    def test_number_of_control_top_groups_from_get_children(self):
        self.assertEqual(len(self.hand.group_controls.get_children()), 15)

    def test_number_of_nodes_from_get_children(self):
        self.assertEqual(len(self.hand.group_nodes.get_children()), 15)

    def test_control_names(self):
        top_groups = ['A_fk_OGP', 'A_ik_OGP', 'A_pv_OGP']
        self.assertIn([name + ending for ending in top_groups for name in self.TEMPLATE_CLASS.DEFAULT_NAMES],
                      self.hand.hierarchy.control.to_flat_list())

    def test_joint_names(self):
        top_groups = ['A_fk_JNT', 'A_ik_JNT', 'A_blend_JNT']
        self.assertIn(['%s_%s' % (name, ending) for ending in top_groups for name in self.TEMPLATE_CLASS.DEFAULT_NAMES],
                      self.hand.hierarchy.joint.to_flat_list())

    def test_node_names(self):
        top_groups = ['IKHANDLE']
        self.assertIn(['%s_%s' % (name, ending) for ending in top_groups for name in self.TEMPLATE_CLASS.DEFAULT_NAMES],
                      self.hand.hierarchy.node.to_flat_list())


class TestBuildDefaultHand(TestHandBase):
    @clean_up_scene
    @auto_save_result
    def test_build_with_parent(self):
        parent = nt.Transform.build(name='test')
        rig_instance = self.from_template_file(self.HAND_MERC, self.HAND_MERC_JOINTS, parent=parent)
        self.assertEqual(str(rig_instance.root.get_parent()), str(parent))

    @clean_up_scene
    @auto_save_result
    def test_build_no_kwargs_no_errors(self):
        self.assertIsNotNone(self.from_template_file(self.HAND_MERC, self.HAND_MERC_JOINTS))

    @clean_up_scene
    @auto_save_result
    def test_build_with_rp_solver(self):
        self.assertIsNotNone(self.from_template_file(self.HAND_MERC, self.HAND_MERC_JOINTS, solver=cfg.IK_RP_SOLVER))


class TestGetFingerBaseNames(TestHandBase):
    @classmethod
    def setUpClass(cls):
        cls.hand = cls.TEMPLATE_CLASS(cls.HAND_MERC_JOINTS)

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
