import anvil.config as cfg
import anvil.objects as objects
import anvil.runtime as rt
import base


class Control(base.AbstractGrouping):
    ANVIL_TYPE = 'control'
    SHAPE_PARENT_KWARGS = {'relative': True, 'absolute': False, 'shape': True}

    def __init__(self, control=None, offset_group=None, connection_group=None, **kwargs):
        super(Control, self).__init__(top_node=offset_group or control, **kwargs)
        self.register_node('control', control)
        self.register_node('offset_group', offset_group)
        self.register_node('connection_group', connection_group)

    @classmethod
    def build(cls, reference_object=None, meta_data=None, **flags):
        instance = cls(control=objects.Curve.build(meta_data={'type': 'control'}, **flags),
                       offset_group=objects.Transform.build(meta_data={'type': 'offset_group'}, **flags),
                       connection_group=objects.Transform.build(meta_data={'type': 'connection_group'}, **flags),
                       meta_data=meta_data, **flags)
        instance.build_layout()
        instance.match_position(reference_object)
        return instance

    def match_position(self, reference_object):
        try:
            self.offset_group.match_position(reference_object)
        except AttributeError:
            self.control.match_position(reference_object)

    def build_layout(self):
        rt.dcc.scene.parent(self.control, self.offset_group)
        rt.dcc.scene.parent(self.connection_group, self.control)

    def colorize(self, color_id=None, color_tuple=None, use_metadata=False):
        self.control.colorize(color_tuple or color_id, use_metadata=use_metadata)

    def scale_shape(self, value=1.0, relative=False):
        self.control.transform_shape(value, relative=relative, mode=cfg.SCALE)

    def rotate_shape(self, value=90.0, relative=False):
        self.control.transform_shape(value, relative=relative, mode=cfg.ROTATE)

    def translate_shape(self, value=0.0, relative=False):
        self.control.transform_shape(value, relative=relative, mode=cfg.TRANSLATE)

    def swap_shape(self, new_shape, maintain_position=False):
        self.control.swap_shape(new_shape, maintain_position=maintain_position)
        self.rename()
