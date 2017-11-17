from base import SubRigTemplate
import anvil.node_types as nt
import anvil.runtime as rt


class Spine(SubRigTemplate):
    name_tokens = {'name': 'spine'}

    def build(self, spine_joints, meta_data=None, parent=None):
        if len(spine_joints) < 4:
            raise ValueError('Need to input more than 4 joints in order to create a %s' % self.__class__.__name__)
        self.meta_data = self.merge_dicts(meta_data)
        super(Spine, self).build(name_tokens=meta_data, parent=parent)

        # Build Spine Curve
        nt.Curve.build_from_objects(spine_joints)
        self.build_node(nt.Joint, 'joint_eye', parent=self.group_joints, meta_data=self.meta_data)
        self.build_node(nt.Control, 'control_eye', parent=self.group_controls, meta_data=self.meta_data,
                        shape='sphere')

        rt.dcc.constrain.parent(self.joint_eye, self.control_eye.connection_group)
        self.rename()
        self.LOG.info('Built sub rig %s' % self.__class__.__name__)
