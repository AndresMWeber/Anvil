class Attribute(object):
    def get(self, object, attr):
        raise NotImplementedError

    def set(self, object, attr, value):
        raise NotImplementedError
