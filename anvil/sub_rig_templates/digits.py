import anvil.config as cfg
from anvil.meta_data import MetaData
from limb import Limb


class Digit(Limb):
    BUILT_IN_NAME_TOKENS = MetaData({"name": "finger"}, Limb.BUILT_IN_NAME_TOKENS)

    def __init__(self, *args, **kwargs):
        """ General class for the digit of a Plantigrade animal.  Assumes X axis is down.
        """
        super(Digit, self).__init__(*args, **kwargs)

    def build(self, parent=None, use_layout=True, build_ik=True, build_fk=True, meta_data=None, **kwargs):
        super(Limb, self).build(meta_data=meta_data, parent=parent, **kwargs)

        # Build IK/FK chains from the initial layout joints
        if build_fk:
            self.LOG.info('Building FK chain on %r from layout joints %r.' % (self, self.layout_joints))
            self.build_kwargs['shape'] = 'pyramid_pin'
            self.build_fk_chain(self.layout_joints, **self.build_kwargs)

        if build_ik:
            self.LOG.info('Building IK chain on %r from layout joints %r.' % (self, self.layout_joints))
            self.build_kwargs['shape'] = 'cube'
            self.build_ik_chain(self.layout_joints, **self.build_kwargs)

        self.build_blend_chain(self.layout_joints, use_layout=use_layout, **self.build_kwargs)
        self.rename()

    def connect_curl_fist(self, control, axis=cfg.X):
        phalanges = self.fk_chain if hasattr(self, '%s_chain' % cfg.FK) else self.blend_chain
        control.add_attr('curl', defaultValue=0, attributeType=cfg.FLOAT)
        for phalanges in phalanges[:-1]:
            pass

    def connect_spread(self, control, axis=cfg.Y):
        pass
