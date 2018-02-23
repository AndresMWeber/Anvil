from base import SubRigTemplate
import anvil.config as cfg


class Limb(SubRigTemplate):
    BUILT_IN_META_DATA = SubRigTemplate.BUILT_IN_META_DATA.merge({'name': 'limb'}, new=True)

    def __init__(self, *args, **kwargs):
        super(Limb, self).__init__(*args, **kwargs)
        self.blend_chain = []
        self.fk_chain = []
        self.ik_chain = []

    def build(self, parent=None, use_layout=True, build_ik=True, build_fk=True, meta_data=None, **kwargs):
        super(Limb, self).build(meta_data=meta_data, parent=parent, **kwargs)
        if build_fk:
            fk_results = self.build_fk_chain(self.layout_joints, **self.build_kwargs)

        if build_ik:
            ik_results = self.build_ik_chain(self.layout_joints, **self.build_kwargs)
        from pprint import pprint
        pprint(fk_results)
        pprint(ik_results)
        if build_fk and build_ik:
            blend_results = self.build_blend_chain(self.layout_joints,
                                                   [fk_results[cfg.JOINT_TYPE], ik_results[cfg.JOINT_TYPE]],
                                                   use_layout=use_layout, **self.build_kwargs)
        self.rename()

    def rename(self, *input_dicts, **name_tokens):
        super(Limb, self).rename(*input_dicts, **name_tokens)

        joint_chain_meta_data = self.meta_data + {cfg.TYPE: cfg.JOINT_TYPE, cfg.PURPOSE: cfg.BLEND}
        self.rename_chain(list(self.blend_chain), **joint_chain_meta_data)

        joint_chain_meta_data[cfg.PURPOSE] = cfg.FK
        self.rename_chain(list(self.fk_chain), **joint_chain_meta_data)

        joint_chain_meta_data[cfg.PURPOSE] = cfg.IK
        self.rename_chain(list(self.ik_chain), **joint_chain_meta_data)
