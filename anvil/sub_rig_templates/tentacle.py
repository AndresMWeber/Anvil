from base_sub_rig_template import SubRigTemplate


class Tentacle(SubRigTemplate):
    BUILT_IN_META_DATA = SubRigTemplate.BUILT_IN_META_DATA.merge({'name': 'tentacle'}, new=True)
