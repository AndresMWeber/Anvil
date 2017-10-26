from six import iteritems
import anvil
import anvil.node_types as nt
from base_test import TestBase
from pprint import pprint


class TestBaseRig(TestBase):
    name_tokens = {'name': 'eye', 'purpose': 'mvp'}
    test_rig = None

    def build_test_deps(self):
        test_rig = nt.Rig.build(meta_data=self.name_tokens)
        test_rig.build_node(nt.Joint, 'joint_eye', parent=test_rig.group_joints, meta_data=self.name_tokens)
        test_rig.build_node(nt.Control, 'control_eye', parent=test_rig.group_controls, meta_data=self.name_tokens,
                            shape='sphere')
        test_rig.control_eye.meta_data['name'] = 'eyeball'
        test_rig.rename()
        self.test_rig = test_rig
        self.LOG.info('Built rig for testing %r' % test_rig)

class TestRigEyeBuild(TestBaseRig):
    @TestBase.delete_created_nodes
    def test_control_created(self):
        print(self.test_rig.hierarchy)
        self.assertEqual(self.test_rig.find_node('control_universal'), self.test_rig.control_universal)

    @TestBase.delete_created_nodes
    def test_extra_control_created(self):
        self.assertEqual(self.test_rig.find_node('control_eye'), self.test_rig.control_eye)

    @TestBase.delete_created_nodes
    def test_extra_joint_created(self):
        self.assertEqual(self.test_rig.find_node('joint_eye'), self.test_rig.joint_eye)

    @TestBase.delete_created_nodes
    def test_constraint(self):
        anvil.runtime.dcc.constrain.parent(str(self.test_rig.control_eye.top_node), str(self.test_rig.joint_eye))
        print(anvil.runtime.dcc.scene.list_scene(type='parentConstraint'))

    @TestBase.delete_created_nodes
    def test_hierarchy_exists(self):
        for key, node in iteritems(self.test_rig.hierarchy):
            self.LOG.info('Checking to see if node %r at key %s exists...' % (node, key))
            self.assertTrue(anvil.runtime.dcc.scene.exists(str(node)))

    @TestBase.delete_created_nodes
    def test_hierarchy_count(self):
        self.assertEquals(len([node for key, node in iteritems(self.test_rig.hierarchy)]), 9)


class TestRigRename(TestBaseRig):
    @TestBase.delete_created_nodes
    def test_universal_control_name(self):
        self.assertEqual(str(self.test_rig.control_universal.control), 'eye_universal_mvp_CTR')

    @TestBase.delete_created_nodes
    def test_root_name(self):
        self.assertEqual(str(self.test_rig.top_node), 'eye_rig_mvp_GRP')

    @TestBase.delete_created_nodes
    def test_sub_groups(self):
        self.assertListSame(['eye_rig_mvp_GRP',
                             'eye_universal_mvp_OGP',
                             'eyeball_mvp_OGP',
                             'eye_nodes_mvp_GRP',
                             'eye_model_mvp_GRP',
                             'eye_joints_mvp_GRP',
                             'eye_controls_mvp_GRP',
                             'eye_world_mvp_GRP',
                             'eye_rig_mvp_JNT'],
                            [str(self.test_rig.hierarchy[node]) for node in self.test_rig.hierarchy])
