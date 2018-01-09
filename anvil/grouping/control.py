from anvil.meta_data import MetaData, cls_merge_name_tokens_and_meta_data
import anvil.config as cfg
import anvil.objects as ob
import anvil.runtime as rt
import anvil.utils.generic as gc
import base


class Control(base.AbstractGrouping):
    ANVIL_TYPE = cfg.CONTROL_TYPE
    PV_MOVE_DEFAULT = [0, 0, 3]
    PV_AIM_DEFAULT = [0, 0, 1]
    PV_UP_DEFAULT = [0, 1, 0]
    LOCAL_MOVE_KWARGS = MetaData({cfg.RELATIVE: True, cfg.OBJECT_SPACE: True, cfg.WORLD_SPACE_DISTANCE: True})
    SHAPE_PARENT_KWARGS = {cfg.RELATIVE: True, cfg.ABSOLUTE: False, cfg.SHAPE: True}

    def __init__(self, control=None, offset_group=None, connection_group=None, **kwargs):
        super(Control, self).__init__(top_node=offset_group or control, **kwargs)
        self.register_node(cfg.CONTROL_TYPE, control)
        self.register_node(cfg.OFFSET_GROUP, offset_group)
        self.register_node(cfg.CONNECTION_GROUP, connection_group)

    @classmethod
    @cls_merge_name_tokens_and_meta_data(pre=True)
    def build(cls, reference_object=None, parent=None, name_tokens=None, **kwargs):
        name_tokens = MetaData(name_tokens)
        instance = cls(
            ob.Curve.build(name_tokens=name_tokens + {cfg.TYPE: cfg.CONTROL_TYPE}, **kwargs),
            ob.Transform.build(name_tokens=name_tokens + {cfg.TYPE: cfg.OFFSET_GROUP}, **kwargs),
            ob.Transform.build(name_tokens=name_tokens + {cfg.TYPE: cfg.CONNECTION_GROUP}, **kwargs),
            **kwargs)
        instance.build_layout()
        instance.match_position(reference_object)
        instance.parent(parent)
        return instance

    @classmethod
    def build_pole_vector(cls, joints, ik_handle,
                          up_vector=None, aim_vector=None, up_object=None, move_by=None, **kwargs):
        joints = gc.to_list(joints)
        start, end = joints[0], joints[-1]

        control = cls.build(**kwargs)
        offset = getattr(control, cfg.OFFSET_GROUP)
        offset.match_position([start, end])
        offset.aim_at(joints,
                      aim_vector=aim_vector or cls.PV_AIM_DEFAULT,
                      up_vector=up_vector or cls.PV_UP_DEFAULT,
                      up_object=up_object or start)
        offset.translate_node(move_by or cls.PV_MOVE_DEFAULT, **cls.LOCAL_MOVE_KWARGS.data)
        offset.rotate.set([0, 0, 0])

        rt.dcc.connections.pole_vector(getattr(control, cfg.CONNECTION_GROUP), ik_handle)
        return control

    def match_position(self, reference_object):
        try:
            self.offset_group.match_transform(reference_object)
        except AttributeError:
            self.control.match_transform(reference_object)

    def build_layout(self):
        rt.dcc.scene.parent(getattr(self, cfg.CONTROL_TYPE), getattr(self, cfg.OFFSET_GROUP))
        rt.dcc.scene.parent(getattr(self, cfg.CONNECTION_GROUP), getattr(self, cfg.CONTROL_TYPE))

    def colorize(self, rgb_or_index):
        self.control.colorize(rgb_or_index)

    def scale_shape(self, value=1.0, relative=False):
        self.control.transform_shape(value, relative=relative, mode=cfg.SCALE)

    def rotate_shape(self, value=90.0, relative=False):
        self.control.transform_shape(value, relative=relative, mode=cfg.ROTATE)

    def translate_shape(self, value=0.0, relative=False):
        self.control.transform_shape(value, relative=relative, mode=cfg.TRANSLATE)

    def swap_shape(self, new_shape, maintain_position=False):
        self.control.swap_shape(new_shape, maintain_position=maintain_position)
        self.rename()
