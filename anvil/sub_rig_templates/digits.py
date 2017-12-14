import anvil
from anvil.meta_data import MetaData
from six import iteritems
from limb import Limb


class Digit(Limb):
    BUILT_IN_META_DATA = MetaData.merge_dicts({"name": "finger"}, Limb.BUILT_IN_META_DATA)
    CONTROLLER_ATTRIBUTES = {
        "curl": None,
        "spread": None,
        "fkik": None,
    }

    def __init__(self, *args, **kwargs):
        """ General class for the digit of a Plantigrade animal.  Assumes X axis is down.
        """
        super(Digit, self).__init__(*args, **kwargs)

    def hook_up_attribute_controls(self, controller):
        controller = anvil.factory(controller)
        for attr, attr_kwargs in iteritems(self.CONTROLLER_ATTRIBUTES):
            controller.add_attr(attr, **attr_kwargs)

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