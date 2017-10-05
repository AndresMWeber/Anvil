import node_types as node_types
import dag_node


@node_types.register_node
class Transform(dag_node.DagNode):
    dcc_type = 'transform'

    def __init__(self, name, parent=None, flags=None, metaData=None):
        super(Transform, self).__init__(name, flags=flags, metaData=metaData)
