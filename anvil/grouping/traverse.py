from functools import wraps
from six import iteritems
import anvil.runtime as rt
import anvil
import nomenclate.core.tools as ts


def verify_chain_integrity(function):
    @wraps(function)
    def wrapper(self, *args, **kwargs):
        if not rt.dcc.scene.exists(self.root):
            raise MemoryError('Reference %s to top node does not exist anymore...' % self.top_node)
        return function(self, *args, **kwargs)

    return wrapper


class HierarchyChain(object):
    def __init__(self, top_node, end_node=None, node_filter=None):
        self.root = anvil.factory(top_node)
        self.node_filter = self._default_filter(node_filter=node_filter)
        self.end = end_node
        self.set_end()

    @verify_chain_integrity
    def set_end(self, end_node=None, node_filter=None):
        """ Returns the last item found of type
        """
        node_filter = node_filter or self.node_filter
        try:
            self.end = anvil.factory(end_node)
        except RuntimeError:
            last_node = self.get_level(self.depth(), node_filter=node_filter)
            if last_node:
                self.end = anvil.factory(list(last_node)[0])
            else:
                raise ValueError('Could not find last node at depth %d' % self.depth())

    @verify_chain_integrity
    def get_hierarchy(self, node_filter=None):
        node_filter = node_filter or self.node_filter
        return rt.dcc.scene.node_hierarchy_as_dict(self.root, node_filter=node_filter)

    def get_hierarchy_as_list(self, node_filter=None):
        return self._flatten_dict_keys(self.get_hierarchy(node_filter=node_filter))

    def _default_filter(self, node_filter=None):
        return rt.dcc.scene.get_type(self.root) if node_filter is None else node_filter

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

    def depth(self, node_filter=None):
        node_filter = node_filter or self.node_filter
        return self._dict_depth(d=self.get_hierarchy(node_filter=node_filter)) - 1

    def _dict_depth(self, d=None, level=0, node_filter=None):
        """ Returns maximum depth of the hierarchy
        """
        node_filter = node_filter or self.node_filter
        if d is None:
            d = self.get_hierarchy(node_filter=node_filter)

        if not isinstance(d, dict) or not d:
            return level
        return max(self._dict_depth(d[k], level + 1) for k in d)

    def _flatten_dict_keys(self, d, keys=None):
        keys = keys if keys is not None else []
        if isinstance(d, dict):
            for k, v in iteritems(d):
                keys.append(k)
                self._flatten_dict_keys(v, keys)
        else:
            keys.append(d)
        return keys

    @verify_chain_integrity
    def __iter__(self):
        """ This is setup to only iterate on the nodes in between the top node and the end node
            ignores branching paths
        """
        current_node = self.end
        chain_path = [current_node]
        while current_node.get_parent():
            current_node = anvil.factory(current_node.get_parent())
            chain_path.insert(0, current_node)
            if current_node == self.root:
                return iter(chain_path)

        raise IndexError('Could not find %s in parent hierarchy of last node %s' % (self.root, self.end))

    def __contains__(self, item):
        return str(item) in [str(n) for n in ts.flatten(self.get_hierarchy())]

    def __getitem__(self, key):
        if isinstance(key, int):
            return list(self)[key]
        else:
            def gen_matches(key, dictionary):
                for k, v in iteritems(dictionary):
                    if k == key:
                        return {k: v}
                    elif isinstance(v, dict):
                        return gen_matches(key, v)

            return gen_matches(key, self.get_hierarchy())

    def __len__(self):
        return len(list(iter(self)))

    def __str__(self):
        return self.root
