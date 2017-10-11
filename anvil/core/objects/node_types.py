import sys

REGISTERED_NODES = {}


def register_node(node_class):
    # setattr(sys.modules[__name__], node_class.__name__, node_class)
    REGISTERED_NODES[node_class.__name__] = node_class
    return node_class


from joint import Joint
from transform import Transform
from unicode_delegate import UnicodeDelegate
from dag_node import DagNode
from curve import Curve
from control import Control
