from six import iteritems
import inspect
from objects import *  # noqa
from grouping import *  # noqa

REGISTERED_NODES = {}


def register_node(node_class):
    REGISTERED_NODES[node_class.__name__] = node_class
    return node_class


for imported_class in list(set([v for k, v in iteritems(globals().copy()) if inspect.isclass(v)])):
    register_node(imported_class)

__all__ = ['AbstractGrouping',
           'SubRig',
           'Rig',
           'NodeRelationshipSet',
           'LinearHierarchyNodeSet',
           'NonLinearHierarchyNodeSet',
           'Control',
           'UnicodeDelegate',
           'DagNode',
           'Transform',
           'Curve',
           'Joint']
