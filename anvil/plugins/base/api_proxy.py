from inspect import ismodule
import sys
from six import iteritems
import anvil
import dependencies

class APIProxy(object):
    LOG = anvil.log.obtainLogger(__name__)
    API_LOG = anvil.log.obtainLogger(__name__ + '.api_calls')
    CURRENT_API = None

    def __init__(self):
        for dependency in dir(dependencies):
            if ismodule(getattr(dependencies, dependency)):
                if dependency not in sys.modules:
                    import_call = 'import %s' % dependency.__name__
                    self.API_LOG.info(import_call)
                    eval(import_call)

    def _initialize_and_filter_flags(self, flags, schema):
        if flags is None or flags == {}:
            return {}
        else:
            new_flags = flags.copy()
            schema_properties = [key for key in list(schema.get('properties'))]
            self.LOG.debug('Filtering flags %s for the schema properties %s' % (new_flags, schema_properties))
            for flag_key in list(new_flags):
                if flag_key not in schema_properties:
                    self.LOG.warning('  Flag %s not in schema...removing from flags' % (flag_key))
                    new_flags.pop(flag_key)
            return new_flags

    @staticmethod
    def is_anvil_type(obj):
        return issubclass(type(obj), (anvil.grouping.AbstractGrouping, anvil.objects.UnicodeDelegate))

    @classmethod
    def _log_and_run_api_call(cls, api, function_name, *args, **kwargs):
        parametrized_function_call = cls._compose_api_call(api, function_name, *args, **kwargs)
        cls.API_LOG.info(parametrized_function_call)
        return getattr(api, function_name)(*args, **kwargs)

    @staticmethod
    def _compose_api_call(api, function_name, *args, **kwargs):
        formatted_args = ', '.join([str(arg) for arg in args]) if args else ''
        formatted_kwargs = ', '.join('%s=%s' % (key, str(node)) for key, node in iteritems(kwargs)) if kwargs else ''
        formatted_flags = ', '.join(
            '%s=%s' % (key, str(node)) for key, node in iteritems(kwargs.get('flags', {}))) if kwargs else ''
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