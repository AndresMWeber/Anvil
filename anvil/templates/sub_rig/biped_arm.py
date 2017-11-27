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
                                                  meta_data=self.merge_dicts(self.meta_data,
                                                                             {'name': 'spine', 'type': 'curve'}),
                                                  degree=3)
        self.register_node('curve_spine', spine_curve)

        for chain_type in ['ik', 'fk']:
            meta_data = {'name': chain_type}
            chain = nt.HierarchyChain(rt.dcc.scene.duplicate(self.layout_joints, renameChildren=True)[0])
            setattr(self, '%s_chain' % chain_type, chain)
            print(chain, list(chain), chain[0], chain[-1], list(chain)[-1])
            print(rt.dcc.scene.get_scene_tree())
            ik_handle_kwargs = {'endEffector': str(chain[-1]),
                                'curve': str(spine_curve),
                                'createCurve': False,
                                'solver': 'ikRPsolver'}

            for ik_part, label in zip(rt.dcc.rigging.ik_handle(chain[0], **ik_handle_kwargs), ['handle', 'effector']):
                meta_data.update({'type': chain_type + label})
                node = self.register_node('%s_%s' % (chain_type, label),
                                          nt.Transform(str(ik_part),
                                                       meta_data=self.merge_dicts(self.meta_data, meta_data)))
                if label == 'handle':
                    node.parent(self.group_nodes)

                print(chain, self.group_joints)
                rt.dcc.scene.parent(chain, self.group_joints)

                # self.build_node(nt.Joint, 'joint_eye', parent=self.group_joints, meta_data=self.meta_data)
                # self.build_node(nt.Control, 'control_eye', parent=self.group_controls, meta_data=self.meta_data,
                #                shape='sphere')

                # rt.dcc.constrain.parent(self.joint_eye, self.control_eye.connection_group)
                self.rename()
                self.LOG.info('Built sub rig %s' % self.__class__.__name__)

    def rename(self, *input_dicts, **name_tokens):
        super(BipedArm, self).rename()
        meta_data = {'type': 'joint'}
        print(self.ik_chain, self.fk_chain)
        ik_chain_hierarchy = nt.HierarchyChain(self.ik_chain[0], node_filter='joint')
        self.rename_chain(ik_chain_hierarchy, purpose='ik', **meta_data)
        fk_chain_hierarchy = nt.HierarchyChain(self.fk_chain[0], node_filter='joint')
        self.rename_chain(fk_chain_hierarchy, purpose='fk', **meta_data)
