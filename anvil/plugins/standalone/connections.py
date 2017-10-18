import anvil.plugins.base.connections as attribute


class Attribute(attribute.Attribute):
    def get(self, object, attr):
        return getattr(object, attr)

    def set(self, object, attr, value):
        return setattr(object, attr, value)


class Constraint(attribute.Constraint):
    def translate(self, source, targets, **flags):
        return True

    def rotate(self, source, targets, **flags):
        return True

    def aim(self, source, targets, **flags):
        return True

    def scale(self, source, targets, **flags):
        return True

    def parent(self, source, targets, **flags):
        return True

    def tangent(self, source, targets, **flags):
        return True

    def geometry_point(self, source, targets, **flags):
        return True

    def geometry_normal(self, source, targets, **flags):
        return True

    def pole_vector(self, source, targets, **flags):
        return True

