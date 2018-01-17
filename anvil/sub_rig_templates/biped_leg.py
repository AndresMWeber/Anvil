from limb import Limb


class BipedLeg(Limb):
    BUILT_IN_META_DATA = Limb.BUILT_IN_META_DATA.merge({'name': 'leg'}, new=True)
