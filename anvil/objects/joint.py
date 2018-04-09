import anvil.config as cfg
import anvil.runtime as rt
from transform import Transform


class Joint(Transform):
    DCC_TYPE = cfg.JOINT_TYPE
    ANVIL_TYPE = cfg.JOINT_TYPE
    BUILT_IN_META_DATA = Transform.BUILT_IN_META_DATA.merge({cfg.TYPE: cfg.JOINT_TYPE}, force=True, new=True)

    @staticmethod
    def create_engine_instance(**kwargs):
        return rt.dcc.create.create_joint(**kwargs)
