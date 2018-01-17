from base import SubRigTemplate


class QuadrupedArm(SubRigTemplate):
    BUILT_IN_META_DATA = SubRigTemplate.BUILT_IN_META_DATA.merge({'name': 'quadarm'}, new=True)

