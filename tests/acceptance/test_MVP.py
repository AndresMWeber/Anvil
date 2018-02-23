from six import itervalues
import anvil
import anvil.node_types as nt
from tests.base_test import TestBase, sanitize_scene


class TestBaseRig(TestBase):
    name_tokens = {'name': 'eye', 'purpose': 'mvp', 'character': 'bert'}
    test_rig = None

    @classmethod
    def setUpClass(cls):
        sanitize_scene()
        super(TestBaseRig, cls).setUpClass()
        cls.build_dependencies()

    @classmethod
    def tearDownClass(cls):
        super(TestBaseRig, cls).tearDownClass()
        sanitize_scene()

    @classmethod
    def build_dependencies(cls):
        super(TestBaseRig, cls).build_dependencies()
        test_rig = nt.Rig(name_tokens=cls.name_tokens)
        sub_rig = test_rig.build_sub_rig('eyeball', name_tokens={'name': 'eyeball'})
        test_rig.build()
        sub_rig.build_node(nt.Joint, hierarchy_id='eye', parent=sub_rig.group_joints)
        sub_rig.build_node(nt.Control, hierarchy_id='eye', parent=sub_rig.group_controls, shape='sphere')
        anvil.runtime.dcc.connections.parent(sub_rig.joint.eye, sub_rig.control.eye.node.connection_group)
        test_rig.rename()
        cls.test_sub_rig = sub_rig
        cls.test_rig = test_rig
        cls.LOG.info('Built rig for testing %s' % test_rig)
        return test_rig


class TestRigEyeBuild(TestBaseRig):
    def test_control_created(self):
        self.assertEqual(self.test_rig.find_node('universal'), self.test_rig.control.universal)

    def test_extra_control_created(self):
        self.assertEqual(self.test_sub_rig.find_node('eye', 'control'), self.test_sub_rig.control.eye)

    def test_extra_joint_created(self):
        self.assertEqual(self.test_sub_rig.find_node('eye', 'joint'), self.test_sub_rig.joint.eye)

    def test_constraint(self):
        self.assertTrue(anvil.runtime.dcc.scene.list_scene(type='parentConstraint'))

    def test_hierarchy_exists(self):
        for node in list(self.test_rig._flat_hierarchy()):
            if anvil.is_agrouping(node):
                for n in node._flat_hierarchy():
                    self.assertTrue(anvil.runtime.dcc.scene.exists(n))
            else:
                self.assertTrue(anvil.runtime.dcc.scene.exists(node))

    def test_hierarchy_count(self):
        self.assertEquals(len(list(self.test_rig._flat_hierarchy())), 5)

    def test_sub_rig_hierarchy_count(self):
        print(list(self.test_rig.sub_rigs['eyeball']._flat_hierarchy()))
        self.assertEquals(len(list(self.test_rig.sub_rigs['eyeball']._flat_hierarchy())), 8)

    def test_sub_rig_count(self):
        self.assertEquals(len(list(self.test_rig.sub_rigs)), 1)


class TestRigRename(TestBaseRig):
    def test_universal_control_name(self):
        self.assertEqual(str(self.test_rig.control.universal.controller), 'bert_eye_universal_mvp_CTR')

    def test_root_name(self):
        self.assertEqual(str(self.test_rig.root), 'bert_rig_eye_mvp_GRP')

    def test_sub_groups(self):
        self.assertListSame(sorted(['bert_rig_eye_mvp_GRP',
                                    'bert_eye_sub_rigs_mvp_GRP',
                                    'bert_eye_extras_mvp_GRP',
                                    'bert_eye_model_mvp_GRP']),
                            sorted([str(node) for node in itervalues(self.test_rig.hierarchy.node)]))

    def test_control_offset(self):
        self.assertEqual(str(self.test_rig.hierarchy.control.universal.offset_group), 'bert_eye_universal_mvp_OGP')