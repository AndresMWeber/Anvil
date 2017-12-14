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

