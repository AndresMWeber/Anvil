from base_sub_rig_template import SubRigTemplate


class Eye(SubRigTemplate):
    BUILT_IN_META_DATA = SubRigTemplate.BUILT_IN_META_DATA.merge({'name': 'eye'}, new=True)

