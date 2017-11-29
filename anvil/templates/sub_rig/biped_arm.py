from six import iteritems
from base import SubRigTemplate
import anvil.node_types as nt
import anvil.runtime as rt
import anvil.validation as validation


class BipedArm(SubRigTemplate):
    BUILT_IN_META_DATA = {'name': 'arm'}

    def __init__(self, joints, layout=None, meta_data=None, parent=None, top_node=None, **flags):
        super(BipedArm, self).__init__(layout=None, meta_data=None, parent=None, top_node=None, **flags)
        self.layout_joints = joints
        self.fk_chain = None
        self.ik_chain = None

    @validation.verify_class_method_inputs([validation.filter_list_joints, validation.filter_list_joints],
                                           [validation.verify_joint_chain_ready, validation.verify_joint_chain_length])
    def build(self, parent=None, meta_data=None, **flags):
        super(BipedArm, self).build(meta_data=meta_data, parent=parent)

        # Build IK/FK chains from the initial layout joints
        for chain_label in ['fk', 'ik']:
            chain = nt.HierarchyChain(rt.dcc.scene.duplicate(self.layout_joints,
                                                             renameChildren=True,
                                                             upstreamNodes=False)[0])
            rt.dcc.scene.parent(chain[0], world=True)
            setattr(self, '%s_chain' % chain_label, chain)
            self.build_inverse_kinematics_chain(chain, chain_label)

        self.rename()
        self.LOG.info('Built sub rig %s' % self.__class__.__name__)

    def build_inverse_kinematics_chain(self, chain, chain_label, meta_data=None):
        meta_data = {'name': chain_label}

        ik_handle_kwargs = {'endEffector': str(chain[-1]),
                            'solver': 'ikRPsolver'}

        for ik_part, label in zip(rt.dcc.rigging.ik_handle(chain[0], **ik_handle_kwargs), ['handle', 'effector']):
            meta_data = self.merge_dicts(self.meta_data, meta_data, {'type': chain_label + label})
            node = self.register_node('%s_%s' % (chain_label, label), nt.Transform(str(ik_part), meta_data=meta_data))
            if label == 'handle':
                node.parent(self.group_nodes)

        rt.dcc.scene.parent(chain[0], self.group_joints)

    def rename(self, *input_dicts, **name_tokens):
        super(BipedArm, self).rename()
        meta_data = {'type': 'joint'}
        self.rename_chain(self.ik_chain, purpose='ik', **meta_data)
        self.rename_chain(self.fk_chain, purpose='fk', **meta_data)
