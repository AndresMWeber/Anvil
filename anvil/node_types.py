from objects import *
from grouping import *

REGISTERED_NODES = {}


def register_node(node_class):
    REGISTERED_NODES[node_class.__name__] = node_class
    return node_class


__all__ = ['SubRig', 'Rig', 'Control', 'Curve', 'DagNode', 'UnicodeDelegate', 'Transform', 'Joint']
