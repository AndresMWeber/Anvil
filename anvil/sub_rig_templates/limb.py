from base import SubRigTemplate
import anvil.node_types as nt
import anvil.validation as validation
import anvil.runtime as rt
import anvil.config as cfg

class Limb(SubRigTemplate):
    BUILT_IN_META_DATA = {'name': 'limb'}

    def __init__(self, layout_joints, meta_data=None, parent=None, top_node=None, **flags):
        super(Limb, self).__init__(layout=layout_joints, meta_data=meta_data, parent=parent, top_node=top_node, **flags)
        self.layout_joints = layout_joints
        self.blend_chain = []
        self.fk_chain = []
        self.ik_chain = []

    @validation.verify_class_method_inputs([validation.filter_list_joints, validation.filter_list_joints],
                                           [validation.verify_joint_chain_ready, validation.verify_joint_chain_length])
    def build(self, parent=None, use_layout=True, build_ik=True, build_fk=True, meta_data=None, **flags):
        super(Limb, self).build(meta_data=meta_data, parent=parent, **flags)
        self.prep_joint_chain_for_rigging(self.layout_joints)
        self.build_blend(self.layout_joints, use_layout=use_layout)

        # Build IK/FK chains from the initial layout joints
        if build_fk:
            self.build_fk(self.layout_joints)

        if build_ik:
            self.build_ik(self.layout_joints)

        self.rename()
        self.LOG.info('Built sub rig %s' % self.__class__.__name__)

    def build_blend(self, layout_joints, use_layout):
        self.blend_chain = nt.HierarchyChain(layout_joints, duplicate=not use_layout, parent=self.group_joints)

    def build_fk(self, layout_joints):
        self.fk_chain = nt.HierarchyChain(layout_joints, duplicate=True, parent=self.group_joints)

    def build_ik(self, layout_joints, ik_end_index=-1):
        self.ik_chain = nt.HierarchyChain(layout_joints, duplicate=True, parent=self.group_joints)
        handle, effector = self.ik_chain.build_ik(chain_end=self.ik_chain[ik_end_index])
        self.register_node(cfg.IK_HANDLE, handle, meta_data={cfg.NAME: cfg.IK, cfg.TYPE: cfg.IK_HANDLE})
        self.register_node(cfg.IK_EFFECTOR, effector, meta_data={cfg.NAME: cfg.IK, cfg.TYPE: cfg.IK_EFFECTOR})
        self.ik_handle.parent(self.group_nodes)

        self.build_node(nt.Control, '%s_%s' % (cfg.CONTROL_TYPE, cfg.IK),
                        parent=self.group_controls,
                        shape='flat_diamond',
                        reference_object=self.ik_chain[-1],
                        meta_data={cfg.PURPOSE: cfg.IK})

        self.build_pole_vector_control(self.ik_chain,
                                       self.ik_handle,
                                       '%s_%s_%s' % (cfg.CONTROL_TYPE, cfg.IK, cfg.POLE_VECTOR),
                                       meta_data={cfg.PURPOSE: cfg.POLE_VECTOR})

        rt.dcc.constrain.translate(self.control_ik.connection_group, self.ik_handle)

    def prep_joint_chain_for_rigging(self, joint_chain):
        for joint in joint_chain:
            pass
        #joint_chain[-1].jointOrient.set([0, 0, 0])

    def rename(self, *input_dicts, **name_tokens):
        super(Limb, self).rename()
        meta_data = {cfg.TYPE: cfg.JOINT_TYPE}
        self.rename_chain(list(self.blend_chain), purpose=cfg.BLEND, **meta_data)
        self.rename_chain(list(self.fk_chain), purpose=cfg.FK, **meta_data)
        self.rename_chain(list(self.ik_chain), purpose=cfg.IK, **meta_data)
