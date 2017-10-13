import node_types as node_types
import unicode_delegate as unicode_delegate
import anvil.runtime as runtime


@node_types.register_node
class DagNode(unicode_delegate.UnicodeDelegate):
    def rename(self, new_name):
        return runtime.dcc.scene.rename(self._dcc_id, new_name)

    def name(self):
        return self._dcc_id

    def __repr__(self):
        if hasattr(self, '__str__'):
            return '<%s @ 0x%x (%s)>' % (self.__class__.__name__, id(self), str(self))
        else:
            return '<%s @ 0x%x>' % (self.__class__.__name__, id(self))

    def __str__(self):
        return str(self.name())