import anvil.objects as objects
import anvil.runtime as rt
import base


class Control(base.AbstractGrouping):
    ANVIL_TYPE = 'control'

    def __init__(self,
                 control=None,
                 offset_group=None,
                 connection_group=None,
                 **flags):
        super(Control, self).__init__(**flags)
        self.hierarchy['control'] = control
        self.hierarchy['offset_group'] = offset_group
        self.hierarchy['connection_group'] = connection_group

    @classmethod
    def build(cls, meta_data=None, **flags):
        instance = cls(meta_data=meta_data, **flags)
        instance.top_node = instance.add_node(objects.Curve, 'control', meta_data={'type': 'control'}, **flags)
        instance.add_node(objects.Transform, 'offset_group', meta_data={'type': 'offset_group'})
        instance.add_node(objects.Transform, 'connection_group', meta_data={'type': 'connection_group'})
        instance.build_layout()
        return instance

    def build_layout(self):
        if self.flags.get('parent'):
            self.parent(self.flags.get('parent'))
        rt.dcc.scene.parent(str(self.control), str(self.offset_group))
        rt.dcc.scene.parent(str(self.connection_group), str(self.control))
