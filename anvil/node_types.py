from six import iteritems
import inspect
import anvil
from objects import * # noqa
from grouping import * # noqa

REGISTERED_NODES = {}


def register_node(node_class):
    anvil.LOG.debug('Registering Anvil node type %s', node_class)
    REGISTERED_NODES[node_class.__name__] = node_class
    return node_class


for imported_class in list(set([v for k, v in iteritems(globals().copy()) if inspect.isclass(v)])):
    register_node(imported_class)

anvil.LOG.info('Registered all object classes in anvil.node_types: %s', list(REGISTERED_NODES))

__all__ = ['AbstractGrouping',
           'SubRig',
           'Rig',
           'NonLinearHierarchyNodeSet',
           'LinearHierarchyNodeSet'
           'Control',
           'UnicodeDelegate',
           'DagNode',
           'Transform',
           'Curve',
           'Joint']
