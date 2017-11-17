from six import iteritems
import inspect
import anvil
from objects import *
from grouping import *

import grouping
print(dir(grouping))
g = globals().copy()
anvil.LOG.info('Registered all object classes in anvil.node_types: %s' % [k for k, v in iteritems(g) if
                                                                          inspect.isclass(v)])
REGISTERED_NODES = {}


def register_node(node_class):
    REGISTERED_NODES[node_class.__name__] = node_class
    return node_class


__all__ = ['AbstractGrouping',
           'SubRig',
           'Rig',
           'Control',
           'UnicodeDelegate',
           'DagNode',
           'Transform',
           'Curve',
           'Joint']
