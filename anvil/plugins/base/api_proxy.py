from six import iteritems
from functools import wraps
import anvil
from jsonschema import validate


class APIProxy(object):
    LOG = anvil.log.obtainLogger(__name__)
    API_LOG = anvil.log.obtainLogger(__name__ + '.api_calls')
    CURRENT_API = None

    BOOLEAN_TYPE = {"type": "boolean"}
    FLOAT_TYPE = {"type": "number"}
    INT_TYPE = {"type": "integer"}
    STR_TYPE = {"type": "string"}

    STR_LIST_TYPE = {"type": "array", "items": STR_TYPE}
    POSITION_TYPE = {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3}
    POSITION_LIST = {"type": "array", "items": POSITION_TYPE}
    POSITION_WEIGHT_TYPE = {"type": "array", "items": {"type": "number"}, "minItems": 4, "maxItems": 4}
    QUERYABLE_POSITION = {"anyOf": [POSITION_TYPE, BOOLEAN_TYPE]}
    MATRIX_TYPE = {"type": "array", "items": {"type": "number"}, "minItems": 16, "maxItems": 16}
    QUERYABLE_MATRIX = {"anyOf": [MATRIX_TYPE, BOOLEAN_TYPE]}
    LINEAR_ANGLE_TYPE = {"type": "array", "items": {"type": "number"}, "minItems": 2, "maxItems": 2}
    STR_OR_STR_LIST_TYPE = {"anyOf": [STR_TYPE, STR_LIST_TYPE]}

    @classmethod
    def _validate_function(cls, schema, api, function_name):
        def to_validate(function):
            @wraps(function)
            def validator(*args, **kwargs):
                cls.LOG.debug('Validating call for %s.%s(%s, %s) against schema %s' % (
                    api.__name__, function_name, ', '.join([str(a) for a in args]),
                    ','.join(['%s=%s' % (k, v) for k, v in iteritems(kwargs)]),
                    list(schema['properties'])))
                validate(kwargs, schema)
                kwargs = cls._initialize_and_filter_flags(kwargs, schema)
                function(*args, **kwargs)
                return cls._log_and_run_api_call(api, function_name, *args, **kwargs)
            return validator
        return to_validate

    @classmethod
    def _initialize_and_filter_flags(cls, flags, schema):
        new_flags = {} if flags is None else flags.copy()

        schema_properties = list(schema.get('properties'))
        cls.LOG.debug('Filtering flags %s for the schema properties %s' % (new_flags, schema_properties))

        for flag_key in list(new_flags):
            if flag_key not in schema_properties:
                cls.LOG.warning('  Flag %s not in schema...removing from flags' % (flag_key))
                new_flags.pop(flag_key)

        for schema_property in schema_properties:
            default = schema['properties'][schema_property].get('default')
            if default is not None and new_flags.get(schema_property) is None:
                cls.LOG.warning('  Flag %s has default value %s from schema ' % (schema_property, default))
                new_flags[schema_property] = default

        return new_flags

    @staticmethod
    def is_anvil_type(obj):
        return issubclass(type(obj), (anvil.grouping.AbstractGrouping, anvil.objects.UnicodeDelegate))

    @classmethod
    def _log_and_run_api_call(cls, api, function_name, *args, **kwargs):
        args = [arg for arg in args if arg not in ['None', None]]
        parametrized_function_call = cls._compose_api_call(api, function_name, *args, **kwargs)
        cls.API_LOG.info(parametrized_function_call)
        return getattr(api, function_name)(*args, **kwargs)

    @staticmethod
    def _compose_api_call(api, function_name, *args, **kwargs):
        formatted_args = ', '.join([str(arg) for arg in args]) if args else ''
        formatted_kwargs = ', '.join('%s=%r' % (key, str(node)) for key, node in iteritems(kwargs)) if kwargs else ''
        formatted_flags = ', '.join(
            '%s=%r' % (key, str(node)) for key, node in iteritems(kwargs.get('flags', {}))) if kwargs else ''
        formatted_parameters = ', '.join([arg for arg in [formatted_args, formatted_kwargs, formatted_flags] if arg])
        return '%s.%s(%s)' % (api.__name__, function_name, formatted_parameters)

    @staticmethod
    def _convert_anvil_nodes_to_string(func):
        def wrapper(*args, **kwargs):
            args = tuple(str(arg) if APIProxy.is_anvil_type(arg) else arg for arg in args)
            for k, v in iteritems(kwargs):
                if APIProxy.is_anvil_type(v):
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
