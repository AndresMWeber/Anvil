from six import iteritems
from base import SubRigTemplate
import anvil.node_types as nt
import anvil.runtime as rt
import anvil.validation as validation


class BipedArm(SubRigTemplate):
    name_tokens = {'name': 'arm'}

    def __init__(self, joints, layout=None, meta_data=None, parent=None, top_node=None, **flags):
        super(BipedArm, self).__init__(layout=None, meta_data=None, parent=None, top_node=None, **flags)
        self.layout_joints = joints
        self.fk_chain = None
        self.ik_chain = None

    @validation.verify_class_method_inputs([validation.filter_list_joints, validation.filter_list_joints],
                                           [validation.verify_joint_chain_ready, validation.verify_joint_chain_length])
    def build(self, parent=None, meta_data=None, **flags):
        super(BipedArm, self).build(name_tokens=meta_data, parent=parent)

        # Build Spine Curve
        spine_curve = nt.Curve.build_from_objects(self.layout_joints,
                                                  parent=self.group_nodes,
                                                  meta_data=self.merge_dicts(self.meta_data, {'name': 'spine'}),
                                                  degree=3)
        self.register_node('curve_spine', spine_curve)

        for chain_type in ['ik', 'fk']:
            chain = rt.dcc.scene.duplicate(self.layout_joints)
            setattr(self, '%s_chain' % chain_type, chain)
            chain_hierarchy = nt.HierarchyChain(chain[0], node_filter='joint')

            ik_handle, effector = rt.dcc.rigging.ik_handle(chain_hierarchy[0],
                                                           endEffector=str(chain[-1]),
                                                           curve=str(spine_curve),
                                                           createCurve=False,
                                                           solver='ikRPsolver')

            self.register_node(chain_type + '_solver', nt.DagNode(ik_handle))
            self.register_node(chain_type + '_effector', nt.DagNode(effector))

        # self.build_node(nt.Joint, 'joint_eye', parent=self.group_joints, meta_data=self.meta_data)
        # self.build_node(nt.Control, 'control_eye', parent=self.group_controls, meta_data=self.meta_data,
        #                shape='sphere')

        # rt.dcc.constrain.parent(self.joint_eye, self.control_eye.connection_group)
        self.rename()
        self.LOG.info('Built sub rig %s' % self.__class__.__name__)

    def rename(self, *input_dicts, **name_tokens):
        super(BipedArm, self).rename()
        meta_data = {'name': 'ikSolver', 'type': 'ik_handle'}
        self.rename_chain(self.ik_chain, purpose='ik', **meta_data)
        self.rename_chain(self.fk_chain, purpose='fk', **meta_data)
