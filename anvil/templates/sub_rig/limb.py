from base import SubRigTemplate
import anvil.node_types as nt
import anvil.validation as validation


class Limb(SubRigTemplate):
    BUILT_IN_META_DATA = {'name': 'limb'}

    def __init__(self, joints, layout=None, meta_data=None, parent=None, top_node=None, **flags):
        super(Limb, self).__init__(layout=None, meta_data=None, parent=None, top_node=None, **flags)
        self.layout_joints = joints
        self.blend_chain = None
        self.fk_chain = None
        self.ik_chain = None

    @validation.verify_class_method_inputs([validation.filter_list_joints, validation.filter_list_joints],
                                           [validation.verify_joint_chain_ready, validation.verify_joint_chain_length])
    def build(self, parent=None, use_layout=True, build_ik=True, build_fk=True, meta_data=None, **flags):
        super(Limb, self).build(meta_data=meta_data, parent=parent, **flags)
        self.build_internal_structure(use_layout=use_layout, build_ik=build_ik, build_fk=build_fk)
        self.build_control_structure()
        self.rename()
        self.LOG.info('Built sub rig %s' % self.__class__.__name__)

    def build_internal_structure(self, build_ik=True, build_fk=True, use_layout=True):
        self.blend_chain = nt.HierarchyChain(self.layout_joints, duplicate=not use_layout)
        self.blend_chain.parent(self.group_joints)

        # Build IK/FK chains from the initial layout joints
        if build_fk:
                self.fk_chain = nt.HierarchyChain(self.layout_joints, duplicate=True)
                self.fk_chain.parent(self.group_joints)

        if build_ik:
            self.ik_chain = nt.HierarchyChain(self.layout_joints, duplicate=True)
            self.ik_chain.parent(self.group_joints)
            handle, effector = self.ik_chain.build_ik()
            self.register_node('ik_handle', handle, meta_data={'name': 'ik', 'type': 'ikhandle'})
            self.register_node('ik_effector', effector, meta_data={'name': 'ik', 'type': 'ikeffector'})
            self.ik_handle.parent(self.group_nodes)

    def build_control_structure(self):
        pass

    def rename(self, *input_dicts, **name_tokens):
        super(Limb, self).rename()
        meta_data = {'type': 'joint'}
        self.rename_chain(self.fk_chain or [], purpose='blend', **meta_data)
        self.rename_chain(self.fk_chain or [], purpose='fk', **meta_data)
        self.rename_chain(self.ik_chain or [], purpose='ik', **meta_data)
