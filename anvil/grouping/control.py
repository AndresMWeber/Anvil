from anvil.meta_data import MetaData
import anvil.config as cfg
import anvil.objects as objects
import anvil.runtime as rt
import anvil.core.utils as ut
import base


class Control(base.AbstractGrouping):
    ANVIL_TYPE = 'control'
    PV_MOVE_DEFAULT = [3, 0, 0]
    LOCAL_MOVE_KWARGS = MetaData({cfg.RELATIVE: True, 'objectSpace': True, 'worldSpaceDistance': True})
    SHAPE_PARENT_KWARGS = {'relative': True, 'absolute': False, 'shape': True}

    def __init__(self, control=None, offset_group=None, connection_group=None, **kwargs):
        super(Control, self).__init__(top_node=offset_group or control, **kwargs)
        self.register_node('control', control)
        self.register_node('offset_group', offset_group)
        self.register_node('connection_group', connection_group)

    @classmethod
    def build(cls, reference_object=None, meta_data=None, **kwargs):
        instance = cls(control=objects.Curve.build(meta_data={'type': 'control'}, **kwargs),
                       offset_group=objects.Transform.build(meta_data={'type': 'offset_group'}, **kwargs),
                       connection_group=objects.Transform.build(meta_data={'type': 'connection_group'}, **kwargs),
                       meta_data=meta_data, **kwargs)
        instance.build_layout()
        instance.match_position(reference_object)
        return instance

    @classmethod
    def build_pole_vector(cls, joints, ik_handle, move_by=None, meta_data=None, parent=None, **kwargs):
        joints = ut.cast_to_list(joints)
        start, end = joints[0], joints[-1]

        control = Control.build(parent=parent, meta_data=meta_data, **kwargs)
        control.offset_group.match_position([start, end], control.offset_group)
        control.offset_group.aim_at(joints, upObject=start)
        control.offset_group.translate_node(move_by or cls.PV_MOVE_DEFAULT, **cls.LOCAL_MOVE_KWARGS.data)
        control.offset_group.rotate.set([0, 0, 0])

        rt.dcc.connections.pole_vector(control.connection_group, ik_handle)
        return control

    def match_position(self, reference_object):
        try:
            self.offset_group.match_transform(reference_object)
        except AttributeError:
            self.control.match_transform(reference_object)

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
