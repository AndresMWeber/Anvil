from base import SubRigTemplate


class Eye(SubRigTemplate):
    BUILT_IN_META_DATA = SubRigTemplate.BUILT_IN_META_DATA.merge({'name': 'eye'}, new=True)

