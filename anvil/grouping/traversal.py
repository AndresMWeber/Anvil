from six import iteritems
import nomenclate.core.tools as ts
import anvil
import anvil.log as log
import anvil.config as cfg
import anvil.runtime as rt
import anvil.objects as ob
import anvil.utils.generic as gc
import anvil.utils.scene as sc

class HierarchyChain(log.LogMixin):
    LOG = log.obtainLogger(__name__)
    UP = 'up'
    DOWN = 'down'

    def __init__(self, top_node, end_node=None, duplicate=False, node_filter=None, parent=None):
        self.node_filter = self._get_default_filter_type(node_filter=node_filter)
        top_node, end_node = self._process_top_node(top_node, end_node, duplicate=duplicate)
        self.head = top_node
        self.tail = self._process_end_node(end_node)
        self.parent(parent)

    @property
    def mid(self):
        """ Should only be used with non-branching chains as it will create false positives.
        """
        return self.get_hierarchy(as_list=True)[self.depth() / 2]

    def find_child(self, child):
        if isinstance(child, int):
            return self[child]

        child = anvil.factory(child)
        for node in self:
            if node == child:
                return node

        raise IndexError('Child not found in hierarchy %s' % list(self))

    def get_hierarchy(self, node_filter=None, as_list=False):
        hierarchy = sc.get_node_hierarchy_as_dict(self.head, node_filter=node_filter or self.node_filter)
        if as_list:
            hierarchy = gc.dict_to_keys_list(hierarchy)
        return hierarchy

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

    def insert_buffer(self, index_target, buffer_node_class=None, direction=None, **kwargs):
        index_target = self.find_child(index_target)

        direction = self.UP if direction is None else direction if direction in [self.UP, self.DOWN] else self.UP
        buffer_node_class = ob.Transform if not anvil.is_anvil(buffer_node_class) else buffer_node_class

        buffer = buffer_node_class.build(**kwargs)
        buffer_parent = index_target.get_parent() if direction == self.UP else index_target

        buffer.match_position(buffer_parent)
        buffer.parent(buffer_parent)

        if direction == self.UP:
            index_target.parent(buffer)
        else:
            for child in index_target.children():
                child.parent(buffer)

    def depth(self, node_filter=None):
        return gc.get_dict_depth(d=self.get_hierarchy(node_filter=node_filter or self.node_filter)) - 1

    def parent(self, new_parent):
        if sc.objects_exist([self.head, new_parent]):
            rt.dcc.scene.parent(self.head, new_parent)
        else:
            self.warning('Tried to parent %s to non existent object %s', self.head, new_parent)

    def duplicate_chain(self, top_node, end_node=None):
        """ Duplicates a chain and respects the end node by duplicating and reparenting the entire chain
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
        self.info('Duplicating chain %s from %s->%s, kwargs: %s', nodes, top_node, end_node, duplicate_kwargs)
        duplicates = rt.dcc.scene.duplicate(nodes, **duplicate_kwargs)
        self.info('Duplicates of %s are %s', nodes, duplicates)
        if len(duplicates) == 1:
            duplicates = [duplicates[0]] + self._traverse_down_linear_tree(duplicates[0])
        return str(duplicates[0]), str(duplicates[-1])

    def build_ik(self, chain_start=None, chain_end=None, solver=cfg.IK_RP_SOLVER, parent=None, **kwargs):
        chain_start = chain_start if chain_start is not None else self.head
        chain_end = chain_end if chain_end is not None else self.tail

        kwargs.update({'endEffector': str(chain_end), 'solver': solver})
        handle, effector = rt.dcc.rigging.ik_handle(str(chain_start), **kwargs)
        if parent:
            rt.dcc.scene.parent(handle, parent)

        return (anvil.factory(handle), anvil.factory(effector))

    def _process_top_node(self, top_node, end_node, duplicate=False):
        if isinstance(top_node, list) and end_node is None:
            top_node, end_node = top_node[0], top_node[-1]

        elif isinstance(top_node, self.__class__):
            top_node, end_node = top_node.head, top_node.tail

        if duplicate:
            top_node, end_node = self.duplicate_chain(top_node, end_node=end_node)

        return anvil.factory(top_node), end_node

    def _process_end_node(self, end_node_candidate, node_filter=None):
        """ Returns the last item found of type
        """
        try:
            return anvil.factory(end_node_candidate)
        except (RuntimeError, IOError):
            return self._get_linear_end(node_filter=node_filter)

    def _traverse_up_linear_tree(self, downstream_node, upstream_node, node_filter=None):
        node_filter = node_filter if node_filter is not None else self.node_filter
        all_descendants = self._traverse_down_linear_tree(upstream_node)
        if not str(downstream_node) in all_descendants:
            raise IndexError('Node %r is a descendant of %s --> %s' % (downstream_node, upstream_node, all_descendants))

        current_node = anvil.factory(downstream_node)
        chain_path = [current_node]

        while anvil.factory(current_node).get_parent():
            current_node = anvil.factory(current_node.get_parent())
            if any([current_node.type() in node_filter, node_filter is None, node_filter == []]):
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

    def _traverse_down_linear_tree(self, start):
        relatives_kwargs = {'allDescendents': True, 'children': True}
        if self.node_filter:
            relatives_kwargs[cfg.TYPE] = self.node_filter
        return list(reversed(rt.dcc.scene.list_relatives(start, **relatives_kwargs)))

    def __iter__(self):
        """ This is setup to only iterate on the nodes in between the top node and the end node
            ignores branching paths
        """
        return self._traverse_up_linear_tree(self.tail, self.head)

    def __contains__(self, item):
        return str(item) in [str(n) for n in ts.flatten(self.get_hierarchy())]

    def __getitem__(self, key):
        if isinstance(key, (int, slice)):
            return list(self)[key]
        else:

            return gc.get_dict_key_matches(key, self.get_hierarchy())

    def __len__(self):
        return len(list(iter(self)))

    def __str__(self):
        return str(self.head)

    def __repr__(self):
        return super(HierarchyChain, self).__repr__().replace('>', '(root=%s, end=%s)>' % (self.head, self.tail))

    def __radd__(self, other):
        return self.__add__(other)

    def __add__(self, other):
        return list(self) + gc.to_list(other)
