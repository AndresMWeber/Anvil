from base import SubRigTemplate
import anvil.node_types as nt

class Spine(SubRigTemplate):

    def build(self, name_tokens):
        self.merge_dicts(name_tokens)
    test_rig = nt.Rig(meta_data=cls.name_tokens)
    sub_rig = test_rig.register_sub_rig('eyeball', meta_data={'name': 'eyeball'})
    test_rig.build()
    sub_rig.build_node(nt.Joint, 'joint_eye', parent=sub_rig.group_joints, meta_data=cls.name_tokens)
    sub_rig.build_node(nt.Control, 'control_eye', parent=sub_rig.group_controls, meta_data=cls.name_tokens,
                       shape='sphere')

    anvil.runtime.dcc.constrain.parent(sub_rig.joint_eye, sub_rig.control_eye.connection_group)
    test_rig.rename()
    cls.test_sub_rig = sub_rig
    cls.test_rig = test_rig
    cls.LOG.info('Built rig for testing %s' % test_rig)
