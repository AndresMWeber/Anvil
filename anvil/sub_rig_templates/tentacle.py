from base import SubRigTemplate


class Tentacle(SubRigTemplate):
    BUILT_IN_META_DATA = SubRigTemplate.BUILT_IN_META_DATA.merge({'name': 'tentacle'}, new=True)

