import anvil.objects as objects
import anvil.runtime as rt
import base


class Control(base.AbstractGrouping):
    ANVIL_TYPE = 'control'

    def __init__(self, control=None, offset_group=None, connection_group=None, **flags):
        super(Control, self).__init__(top_node=offset_group or control, **flags)
        self.register_node('control', control)
        self.register_node('offset_group', offset_group)
        self.register_node('connection_group', connection_group)

    @classmethod
    def build(cls, meta_data=None, **flags):
        instance = cls(control=objects.Curve.build(meta_data={'type': 'control'}, **flags),
                       offset_group=objects.Transform.build(meta_data={'type': 'offset_group'}, **flags),
                       connection_group=objects.Transform.build(meta_data={'type': 'connection_group'}, **flags),
                       meta_data=meta_data, **flags)
        instance.build_layout()
        return instance

    def build_layout(self):
        if self.flags.get('parent'):
            self.parent(self.flags.get('parent'))

        rt.dcc.scene.parent(str(self.control), str(self.offset_group))
        rt.dcc.scene.parent(str(self.connection_group), str(self.control))

    def colorize(self, color_id=None, color_tuple=None):
        self.control.colorize(color_tuple or color_id)

