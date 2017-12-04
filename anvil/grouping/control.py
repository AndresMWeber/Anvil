import anvil.objects as objects
import anvil.runtime as rt
import base


class Control(base.AbstractGrouping):
    ANVIL_TYPE = 'control'
    SHAPE_PARENT_KWARGS = {'relative': True, 'absolute': False, 'shape': True}

    def __init__(self, control=None, offset_group=None, connection_group=None, **flags):
        super(Control, self).__init__(top_node=offset_group or control, **flags)
        self.register_node('control', control)
        self.register_node('offset_group', offset_group)
        self.register_node('connection_group', connection_group)

    @classmethod
    def build(cls, reference_object=None, meta_data=None, **flags):
        instance = cls(control=objects.Curve.build(meta_data={'type': 'control'}, **flags),
                       offset_group=objects.Transform.build(meta_data={'type': 'offset_group'}, **flags),
                       connection_group=objects.Transform.build(meta_data={'type': 'connection_group'}, **flags),
                       meta_data=meta_data, **flags)
        instance.offset_group.match_position(reference_object)
        instance.build_layout()
        return instance

    def build_layout(self):
        if self.flags.get('parent'):
            self.parent(self.flags.get('parent'))
        rt.dcc.scene.parent(self.control, self.offset_group, relative=True)
        rt.dcc.scene.parent(self.connection_group, self.control, relative=True)

    def colorize(self, color_id=None, color_tuple=None, use_metadata=False):
        self.control.colorize(color_tuple or color_id)

    def scale_shape(self, value=1.0, relative=False):
        rt.dcc.scene.position(self.control.get_shape().cv[:],
                              scale=[value] * 3,
                              pivots=self.control.scalePivot.get(),
                              relative=relative,
                              absolute=not relative)

    def swap_shape(self, new_shape, maintain_position=False):
        self.SHAPE_PARENT_KWARGS['relative'] = not maintain_position
        self.SHAPE_PARENT_KWARGS['absolute'] = maintain_position
        curve = objects.Curve.build(shape=new_shape)
        rt.dcc.scene.delete(self.control.get_shape())
        rt.dcc.scene.parent(curve.get_shape(), self.control, **self.SHAPE_PARENT_KWARGS)
        self.rename()
