from limb import Limb


class BirdWing(Limb):
    BUILT_IN_META_DATA = Limb.BUILT_IN_META_DATA.merge({'name': 'wing'}, new=True)
