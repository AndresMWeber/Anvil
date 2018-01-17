from base import SubRigTemplate


class QuadrupedLeg(SubRigTemplate):
    BUILT_IN_META_DATA = SubRigTemplate.BUILT_IN_META_DATA.merge({'name': 'quadleg'}, new=True)

