import anvil.runtime as rt
import unicode_delegate
import attribute
import anvil.config as cfg

class DagNode(unicode_delegate.UnicodeDelegate):

    def buffer_connect(self, attribute, other_attribute, buffer_value, **kwargs):
        pma = rt.dcc.create.create_node('plusMinusAverage')
        getattr(self, attribute).connect(pma.input1D[0])
        pma.input1D[1].set(buffer_value)
        pma.output1D.connect(other_attribute, **kwargs)

    def _resolve_attribute_name(self, attribute_name):
        return '%s%s%s' % (self, cfg.ATTR_DELIMITER, attribute_name)

    def add_attr(self, attribute, **kwargs):
        attr_name = self._resolve_attribute_name(attribute)
        rt.dcc.connections.add_attr(attr_name, **kwargs)
        return attribute.Attribute(attr_name)

    def get_attr(self, attribute, **kwargs):
        return self.attr(attribute).get(**kwargs)

    def attr(self, attribute):
        return attribute.Attribute(self._resolve_attribute_name(attribute))

    def connect_attr(self, attribute_source, attribute_destination, **kwargs):
        self.attr(attribute_source).connect(attribute.Attribute(attribute_destination), **kwargs)

    def __getattr__(self, item):
        if item in rt.dcc.connections.list_attr(self):
            return attribute.Attribute('%s.%s' % (self, item))
        else:
            return super(DagNode, self).__getattr__(item)
