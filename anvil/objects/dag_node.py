import anvil.runtime as rt
import unicode_delegate as unicode_delegate


class DagNode(unicode_delegate.UnicodeDelegate):
    def rename(self, new_name):
        return rt.dcc.scene.rename(self.name(), new_name)

    def buffer_connect(self, attribute, other_attribute, buffer_value, **kwargs):
        pma = rt.dcc.create.create_node('plusMinusAverage')
        getattr(self, attribute).connect(pma.input1D[0])
        pma.input1D[1].set(buffer_value)
        pma.output1D.connect(other_attribute, **kwargs)
