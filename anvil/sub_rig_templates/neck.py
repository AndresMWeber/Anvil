from base import SubRigTemplate


class Neck(SubRigTemplate):
    BUILT_IN_META_DATA = SubRigTemplate.BUILT_IN_META_DATA.merge({'name': 'neck'}, new=True)

