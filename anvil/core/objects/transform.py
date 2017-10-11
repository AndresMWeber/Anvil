import node_types as node_types
import dag_node
import anvil.runtime as runtime


@node_types.register_node
class Transform(dag_node.DagNode):
    dcc_type = 'transform'

    def __init__(self, name, parent=None, flags=None, meta_data=None):
        super(Transform, self).__init__(name, flags=flags, meta_data=meta_data)
        self.__pynode__ = None

    def get_parent(self):
        try:
            self.__pynode__.getParent()
        except TypeError:
            runtime.dcc.scene.list_relatives(self._dcc_id, parent=True)