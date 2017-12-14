import yaml
import anvil
import anvil.config as cfg
import anvil.runtime as rt
import transform


class Curve(transform.Transform):
    dcc_type = 'nurbsCurve'
    SHAPE_CACHE = None
    DEFAULT_SHAPE = [[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 3, 0]]

    @staticmethod
    def create_engine_instance(**flags):
        return rt.dcc.create.create_curve(**flags)

    @classmethod
    def build(cls, meta_data=None, shape='cube', pre_scale=None, **flags):
        if flags.get('point') is None:
            flags.update(cls._get_shape_constructor(shape, return_positions=True))
        instance = super(Curve, cls).build(meta_data=meta_data, **flags)

        # Just in case we are using PyMEL and it has returned the actual shape node instead of the transform.
        if rt.dcc.scene.get_type(str(instance)) == cls.dcc_type and instance.get_parent():
            instance._dcc_id = rt.dcc.scene.get_persistent_id(str(instance.get_parent()))
        if pre_scale:
            instance.transform_shape(pre_scale, mode=cfg.SCALE)
        return instance

    @classmethod
    def build_from_objects(cls, objects, meta_data=None, **flags):
        position_flags = {'query': True, 'translation': True, 'worldSpace': True}
        flags['point'] = [rt.dcc.scene.position(str(object), **position_flags) for object in objects]
        instance = cls.build(meta_data=meta_data, **flags)
        return instance

    def colorize(self, color_id=None, color_tuple=None, use_metadata=False):
        raise NotImplementedError

    def transform_shape(self, value, mode=cfg.SCALE, relative=False):
        transform_kwargs = {cfg.PIVOTS: list(self.scalePivot.get()),
                            cfg.RELATIVE: relative,
                            cfg.ABSOLUTE: not relative}
        if not isinstance(value, list):
            value = [value] * 3

        if mode == cfg.SCALE:
            transform_kwargs[cfg.SCALE] = value
        elif mode == cfg.TRANSLATE:
            transform_kwargs[cfg.TRANSLATION] = value
        elif mode == cfg.ROTATE:
            transform_kwargs[cfg.ROTATE] = value
        rt.dcc.scene.position(self.get_shape().cv[:], **transform_kwargs)

    def swap_shape(self, new_shape, maintain_position=False):
        self.SHAPE_PARENT_KWARGS['relative'] = not maintain_position
        self.SHAPE_PARENT_KWARGS['absolute'] = maintain_position
        curve = self.__class__.build(shape=new_shape)
        rt.dcc.scene.delete(self.get_shape())
        rt.dcc.scene.parent(curve.get_shape(), self, **self.SHAPE_PARENT_KWARGS)

    @classmethod
    def _get_shape_constructor(cls, shape_name, return_positions=False):
        shape_entry = cls.SHAPE_CACHE.get(shape_name or '', {})

        if return_positions:
            return {key: shape_entry.get(key) for key in ['point', 'degree'] if
                    shape_entry.get(key)} or {'point': cls.DEFAULT_SHAPE, 'degree': 1}

        shape_constructor = shape_entry.pop('constructor')
        api_function = getattr(rt.dcc.ENGINE_API, shape_constructor, None)

        if callable(api_function):
            anvil.LOG.debug('Obtained shape constructor from yml: %s(%s)' % (api_function, shape_entry))
            return lambda: api_function(**shape_entry)

    @classmethod
    def _populate_shape_file_data(cls, shape_file=None):
        if shape_file is None:
            shape_file = cfg.SHAPES_FILE

        if not cls.SHAPE_CACHE:
            try:
                cls.SHAPE_CACHE = yaml.load(open(shape_file, "r"))
            except IOError:
                anvil.LOG.error('Missing file %s, please reinstall or locate' % shape_file)
                cls.SHAPE_CACHE = {}


Curve._populate_shape_file_data()
