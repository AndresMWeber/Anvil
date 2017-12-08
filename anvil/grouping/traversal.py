from functools import wraps
from six import iteritems
import anvil.runtime as rt
import anvil
import nomenclate.core.tools as ts


class HierarchyChain(object):
    def __init__(self, top_node, end_node=None, duplicate=False, node_filter=None, parent=None):
        top_node = self._resolve_root(top_node)

        if isinstance(top_node, self.__class__):
            top_node, end_node = top_node.root, top_node.end

        if duplicate:
            duplicate_kwargs = {'renameChildren': True, 'upstreamNodes': False}
            top_node, end_node = str(rt.dcc.scene.duplicate(top_node, **duplicate_kwargs)[0]), None

        self.root = anvil.factory(top_node)

        self.node_filter = self._get_default_filter_type(node_filter=node_filter)
        self.end = end_node
        self.set_end(end_node=end_node)
        self.parent(parent)

    def _resolve_root(self, root_candidate):
        return root_candidate[0] if isinstance(root_candidate, list) else root_candidate

    @property
    def mid(self):
        """ Should only be used with non-branching chains as it will create false positives.
        """
        return self.get_hierarchy_as_list()[self.depth() / 2]

    def set_end(self, end_node=None, node_filter=None):
        """ Returns the last item found of type
        """
        try:
            self.end = anvil.factory(end_node)
        except (RuntimeError, IOError):
            self.end = self.get_linear_end(node_filter=node_filter)

    def get_linear_end(self, node_filter=None):
        node_filter = node_filter or self.node_filter
        last_node = self.get_level(self.depth(), node_filter=node_filter)
        if last_node:
            return anvil.factory(list(last_node)[0])
        else:
            raise ValueError('Could not find last node at depth %d' % self.depth())

    def get_hierarchy(self, node_filter=None):
        node_filter = node_filter or self.node_filter
        return rt.dcc.scene.node_hierarchy_as_dict(self.root, node_filter=node_filter)

    def get_hierarchy_as_list(self, node_filter=None):
        return self._flatten_dict_keys(self.get_hierarchy(node_filter=node_filter))

    def _get_default_filter_type(self, node_filter=None):
        if self.root and node_filter:
            return rt.dcc.scene.get_type(self.root) if node_filter is None else node_filter
        else:
            return node_filter or []

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

    def build_ik(self, chain_start=None, chain_end=None, solver='ikRPsolver', **kwargs):
        chain_start = chain_start if chain_start is not None else self.root
        chain_end = chain_end if chain_end is not None else self.end

        kwargs.update({'endEffector': str(chain_end), 'solver': solver})
        handle, effector = rt.dcc.rigging.ik_handle(str(chain_start), **kwargs)
        return (anvil.factory(handle), anvil.factory(effector))

    def parent(self, new_parent):
        top_node, new_parent = str(self.root), str(new_parent)
        nodes_exist = [rt.dcc.scene.exists(node) if node != 'None' else False for node in [top_node, new_parent]]
        if all(nodes_exist or [False]):
            rt.dcc.scene.parent(top_node, new_parent)
            return True
        else:
            return False

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

    def __iter__(self):
        """ This is setup to only iterate on the nodes in between the top node and the end node
            ignores branching paths
        """
        current_node = self.end
        chain_path = [current_node]

        while anvil.factory(current_node).get_parent():
            current_node = anvil.factory(current_node.get_parent())
            chain_path.insert(0, current_node)
            if current_node == self.root:
                return iter(chain_path)

        raise IndexError('Could not find %s in parent hierarchy with last node %s' % (self.root, self.end))

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
        return str(self.root)

    def __repr__(self):
        return super(HierarchyChain, self).__repr__().replace('>',
                                                              '(root=%s, end=%s)>' % (str(self.root), str(self.end)))
