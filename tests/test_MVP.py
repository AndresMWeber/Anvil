from six import iteritems
import anvil
import anvil.node_types as nt
from base_test import TestBase
from pprint import pprint

global build_count
build_count = 0


class TestBaseRig(TestBase):
    name_tokens = {'name': 'eye', 'purpose': 'mvp'}

    def setUp(self):
        self.test_rig = None
        self.build_rig()
        anvil.LOG.setLevel(anvil.log.logging.INFO)
        super(TestBaseRig, self).setUp()

    def build_rig(self):
        global build_count
        print(anvil.runtime.dcc.scene.list_scene_nodes())

        if not anvil.runtime.dcc.scene.exists('eye_rig_mvp_GRP'):
            self.test_rig = nt.Rig(meta_data=self.name_tokens)
            self.test_rig.add_node(nt.Joint, 'joint_eye', parent=self.test_rig.group_joints, meta_data=self.name_tokens)
            self.test_rig.add_node(nt.Control, 'control_eye', parent=self.test_rig.group_controls, meta_data=self.name_tokens, shape='sphere')
            self.test_rig.control_eye.meta_data['name'] = 'eyeball'
            self.test_rig.build()
            self.test_rig.rename()
            TestBase.LOG.info('Created Test Rig %d times'% build_count)
            build_count += 1

    def tearDown(self):
        TestBase.LOG.info('Cleaning up/Deleting rig top node %s' % self.test_rig.top_node)
        anvil.runtime.dcc.scene.delete([str(node) for key, node in iteritems(self.test_rig.hierarchy)])
        super(TestBaseRig, self).tearDown()


class TestRigEyeBuild(TestBaseRig):
    def test_control_created(self):
        self.assertEqual(self.test_rig.find_node('control_universal'), self.test_rig.control_universal)

    def test_extra_control_created(self):
        self.assertEqual(self.test_rig.find_node('control_eye'), self.test_rig.control_eye)

    def test_extra_joint_created(self):
        self.assertEqual(self.test_rig.find_node('joint_eye'), self.test_rig.joint_eye)

    def test_constraint(self):
        anvil.runtime.dcc.constrain.parent(str(self.test_rig.control_eye.top_node), str(self.test_rig.joint_eye))
        print(anvil.runtime.dcc.scene.list_scene(type='parentConstraint'))

    def test_hierarchy_exists(self):
        self.assertTrue(
            all([anvil.runtime.dcc.scene.exists(str(node)) for key, node in iteritems(self.test_rig.hierarchy)]))

    def test_hierarchy_count(self):
        self.assertEquals(len([node for key, node in iteritems(self.test_rig.hierarchy)]), 9)


class TestRigRename(TestBaseRig):
    def test_universal_control_name(self):
        self.assertEqual(str(self.test_rig.control_universal.control), 'eye_universal_mvp_CTR')

    def test_root_name(self):
        print(self.test_rig.hierarchy)
        self.assertEqual(str(self.test_rig.top_node), 'eye_rig_mvp_GRP')

    def test_sub_groups(self):
        pprint(anvil.runtime.dcc.scene.list_scene_nodes(), indent=2)
        self.assertListSame(['eye_rig_mvp_GRP',
                             'eye_universal_mvp_CTR',
                             'eyeball_mvp_CTR',
                             'eye_nodes_mvp_GRP',
                             'eye_model_mvp_GRP',
                             'eye_joints_mvp_GRP',
                             'eye_controls_mvp_GRP',
                             'eye_world_mvp_GRP',
                             'eye_rig_mvp_JNT'],
                            [str(self.test_rig.hierarchy[node]) for node in self.test_rig.hierarchy])
