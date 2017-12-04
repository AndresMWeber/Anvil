import anvil.runtime as rt
import unicode_delegate as unicode_delegate


class DagNode(unicode_delegate.UnicodeDelegate):
    def rename(self, new_name):
        return rt.dcc.scene.rename(self.name(), new_name)

    def name(self):
        return str(self._dcc_id)

    def buffer_connect(self, attribute, other_attribute, buffer_value, **kwargs):
        pma = rt.dcc.create.create_node('plusMinusAverage')
        getattr(self, attribute).connect(pma.input1D[0])
        pma.input1D[1].set(buffer_value)
        pma.output1D.connect(other_attribute, **kwargs)

    def __repr__(self):
        if hasattr(self, '__str__'):
            return '<%s @ 0x%x (%s)>' % (self.__class__.__name__, id(self), str(self))
        else:
            return '<%s @ 0x%x>' % (self.__class__.__name__, id(self))

    def __str__(self):
        return str(self.name())

    def __eq__(self, other):
        return str(self) == str(other)
