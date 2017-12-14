from six import iteritems
import anvil.runtime as rt
import anvil
import anvil.config as cfg
import nomenclate.core.tools as ts


class HierarchyChain(object):
    def __init__(self, top_node, end_node=None, duplicate=False, node_filter=None, parent=None):
        self.node_filter = self._get_default_filter_type(node_filter=node_filter)
        top_node, end_node = self._process_top_node(top_node, end_node, duplicate=duplicate)
        self.head = top_node
        self.tail = self._process_end_node(end_node)
        self.parent(parent)

    def _process_top_node(self, top_node, end_node, duplicate=False):
        if isinstance(top_node, list) and end_node is None:
            top_node, end_node = top_node[0], top_node[-1]

        elif isinstance(top_node, self.__class__):
            top_node, end_node = top_node.head, top_node.tail

        if duplicate:
            top_node, end_node = self.duplicate_chain(top_node, end_node=end_node)

        return anvil.factory(top_node), end_node

    @property
    def mid(self):
        """ Should only be used with non-branching chains as it will create false positives.
        """
        return self.get_hierarchy_as_list()[self.depth() / 2]

    def _process_end_node(self, end_node_candidate, node_filter=None):
        """ Returns the last item found of type
        """
        try:
            return anvil.factory(end_node_candidate)
        except (RuntimeError, IOError):
            return self._get_linear_end(node_filter=node_filter)

    def get_hierarchy(self, node_filter=None):
        node_filter = node_filter or self.node_filter
        return rt.dcc.scene.node_hierarchy_as_dict(self.head, node_filter=node_filter)

    def get_hierarchy_as_list(self, node_filter=None):
        return self._flatten_dict_keys(self.get_hierarchy(node_filter=node_filter))

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

    def build_ik(self, chain_start=None, chain_end=None, solver=cfg.IK_RP_SOLVER, parent=None, **kwargs):
        chain_start = chain_start if chain_start is not None else self.head
        chain_end = chain_end if chain_end is not None else self.tail

        kwargs.update({'endEffector': str(chain_end), 'solver': solver})
        handle, effector = rt.dcc.rigging.ik_handle(str(chain_start), **kwargs)
        if parent:
            rt.dcc.scene.parent(handle, parent)

        return (anvil.factory(handle), anvil.factory(effector))

    def parent(self, new_parent):
        top_node, new_parent = str(self.head), str(new_parent)
        nodes_exist = [rt.dcc.scene.exists(node) if node != 'None' else False for node in [top_node, new_parent]]
        if all(nodes_exist or [False]):
            rt.dcc.scene.parent(top_node, new_parent)
            return True
        else:
            return False

    def duplicate_chain(self, top_node, end_node=None):
        """ Duplicates a chain and respects the end node by duplicating and reparenting the entire chain
        :param top_node:
        :param end_node:
        :return:
        """
        duplicate_kwargs = {'renameChildren': True, 'upstreamNodes': False, 'parentOnly': True}
        if isinstance(top_node, self.__class__):
            nodes = list(top_node)
        else:
            try:
                nodes = list(self._traverse_up_linear_tree(end_node, top_node))
            except (IndexError, IOError):
                # This is the case if no end was specified so we will duplicate the entire chain.
                nodes = top_node
                duplicate_kwargs.pop('parentOnly')
        anvil.LOG.info('Duplicating chain %s from %s->%s, kwargs: %s' % (nodes, top_node, end_node, duplicate_kwargs))
        duplicates = rt.dcc.scene.duplicate(nodes, **duplicate_kwargs)
        anvil.LOG.info('Duplicates of %s are %s' % (nodes, duplicates))
        if len(duplicates) == 1:
            duplicates = [duplicates[0]] + self._traverse_down_linear_tree(duplicates[0])
        return str(duplicates[0]), str(duplicates[-1])

    def _traverse_up_linear_tree(self, downstream_node, upstream_node):
        all_descendants = self._traverse_down_linear_tree(upstream_node)
        if not str(downstream_node) in all_descendants:
            raise IndexError('Node %r is not in the descendants of %s --> %s' % (downstream_node,
                                                                                 upstream_node,
                                                                                 all_descendants))

        current_node = anvil.factory(downstream_node)
        chain_path = [current_node]

        while anvil.factory(current_node).get_parent():
            current_node = anvil.factory(current_node.get_parent())
            chain_path.insert(0, current_node)
            if current_node == upstream_node:
                return iter(chain_path)
        raise IndexError('Could not find path between start(%s) --> last(%s)' % (downstream_node, upstream_node))

    def _get_default_filter_type(self, node_filter=None):
        try:
            default_type = rt.dcc.scene.get_type(self.head)
        except AttributeError:
            default_type = []
        return node_filter or default_type

    def _get_linear_end(self, node_filter=None):
        node_filter = node_filter or self.node_filter
        last_node = self.get_level(self.depth(), node_filter=node_filter)
        if last_node:
            return anvil.factory(list(last_node)[0])
        else:
            raise ValueError('Could not find last node at depth %d' % self.depth())

    def _dict_depth(self, d=None, level=0, node_filter=None):
        """ Returns maximum depth of the hierarchy
        """
        node_filter = node_filter or self.node_filter
        if d is None:
            d = self.get_hierarchy(node_filter=node_filter)

        if not isinstance(d, dict) or not d:
            return level
        return max(self._dict_depth(d[k], level + 1) for k in d)

    @classmethod
    def _flatten_dict_keys(cls, d, keys=None):
        keys = keys if keys is not None else []
        if isinstance(d, dict):
            for k, v in iteritems(d):
                keys.append(k)
                cls._flatten_dict_keys(v, keys)
        else:
            keys.append(d)
        return keys

    def _traverse_down_linear_tree(self, start):
        relatives_kwargs = {'allDescendents': True, 'children': True}
        if self.node_filter:
            relatives_kwargs['type'] = self.node_filter
        return list(reversed(rt.dcc.scene.list_relatives(start, **relatives_kwargs)))

    def __iter__(self):
        """ This is setup to only iterate on the nodes in between the top node and the end node
            ignores branching paths
        """
        return self._traverse_up_linear_tree(self.tail, self.head)

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
        return str(self.head)

    def __repr__(self):
        return super(HierarchyChain, self).__repr__().replace('>',
                                                              '(root=%s, end=%s)>' % (str(self.head), str(self.tail)))
