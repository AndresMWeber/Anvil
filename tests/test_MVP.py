from six import iteritems
from pprint import pprint
import anvil
import anvil.node_types as nt
from base_test import TestBase
from pprint import pprint

class TestBaseRig(TestBase):
    name_tokens = {'name': 'eye', 'purpose': 'mvp'}
    test_rig = None

    @classmethod
    def build_test_deps(cls):
        test_rig = nt.Rig(meta_data=cls.name_tokens)
        sub_rig = test_rig.register_sub_rig('eyeball', name='eyeball')
        test_rig.build()
        sub_rig.build_node(nt.Joint, 'joint_eye', parent=sub_rig.group_joints, meta_data=cls.name_tokens)
        sub_rig.build_node(nt.Control, 'control_eye', parent=sub_rig.group_controls, meta_data=cls.name_tokens,
                            shape='sphere')

        sub_rig.control_eye.meta_data['name'] = 'eyeball'
        anvil.runtime.dcc.constrain.parent(sub_rig.joint_eye, sub_rig.control_eye.connection_group)
        test_rig.rename()
        cls.test_sub_rig = sub_rig
        cls.test_rig = test_rig
        cls.LOG.info('Built rig for testing %r' % test_rig)
        return test_rig

class TestRigEyeBuild(TestBaseRig):
    @TestBase.delete_created_nodes
    def test_control_created(self):
        self.assertEqual(self.test_rig.find_node('control_universal'), self.test_rig.control_universal)

    @TestBase.delete_created_nodes
    def test_extra_control_created(self):
        self.assertEqual(self.test_sub_rig.find_node('control_eye'), self.test_sub_rig.control_eye)

    @TestBase.delete_created_nodes
    def test_extra_joint_created(self):
        self.assertEqual(self.test_sub_rig.find_node('joint_eye'), self.test_sub_rig.joint_eye)

    @TestBase.delete_created_nodes
    def test_constraint(self):
        self.assertTrue(anvil.runtime.dcc.scene.list_scene(type='parentConstraint'))

    @TestBase.delete_created_nodes
    def test_hierarchy_exists(self):
        for key, node in iteritems(self.test_rig.hierarchy):
            self.LOG.info('Checking to see if node %r at key %s exists...' % (node, key))
            self.assertTrue(anvil.runtime.dcc.scene.exists(str(node)))

    @TestBase.delete_created_nodes
    def test_hierarchy_count(self):
        self.assertEquals(len(list(self.test_rig.hierarchy)), 5)

    @TestBase.delete_created_nodes
    def test_sub_rig_hierarchy_count(self):
        self.assertEquals(len(list(self.test_rig.sub_rigs['eyeball'].hierarchy)), 8)

    @TestBase.delete_created_nodes
    def test_sub_rig_count(self):
        self.assertEquals(len(list(self.test_rig.sub_rigs)), 1)

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
                             'eye_sub_rigs_mvp_GRP',
                             'eye_universal_mvp_OGP',
                             'eyeball_mvp_OGP',
                             'eye_extras_mvp_GRP',
                             'eye_model_mvp_GRP'],
                            [str(self.test_rig.hierarchy[node]) for node in self.test_rig.hierarchy])
