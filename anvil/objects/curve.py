import yaml
from collections import OrderedDict
import anvil
import anvil.config as cfg
import anvil.runtime as rt
from transform import Transform
import io
from anvil.meta_data import MetaData
from six import iteritems


class Curve(Transform):
    DCC_TYPE = 'nurbsCurve'
    ANVIL_TYPE = cfg.CURVE_TYPE
    BUILT_IN_NAME_TOKENS = Transform.BUILT_IN_NAME_TOKENS.merge({cfg.TYPE: cfg.CURVE_TYPE}, force=True, new=True)
    SHAPE_CACHE = None
    DEFAULT_SHAPE = [[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 3, 0]]

    @staticmethod
    def create_engine_instance(**flags):
        return rt.dcc.create.create_curve(**flags)

    @classmethod
    def build(cls, shape='cube', scale=None, **kwargs):
        if kwargs.get(cfg.POINT) is None:
            kwargs.update(cls._get_shape_constructor(shape, return_positions=True))
        instance = super(Curve, cls).build(**kwargs)

        # Just in case we are using PyMEL and it has returned the actual shape node instead of the transform.
        if rt.dcc.scene.get_type(str(instance)) == cls.DCC_TYPE and instance.get_parent():
            instance._dcc_id = rt.dcc.scene.get_persistent_id(str(instance.get_parent()))

        instance.transform_shape(scale, mode=cfg.SCALE)
        return instance

    @classmethod
    def build_line_indicator(cls, object1, object2, **kwargs):
        kwargs[cfg.DEGREE] = 1
        kwargs[cfg.NAME_TOKENS] = MetaData(kwargs.get(cfg.NAME_TOKENS, {}))
        kwargs[cfg.NAME_TOKENS].update({cfg.NAME: '%s_to_%s' % (object1, object2), cfg.TYPE: cfg.CURVE_TYPE})
        curve = cls.build_from_nodes([object1, object2], **kwargs)
        object1_cluster, object2_cluster = curve.generate_clusters()
        object1_cluster.parent(object1)
        object2_cluster.parent(object2)
        curve.overrideEnabled.set(1)
        curve.overrideDisplayType.set(1)
        return (curve, [object1_cluster, object1_cluster])

    @classmethod
    def build_from_nodes(cls, nodes, **kwargs):
        kwargs[cfg.POINT] = [node.get_world_position() for node in anvil.factory_list(nodes)]
        instance = cls.build(**kwargs)
        return instance

    def auto_color(self, override_color=None):
        self.info('Auto coloring %s based on name_tokens side: %s', self, self.name_tokens.get(cfg.SIDE))
        color = override_color or cfg.RIG_COLORS.get(self.name_tokens.get(cfg.SIDE, None) or cfg.DEFAULT)
        self.colorize(color)
        return color

    def get_shape(self):
        return self._api_class_instance.getShape()

    def cvs(self):
        return self.get_shape().cv[:]

    def transform_shape(self, value, mode=cfg.SCALE, relative=False):
        if value is not None:
            value = [value] * 3 if not isinstance(value, list) else value
            transform_kwargs = {cfg.PIVOTS: self.get_pivot(),
                                cfg.RELATIVE: relative,
                                cfg.ABSOLUTE: not relative,
                                cfg.WORLD_SPACE_DISTANCE: True,
                                self.MODE_LOOKUP[mode]: value}
            rt.dcc.scene.position(self.cvs(), **transform_kwargs)

    def generate_clusters(self):
        return [Transform(rt.dcc.rigging.cluster(cv)[1]) for cv in self.cvs()]

    def swap_shape(self, new_shape, maintain_position=False):
        self.SHAPE_PARENT_KWARGS[cfg.RELATIVE] = not maintain_position
        self.SHAPE_PARENT_KWARGS[cfg.ABSOLUTE] = maintain_position
        curve = self.__class__.build(shape=new_shape)
        rt.dcc.scene.delete(self.get_shape())
        rt.dcc.scene.parent(curve.get_shape(), self, **self.SHAPE_PARENT_KWARGS)

    @classmethod
    def _get_shape_constructor(cls, shape_name, return_positions=False):
        shape_entry = cls.SHAPE_CACHE.get(shape_name or '', {})

        if return_positions:
            return {key: shape_entry.get(key) for key in [cfg.POINT, cfg.DEGREE] if
                    shape_entry.get(key)} or {cfg.POINT: cls.DEFAULT_SHAPE, cfg.DEGREE: 1}

        shape_constructor = shape_entry.pop('constructor')
        api_function = getattr(rt.dcc.ENGINE_API, shape_constructor, None)

        if callable(api_function):
            cls.debug('Obtained shape constructor from yml: %s(%s)', api_function, shape_entry)
            return lambda: api_function(**shape_entry)

    @classmethod
    def populate_shape_file_data(cls, shape_file=None):
        if shape_file is None:
            shape_file = cfg.SHAPES_FILE

        if not cls.SHAPE_CACHE:
            try:
                cls.SHAPE_CACHE = yaml.load(open(shape_file, "r"))
            except IOError:
                cls.error('Missing file %s, please reinstall or locate', shape_file)
                cls.SHAPE_CACHE = {}

    @staticmethod
    def _ordered_dump(data, stream=None, dumper=yaml.Dumper, **kwargs):
        """ Stolen from https://stackoverflow.com/a/21912744.  Great way of dumping as OrderedDict.
        """

        class OrderedDumper(dumper):
            pass

        def _dict_representer(dumper, data):
            return dumper.represent_mapping(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, iteritems(data))

        OrderedDumper.add_representer(OrderedDict, _dict_representer)
        return yaml.dump(data, stream, OrderedDumper, **kwargs)

    def _add_curve_shape_to_shape_file(self, shape_file=None):
        """ Adds the currently encapsulated Curve node's shape data to the shape curve_shapes file based
            on the name of the dag node in the DCC.

        """
        if shape_file is None:
            shape_file = cfg.SHAPES_FILE
        try:
            shape_name = self.name()
            shapes_data = yaml.load(open(shape_file, "r"))

            target_data = shapes_data.get(shape_name, {})
            degree = self.get_shape().degree()
            target_data[cfg.DEGREE] = degree
            target_data[cfg.POINT] = [[round(p, 3) for p in cv.getPosition(space='world')] for cv in
                                      self.get_shape().cv[:]]

            shapes_data[shape_name] = target_data

            with io.open(shape_file, 'w') as f:
                self._ordered_dump(shapes_data, stream=f, encoding='utf-8', default_flow_style=None)
                self.info('Successfully wrote shape data %s to file %s', shape_name, f)

        except IOError:
            self.error('Missing file %s, please reinstall or locate', shape_file)

    @classmethod
    def _build_all_controls(cls):
        for shape in cls.SHAPE_CACHE:
            curve = cls.build(shape=shape)
            curve.rename(shape)


Curve.populate_shape_file_data()
