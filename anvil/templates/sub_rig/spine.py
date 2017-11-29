from base import SubRigTemplate
import anvil.node_types as nt
import anvil.runtime as rt


class Spine(SubRigTemplate):
    name_tokens = {'name': 'spine'}

    def __init__(self, spine_joints, layout=None, meta_data=None, parent=None, top_node=None, **flags):
        super(Spine, self).__init__(layout=None, meta_data=None, parent=None, top_node=None, **flags)
        self.layout_joints = spine_joints

    def build(self, parent=None, meta_data=None, **flags):
        if len(self.layout_joints) < 4:
            raise ValueError('Need to input more than 4 joints in order to create a %s' % self.__class__.__name__)
        super(Spine, self).build(name_tokens=meta_data, parent=parent)

        # Build Spine Curve
        spine_curve = nt.Curve.build_from_objects(self.layout_joints,
                                                  parent=self.group_nodes,
                                                  meta_data=self.merge_dicts(self.meta_data,
                                                                             {'name': 'spine', 'type': 'curve'}),
                                                  degree=3)
        self.register_node('curve_spine', spine_curve)

        # self.build_node(nt.Joint, 'joint_eye', parent=self.group_joints, meta_data=self.meta_data)
        # self.build_node(nt.Control, 'control_eye', parent=self.group_controls, meta_data=self.meta_data,
        #                shape='sphere')

        # rt.dcc.constrain.parent(self.joint_eye, self.control_eye.connection_group)
        self.rename()
        self.LOG.info('Built sub rig %s' % self.__class__.__name__)
