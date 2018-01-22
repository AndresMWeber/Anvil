import anvil.config as cfg
import anvil.runtime as rt
import transform
from anvil.meta_data import MetaData


class Joint(transform.Transform):
    dcc_type = cfg.JOINT_TYPE
    BUILTIN_NAME_TOKENS = MetaData({cfg.TYPE: dcc_type}, protected=cfg.TYPE)

    @staticmethod
    def create_engine_instance(**kwargs):
        return rt.dcc.create.create_joint(**kwargs)
