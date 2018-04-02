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

    def __init__(self, **kwargs):
        self.controller = None
        self.connection_group = None
        self.offset_group = None
        super(Control, self).__init__(**kwargs)

    @classmethod
    def build(cls, reference_object=None, parent=None, meta_data=None, name_tokens=None, **kwargs):
        kwargs[cfg.META_DATA] = cls.BUILT_IN_META_DATA.merge(meta_data, new=True)
        kwargs[cfg.META_DATA].set_protected(cls.BUILT_IN_META_DATA.protected)
        kwargs[cfg.NAME_TOKENS] = cls.BUILT_IN_NAME_TOKENS.merge(name_tokens, new=True)
        kwargs[cfg.NAME_TOKENS].set_protected(cls.BUILT_IN_NAME_TOKENS.protected)

        instance = cls(**kwargs)

        kwargs.pop(cfg.ID_TYPE, None)
        kwargs['skip_register'] = False
        kwargs['skip_report'] = False

        instance.build_node(ob.Curve, hierarchy_id='control', **kwargs)
        instance.build_node(ob.Transform, hierarchy_id='offset_group', **kwargs)
        instance.build_node(ob.Transform, hierarchy_id='connection_group', **kwargs)
        instance.controller = instance.hierarchy.curve.control
        instance.offset_group = instance.root = instance.hierarchy.node.offset_group
        instance.connection_group = instance.hierarchy.node.connection_group

        instance.controller.name_tokens.merge(instance.CTRL_NAME_TOKENS, force=True)
        instance.offset_group.name_tokens.merge(instance.OFFSET_NAME_TOKENS, force=True)
        instance.connection_group.name_tokens.merge(instance.CONN_NAME_TOKENS, force=True)

        rt.dcc.scene.parent(instance.controller, instance.offset_group)
        rt.dcc.scene.parent(instance.connection_group, instance.controller)

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
        target.match_transform(reference_object, rotate=rotate, translate=translate, **kwargs)

    def colorize(self, rgb_or_index):
        self.controller.colorize(rgb_or_index)

    def scale_shape(self, value=1.0, relative=False):
        self.controller.transform_shape(value, relative=relative, mode=cfg.SCALE)

    def rotate_shape(self, value=90.0, relative=False):
        self.controller.transform_shape(value, relative=relative, mode=cfg.ROTATE)

    def translate_shape(self, value=0.0, relative=False):
        self.controller.transform_shape(value, relative=relative, mode=cfg.TRANSLATE)

    def swap_shape(self, new_shape, maintain_position=False):
        self.controller.swap_shape(new_shape, maintain_position=maintain_position)
        self.rename()

    def rename(self, *input_dicts, **kwargs):
        super(Control, self).rename(*input_dicts, **kwargs)

    def parent(self, new_parent, override_root=None):
        super(Control, self).parent(new_parent, override_root=override_root or self.offset_group or self.controller)
