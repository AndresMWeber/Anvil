from api_proxy import APIProxy


class Attribute(APIProxy):
    def get(self, object, attr):
        raise NotImplementedError

    def set(self, object, attr, value):
        raise NotImplementedError


class Constraint(APIProxy):
    def translate(self, source, targets, **flags):
        raise NotImplementedError

    def rotate(self, source, targets, **flags):
        raise NotImplementedError

    def aim(self, source, targets, **flags):
        raise NotImplementedError

    def scale(self, source, targets, **flags):
        raise NotImplementedError

    def parent(self, source, targets, **flags):
        raise NotImplementedError

    def tangent(self, source, targets, **flags):
        raise NotImplementedError

    def geometry_point(self, source, targets, **flags):
        raise NotImplementedError

    def geometry_normal(self, source, targets, **flags):
        raise NotImplementedError

    def pole_vector(self, source, targets, **flags):
        raise NotImplementedError
