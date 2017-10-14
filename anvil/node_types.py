import anvil
from objects import *
anvil.LOG.info('Imported objects')
from grouping import *
anvil.LOG.info('Imported groupings')
anvil.LOG.info('Imported all nodes %s' % list(locals()))
REGISTERED_NODES = {}


def register_node(node_class):
    REGISTERED_NODES[node_class.__name__] = node_class
    return node_class

__all__ = ['SubRig', 'Rig', 'Control', 'UnicodeDelegate', 'DagNode', 'Transform', 'Curve', 'Joint']
