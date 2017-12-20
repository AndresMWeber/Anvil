import anvil.runtime as rt
import unicode_delegate
import attribute as at
import anvil.config as cfg


class DagNode(unicode_delegate.UnicodeDelegate):

    def buffer_connect(self, attribute, other_attribute, buffer_value, **kwargs):
        pma = rt.dcc.create.create_node(cfg.ADD_SUB_TYPE)
        self.attr(attribute).connect(pma.input1D[0])
        pma.input1D[1].set(buffer_value)
        pma.output1D.connect(other_attribute, **kwargs)

    def _resolve_attribute_name(self, attribute_name):
        return '%s%s%s' % (self, cfg.ATTR_DELIMITER, attribute_name)

    def add_attr(self, attribute, **kwargs):
        rt.dcc.connections.add_attr(self, longName=attribute, **kwargs)
        return at.Attribute(self._resolve_attribute_name(attribute))

    def get_attr(self, attribute, **kwargs):
        return self.attr(attribute).get(**kwargs)

    def attr(self, attribute):
        return at.Attribute(self._resolve_attribute_name(attribute))

    def connect_attr(self, attribute_source, attribute_destination, **kwargs):
        self.attr(attribute_source).connect(at.Attribute(attribute_destination), **kwargs)

    def colorize(self, color):
        self.attr(cfg.OVERRIDE_ENABLED).set(True)
        if isinstance(color, list) and len(color) == 3:
            self.attr(cfg.OVERRIDE_RGB).set(True)
        self.attr(cfg.OVERRIDE_COLOR).set(color)

    def __getattr__(self, item):
        if item in rt.dcc.connections.list_attr(self):
            return at.Attribute('%s.%s' % (self, item))
        else:
            return super(DagNode, self).__getattr__(item)
