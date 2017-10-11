import node_types as node_types
import transform


@node_types.register_node
class Joint(transform.Transform):
    dcc_type = 'joint'

