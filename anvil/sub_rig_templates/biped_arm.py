from limb import Limb


class BipedArm(Limb):
    BUILT_IN_META_DATA = Limb.BUILT_IN_META_DATA.merge({'name': 'arm'}, new=True)
