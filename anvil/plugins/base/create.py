from api_proxy import APIProxy


class Create(APIProxy):
    def create(self, dcc_node_type, flags=None):
        self.LOG.debug('Attempting to create node type %s with flags %s' % (dcc_node_type, flags))
        function_name_query = 'create_%s' % dcc_node_type
        node = dcc_node_type
        try:
            node = getattr(self, function_name_query)(flags=flags)
        except AttributeError:
            self.LOG.warning('No custom method for node type %s found...defaulting...' % dcc_node_type)
        self.LOG.info('Created node %s from function %s with flags %s' % (node, function_name_query, flags))
        return node

    def create_transform(self, *dcc_nodes, **flags):
        raise NotImplementedError

    def create_joint(self, **flags):
        raise NotImplementedError

    def create_curve(self, **flags):
        raise NotImplementedError
