from functools import wraps
from six import iteritems
import anvil.runtime as rt
import anvil


def verify_chain_integrity(function):
    @wraps(function)
    def wrapper(self, *args, **kwargs):
        if not rt.dcc.scene.exists(self.top_node):
            raise MemoryError('Reference %s to top node does not exist anymore...' % self.top_node)
        return function(self, *args, **kwargs)

    return wrapper


class HierarchyChain(object):
    def __init__(self, top_node, node_filter=None):
        self.top_node = anvil.factory(top_node)
        self.node_filter = self._default_filter(node_filter=node_filter)
        self.end_node = anvil.factory(self.get_end())

    @verify_chain_integrity
    def verify_chain(self):
        current_node = self.end_node
        while current_node.get_parent():
            if current_node == self.top_node:
                return True
            current_node = current_node.get_parent()
        raise IndexError('Could not find %s in parent hierarchy of last node %s' % (self.top_node, self.end_node))

    @verify_chain_integrity
    def get_end(self, node_filter=None):
        """ Returns the last item found of type
        """
        node_filter = node_filter or self.node_filter
        depth = self.depth(d=self.get_hierarchy(node_filter=node_filter)) - 1
        last_node = self.get_level(depth, node_filter=node_filter)
        if last_node:
            return anvil.factory(list(last_node)[0])
        else:
            raise ValueError('Could not find last node at depth %d' % depth)

    @verify_chain_integrity
    def get_hierarchy(self, node_filter=None):
        node_filter = node_filter or self.node_filter
        return rt.dcc.scene.node_hierarchy_as_dict(str(self.top_node), node_filter=node_filter)

    def _default_filter(self, node_filter=None):
        return rt.dcc.scene.get_type(self.top_node) if node_filter is None else node_filter

    @verify_chain_integrity
    def get_level(self, desired_level, traversal=None, level_tree=None, node_filter=None):
        """ Returns a dictionary at depth "desired_level" from the hierarchy.
            Returns {} if nothing is found at that depth.
        """
        node_filter = node_filter or self.node_filter
        if level_tree is None:
            self.level = 0
            level_tree = {}
        traversal = self.get_hierarchy(node_filter=node_filter) if traversal is None else traversal

        for k, v in iteritems(traversal):
            if self.level > desired_level:
                pass
            elif self.level == desired_level:
                level_tree.update({k: v})
            else:
                self.level += 1
                self.get_level(desired_level, traversal=v, level_tree=level_tree, node_filter=node_filter)
                self.level -= 1

        return level_tree

    @verify_chain_integrity
    def depth(self, d=None, level=0, node_filter=None):
        """ Returns maximum depth of the hierarchy
        """
        node_filter = node_filter or self.node_filter
        if d is None:
            d = self.get_hierarchy(node_filter=node_filter)

        if not isinstance(d, dict) or not d:
            return level
        return max(self.depth(d[k], level + 1) for k in d)

    def __str__(self):
        return self.top_node
