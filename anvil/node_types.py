import anvil
from objects import *
from grouping import *
anvil.LOG.info('Registered all object classes in anvil.node_types')
REGISTERED_NODES = {}


def register_node(node_class):
    REGISTERED_NODES[node_class.__name__] = node_class
    return node_class

__all__ = ['SubRig', 'Rig', 'Control', 'UnicodeDelegate', 'DagNode', 'Transform', 'Curve', 'Joint']
