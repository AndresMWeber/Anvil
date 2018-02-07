from six import iteritems
from functools import wraps
import anvil
import anvil.config as cfg
from jsonschema import validate

DEFAULT_SCHEMA = {cfg.TYPE: ["object", "null"], "properties": {}}
BOOL_TYPE = {cfg.TYPE: cfg.BOOLEAN}
FLOAT_TYPE = {cfg.TYPE: cfg.NUMBER}
INT_TYPE = {cfg.TYPE: cfg.INTEGER}
STR_TYPE = {cfg.TYPE: cfg.STRING}
NUM_TYPE = {cfg.TYPE: cfg.NUMBER}

STR_LIST_TYPE = {cfg.TYPE: cfg.ARRAY, "items": STR_TYPE}
POSITION_TYPE = {cfg.TYPE: cfg.ARRAY, "items": NUM_TYPE, "minItems": 3, "maxItems": 3}
POSITION_LIST = {cfg.TYPE: cfg.ARRAY, "items": POSITION_TYPE}
POSITION_WEIGHT_TYPE = {cfg.TYPE: cfg.ARRAY, "items": NUM_TYPE, "minItems": 4, "maxItems": 4}
QUERYABLE_POSITION = {"anyOf": [POSITION_TYPE, BOOL_TYPE]}
MATRIX_TYPE = {cfg.TYPE: cfg.ARRAY, "items": NUM_TYPE, "minItems": 16, "maxItems": 16}
QUERYABLE_MATRIX = {"anyOf": [MATRIX_TYPE, BOOL_TYPE]}
LINEAR_ANGLE_TYPE = {cfg.TYPE: cfg.ARRAY, "items": NUM_TYPE, "minItems": 2, "maxItems": 2}
LINEAR_STRING_TYPE = {cfg.TYPE: cfg.ARRAY, "items": STR_TYPE, "minItems": 2, "maxItems": 2}
STR_OR_STR_LIST_TYPE = {"anyOf": [STR_TYPE, STR_LIST_TYPE]}
POSITION_OR_STR_TYPE = {"anyOf": [STR_TYPE, POSITION_LIST]}


class APIProxy(object):
    LOG = anvil.log.obtainLogger(__name__)
    API_LOG = anvil.log.obtainLogger(__name__ + '.api_calls')
    CURRENT_API = None

    @classmethod
    def _validate_function(cls, schema, api, function_name):
        def to_validate(function):
            @wraps(function)
            def validator(*args, **kwargs):
                validate(kwargs, schema)
                kwargs = cls._initialize_and_filter_flags(kwargs, schema)
                return cls._log_and_run_api_call(api, function_name, *args, **kwargs)
            return validator
        return to_validate

    @classmethod
    def _initialize_and_filter_flags(cls, flags, schema):
        new_flags = {} if flags is None else flags.copy()

        schema_properties = list(schema.get('properties'))

        for flag_key in list(new_flags):
            if flag_key not in schema_properties:
                new_flags.pop(flag_key)

        for schema_property in schema_properties:
            default = schema['properties'][schema_property].get(cfg.DEFAULT)
            if default is not None and new_flags.get(schema_property) is None:
                new_flags[schema_property] = default

        return new_flags

    @classmethod
    def _log_and_run_api_call(cls, api, function_name, *args, **kwargs):
        # Pre-process all Anvil nodes to str
        args = [str(arg) if anvil.is_anvil(arg) else arg for arg in args if arg not in ['None', None]]

        if kwargs:
            flags = kwargs.pop('flags', {})
            kwargs.update(flags)
            for key, node in iteritems(kwargs):
                if anvil.is_anvil(node):
                    kwargs[key] = str(node)

        cls.API_LOG.info(cls._compose_api_call(api, function_name, *args, **kwargs))
        return getattr(api, function_name)(*args, **kwargs)

    @staticmethod
    def _compose_api_call(api, function_name, *args, **kwargs):
        formatted_args = ', '.join([repr(a) for a in args]) if args else ''

        flags = kwargs.pop('flags', {})
        kwargs.update(flags)
        if kwargs is not None and kwargs != {}:
            formatted_args += ''.join(', %s=%r' % (key, node) for key, node in iteritems(kwargs))

        return '%s.%s(%s)' % (api.__name__, function_name, formatted_args)

    @staticmethod
    def _convert_anvil_nodes_to_string(func):
        def wrapper(*args, **kwargs):
            args = tuple(str(arg) if anvil.is_anvil(arg) else arg for arg in args)
            for k, v in iteritems(kwargs):
                if anvil.is_anvil(v):
                    kwargs[k] = str(v)

            result = func(*args, **kwargs)
            if not func.__name__.startswith('_'):
                try:
                    class_name = func.im_class.__name__
                    report = '%s.%s(%s, %s)\t# Result: %s' % (class_name, func.__name__, args, kwargs, result)
                    APIProxy.LOG.info(report)
                except AttributeError:
                    pass

            return result

        wrapper.__name__ = func.__name__

        return wrapper

    def __getattribute__(self, item):
        result = super(APIProxy, self).__getattribute__(item)
        if callable(result):
            return APIProxy._convert_anvil_nodes_to_string(result)
        else:
            return result


def merge_dicts(*dicts):
    result = {}
    for dictionary in dicts:
        result.update(dictionary)
    return result
