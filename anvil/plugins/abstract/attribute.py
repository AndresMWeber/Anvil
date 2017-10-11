class Attribute(object):
    def get(self, object, attr):
        return getattr(object, attr)

    def set(self, object, attr, value):
        return setattr(object, attr, value)
