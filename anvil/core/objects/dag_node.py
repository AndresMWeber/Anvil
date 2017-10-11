import node_types as node_types
import unicode_delegate as unicode_delegate


@node_types.register_node
class DagNode(unicode_delegate.UnicodeDelegate):
    pass
