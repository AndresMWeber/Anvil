from anvil.meta_data import MetaData
import anvil.config as cfg
import anvil.objects as ob
import anvil.runtime as rt
import anvil.utils.generic as gc
import base


class Control(base.AbstractGrouping):
    ANVIL_TYPE = cfg.CONTROL_TYPE

    CTRL_NAME_TOKENS = {cfg.TYPE: cfg.CONTROL_TYPE}
    OFFSET_NAME_TOKENS = {cfg.TYPE: cfg.OFFSET_GROUP}
    CONN_NAME_TOKENS = {cfg.TYPE: cfg.CONNECTION_GROUP}

    PV_MOVE_DEFAULT = [0, 0, 3]
    PV_AIM_DEFAULT = [0, 0, 1]
    PV_UP_DEFAULT = [0, 1, 0]

    LOCAL_MOVE_KWARGS = {cfg.RELATIVE: True, cfg.OBJECT_SPACE: True, cfg.WORLD_SPACE_DISTANCE: True}
    SHAPE_PARENT_KWARGS = {cfg.RELATIVE: True, cfg.ABSOLUTE: False, cfg.SHAPE: True}

    def __init__(self, control=None, offset_group=None, connection_group=None, **kwargs):
        super(Control, self).__init__(top_node=offset_group or control, **kwargs)
        self.register_node(cfg.CONTROL_TYPE, control)
        self.register_node(cfg.OFFSET_GROUP, offset_group)
        self.register_node(cfg.CONNECTION_GROUP, connection_group)
        getattr(self, cfg.CONTROL_TYPE).name_tokens.merge(self.CTRL_NAME_TOKENS, force=True)
        getattr(self, cfg.OFFSET_GROUP).name_tokens.merge(self.OFFSET_NAME_TOKENS, force=True)
        getattr(self, cfg.CONNECTION_GROUP).name_tokens.merge(self.CONN_NAME_TOKENS, force=True)

    @classmethod
    def build(cls, reference_object=None, parent=None, meta_data=None, name_tokens=None, **kwargs):
        meta_data = cls.BUILT_IN_META_DATA.merge(meta_data, new=True)
        meta_data.set_protected(cls.BUILT_IN_META_DATA.protected)
        name_tokens = cls.BUILT_IN_NAME_TOKENS.merge(name_tokens, new=True)
        name_tokens.set_protected(cls.BUILT_IN_NAME_TOKENS.protected)

        kwargs[cfg.META_DATA] = meta_data
        instance = cls(
            ob.Curve.build(name_tokens=name_tokens, **kwargs),
            ob.Transform.build(name_tokens=name_tokens, **kwargs),
            ob.Transform.build(name_tokens=name_tokens, **kwargs),
            name_tokens=name_tokens,
            **kwargs)

        instance.build_layout()
        instance.match_position(reference_object, **kwargs)
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
        offset.translate_node(move_by or cls.PV_MOVE_DEFAULT, **cls.LOCAL_MOVE_KWARGS)
        offset.rotate.set([0, 0, 0])

        rt.dcc.connections.pole_vector(getattr(control, cfg.CONNECTION_GROUP), ik_handle)
        return control

    def match_position(self, reference_object, rotate=True, translate=True, **kwargs):
        try:
            target = self.offset_group
        except AttributeError:
            target = self.control
        target.match_transform(reference_object, rotate=rotate, translate=translate)

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
