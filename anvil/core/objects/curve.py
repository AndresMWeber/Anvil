import os
import node_types as node_types
import transform
import anvil
import anvil.config as config
import anvil.runtime as runtime
import yaml


@node_types.register_node
class Curve(transform.Transform):
    dcc_type = 'curve'
    SHAPE_CACHE = None
    DEFAULT_SHAPE = [[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 3, 0]]

    @classmethod
    def build(cls, meta_data=None, shape='cube', **flags):
        if flags.get('point') is None:
            flags.update(cls._get_shape_constructor(shape, return_positions=True))

        return super(Curve, cls).build(meta_data=meta_data, **flags)

    @classmethod
    def _get_shape_constructor(cls, shape_name, return_positions=False):
        cls._populate_shape_file_data()
        shape_entry = cls.SHAPE_CACHE.get(shape_name or '', {})

        if return_positions:
            return {key: shape_entry.get(key) for key in ['point', 'degree'] if
                    shape_entry.get(key)} or {'point': cls.DEFAULT_SHAPE, 'degree': 1}

        shape_constructor = shape_entry.pop('constructor')
        api_function = getattr(runtime.dcc.ENGINE_API, shape_constructor, None)

        if callable(api_function):
            anvil.LOG.info('Obtained shape constructor from yml: %s(%s)' % (api_function, shape_entry))
            return lambda: api_function(**shape_entry)

    @classmethod
    def _populate_shape_file_data(cls, shape_file=None):
        if shape_file is None:
            shape_file = config.SHAPES_FILE

        if not cls.SHAPE_CACHE:
            anvil.LOG.info('Initializing shapes lookup from yml file')
            try:
                cls.SHAPE_CACHE = yaml.load(open(shape_file, "r"))
            except IOError:
                anvil.LOG.error('Missing file %s, please reinstall or locate' % shape_file)
                cls.SHAPE_CACHE = {}
