from six import iteritems
import anvil
import anvil.node_types as nt
from base_test import TestBase


class TestBaseRig(TestBase):
    name_tokens = {'name': 'eye', 'purpose': 'mvp'}

    def setUp(self):
        self.build_rig()
        anvil.LOG.setLevel(anvil.log.logging.INFO)
        super(TestBaseRig, self).setUp()

    def build_rig(self):
        self.test_rig = nt.Rig([])
        self.test_rig.add_node(nt.Joint, 'joint_eye', meta_data=self.name_tokens)
        self.test_rig.add_node(nt.Control, 'control_eye', meta_data=self.name_tokens, shape='sphere')
        self.test_rig.control_eye.meta_data['name'] = 'eyeball'
        self.test_rig.build()
        self.test_rig.rename(**self.name_tokens)

    def tearDown(self):
        TestBase.LOG.info('Cleaning up/Deleting rig top node %s' % self.test_rig.group_root)
        anvil.runtime.dcc.scene.delete(str(self.test_rig.group_root))
        super(TestBaseRig, self).tearDown()


class TestRigEyeBuild(TestBaseRig):
    def test_control_created(self):
        self.assertEqual(self.test_rig.find_node('control_universal'), self.test_rig.control_universal)

    def test_extra_control_created(self):
        self.assertEqual(self.test_rig.find_node('control_eye'), self.test_rig.control_eye)

    def test_extra_joint_created(self):
        self.assertEqual(self.test_rig.find_node('joint_eye'), self.test_rig.joint_eye)

    def test_constraint(self):
        pass

    def test_hierarchy_exists(self):
        """
        'control_universal': <anvil.grouping.control.Control object at 0x000001B010ECBE48>,
        'group_joint': <Transform @ 0x1b010bf0e10 (eye_joint_mvp_GRP)>,
        'group_controls': <Transform @ 0x1b010bf0be0 (eye_controls_mvp_GRP)>,
        'control_eye': <anvil.grouping.control.Control object at 0x000001B010ECF630>,
        'group_nodes': <Transform @ 0x1b010ecbc18 (eye_nodes_mvp_GRP)>,
        'group_world': <Transform @ 0x1b010bf0d68 (eye_world_mvp_GRP)>,
        'group_model': <Transform @ 0x1b010bdadd8 (eye_model_mvp_GRP)>,
        'group_root': <Transform @ 0x1b010ecb550 (eye_rig_mvp_GRP)>,
        'joint_eye': <Joint @ 0x1b010ecf908 (joint5)>
        """
        hierarchy_nodes = [str(node) for key, node in iteritems(self.test_rig.hierarchy)]
        self.assertListEqual(hierarchy_nodes, [])


class TestRigRename(TestBaseRig):
    def test_universal_control_name(self):
        self.assertEqual(str(self.test_rig.control_universal.control), 'eye_universal_mvp_CTR')

    def test_root_name(self):
        self.assertEqual(str(self.test_rig.group_root), 'eye_rig_mvp_GRP')

    def test_sub_groups(self):
        """
        {'control_universal': <anvil.grouping.control.Control object at 0x000001B010ECBE48>,
        'group_joint': <Transform @ 0x1b010bf0e10 (eye_joint_mvp_GRP)>,
        'group_controls': <Transform @ 0x1b010bf0be0 (eye_controls_mvp_GRP)>,
        'control_eye': <anvil.grouping.control.Control object at 0x000001B010ECF630>,
        'group_nodes': <Transform @ 0x1b010ecbc18 (eye_nodes_mvp_GRP)>,
        'group_world': <Transform @ 0x1b010bf0d68 (eye_world_mvp_GRP)>,
        'group_model': <Transform @ 0x1b010bdadd8 (eye_model_mvp_GRP)>,
        'group_root': <Transform @ 0x1b010ecb550 (eye_rig_mvp_GRP)>,
        'joint_eye': <Joint @ 0x1b010ecf908 (joint5)>}
        :return:
        """
        self.assertListEqual([], [])
