import node_types as node_types
import dag_node as dag_node


@node_types.register_node
class Curve(dag_node.DagNode):
    dcc_type = 'curve'

    def __init__(self, name, parent=None, flags=None, metaData=None):
        super(Curve, self).__init__(name, flags=flags, metaData=metaData)
