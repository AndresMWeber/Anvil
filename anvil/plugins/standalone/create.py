import anvil.plugins.base.create as create


class Create(create.Create):
    def create_node(self, dcc_node_type, **flags):
        return dcc_node_type

    def create_transform(self, **flags):
        return 'group'

    def create_joint(self, **flags):
        return 'joint'

    def create_curve(self, **flags):
        return 'curve'
