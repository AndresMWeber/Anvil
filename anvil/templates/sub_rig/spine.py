from base import SubRigTemplate
import anvil.node_types as nt
import anvil.runtime as rt


class Spine(SubRigTemplate):
    name_tokens = {'name': 'spine'}

    def build(self, spine_joints, name_tokens, parent=None):
        super(Spine, self).build(name_tokens=name_tokens, parent=parent)
        self.meta_data = self.merge_dicts(name_tokens)

        # Build Spine Curve

        self.build_node(nt.Joint, 'joint_eye', parent=self.group_joints, meta_data=self.meta_data)
        self.build_node(nt.Control, 'control_eye', parent=self.group_controls, meta_data=self.meta_data,
                        shape='sphere')

        rt.dcc.constrain.parent(self.joint_eye, self.control_eye.connection_group)
        self.rename()
        self.LOG.info('Built sub rig %s' % self.__class__.__name__)
