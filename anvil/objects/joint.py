import anvil.config as cfg
import anvil.runtime as rt
import transform


class Joint(transform.Transform):
    dcc_type = cfg.JOINT_TYPE

    @staticmethod
    def create_engine_instance(**flags):
        return rt.dcc.create.create_joint(**flags)
