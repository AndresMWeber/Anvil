import anvil.plugins.base.attribute as attribute
from dependencies import *


class Attribute(attribute.Attribute):
    def get(self, object, attr):
        return mc.getAttr(object, attr)

    def set(self, object, attr, value, **flags):
        return mc.setAttr(object, attr, value, **flags)
