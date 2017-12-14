from base import SubRigTemplate
import anvil.node_types as nt
import anvil.validation as validation
import anvil.runtime as rt
import anvil.config as cfg


class Limb(SubRigTemplate):
    BUILT_IN_META_DATA = {'name': 'limb'}

    def __init__(self, *args, **kwargs):
        super(Limb, self).__init__(*args, **kwargs)
        self.blend_chain = []
        self.fk_chain = []
        self.ik_chain = []

    def build(self, parent=None, use_layout=True, build_ik=True, build_fk=True, meta_data=None, **kwargs):
        super(Limb, self).build(meta_data=meta_data, parent=parent, **kwargs)
        self.prep_joint_chain_for_rigging(self.layout_joints)

        # Build IK/FK chains from the initial layout joints
        if build_fk:
            self.LOG.info('Building FK chain on %r from layout joints %r.' % (self, self.layout_joints))
            self.build_fk_chain(self.layout_joints, **self.build_kwargs)

        if build_ik:
            self.LOG.info('Building IK chain on %r from layout joints %r.' % (self, self.layout_joints))
            self.build_ik_chain(self.layout_joints, **self.build_kwargs)

        self.build_blend_chain(self.layout_joints, use_layout=use_layout, **self.build_kwargs)
        self.rename()

    def rename(self, *input_dicts, **name_tokens):
        super(Limb, self).rename()
        meta_data = {cfg.TYPE: cfg.JOINT_TYPE}
        self.rename_chain(list(self.blend_chain), purpose=cfg.BLEND, **meta_data)
        self.rename_chain(list(self.fk_chain), purpose=cfg.FK, **meta_data)
        self.rename_chain(list(self.ik_chain), purpose=cfg.IK, **meta_data)
