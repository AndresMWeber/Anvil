from base_sub_rig_template import SubRigTemplate
import anvil.config as cfg


class Limb(SubRigTemplate):
    BUILT_IN_META_DATA = SubRigTemplate.BUILT_IN_META_DATA.merge({'name': 'limb'}, new=True)

    def __init__(self, *args, **kwargs):
        super(Limb, self).__init__(*args, **kwargs)
        self.blend_chain = None
        self.fk_chain = None
        self.ik_chain = None

    def build(self, parent=None, use_layout=True, build_ik=True, build_fk=True, meta_data=None, **kwargs):
        super(Limb, self).build(meta_data=meta_data, parent=parent, **kwargs)
        fk_chain = ik_chain = None
        if build_fk:
            fk_chain, fk_controls = self.build_fk_chain(self.layout_joints,
                                                        skip_register=True,
                                                        skip_report=True,
                                                        **self.build_kwargs)
            self.register_node(fk_chain, hierarchy_id='fk_chain')
            self.register_node(fk_controls, hierarchy_id='fk_controls')

        if build_ik:
            ik_chain, ik_controls, handle, effector = self.build_ik_chain(self.layout_joints,
                                                                          skip_register=True,
                                                                          skip_report=True,
                                                                          **self.build_kwargs)
            self.register_node(ik_chain, hierarchy_id='ik_chain')
            self.register_node(ik_controls, hierarchy_id='ik_controls')
            self.register_node(handle, hierarchy_id='ik_handle')
            self.register_node(effector, hierarchy_id='ik_effector')

        if fk_chain and ik_chain:
            blend_chain = self.build_blend_chain(self.layout_joints,
                                                 [fk_chain, ik_chain],
                                                 skip_register=True,
                                                 skip_report=True,
                                                 use_layout=use_layout, **self.build_kwargs)
            self.register_node(blend_chain, hierarchy_id='blend_chain')

        self.rename()

    def rename(self, *input_dicts, **kwargs):
        super(Limb, self).rename(*input_dicts, **kwargs)

        joint_chain_meta_data = self.meta_data + {cfg.TYPE: cfg.JOINT_TYPE, cfg.PURPOSE: cfg.BLEND}
        self.joint.blend_chain.rename(**joint_chain_meta_data)

        joint_chain_meta_data[cfg.PURPOSE] = cfg.FK
        self.joint.fk_chain.rename(**joint_chain_meta_data)

        joint_chain_meta_data[cfg.PURPOSE] = cfg.IK
        self.joint.ik_chain.rename(**joint_chain_meta_data)
