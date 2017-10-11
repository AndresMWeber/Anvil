import node_types as node_types
import dag_node
import anvil.runtime as runtime


@node_types.register_node
class Transform(dag_node.DagNode):
    dcc_type = 'transform'

    def get_parent(self):
        try:
            self.getParent()
        except TypeError:
            runtime.dcc.scene.list_relatives(self._dcc_id, parent=True)