import anvil.plugins.base.create as create


class Create(create.Create):
    def create_transform(self, **flags):
        return 'group'

    def create_joint(self, **flags):
        return 'joint'

    def create_curve(self, **flags):
        return 'curve'
