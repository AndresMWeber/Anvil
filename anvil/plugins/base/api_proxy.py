from six import iteritems
import anvil


class APIProxy(object):
    LOG = anvil.log.obtainLogger(__name__)
    API_LOG = anvil.log.obtainLogger(__name__ + '.api_calls')
    API_LOG.info('import pymel.core as pm')

    def initialize_and_filter_flags(self, flags, schema):
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
    def log_function_call(func):
        def wrapper(*args, **kwargs):
            func_result = func(*args, **kwargs)
            APIProxy.LOG.info('%s(%s, %s) -> %s' % (func.__name__, args, kwargs, func_result))

            if 'initialize' not in func.__name__:
                formatted_args = ', '.join([str(arg) for arg in args]) if args else ''
                formatted_kwargs = ', '.join(
                    '%s=%s' % (key, str(node)) for key, node in iteritems(kwargs)) if kwargs else ''

                formatted_flags = ', '.join(
                    '%s=%s' % (key, str(node)) for key, node in iteritems(kwargs.get('flags', {}))) if kwargs else ''
                formatted_all = ', '.join([arg for arg in [formatted_args, formatted_kwargs, formatted_flags] if arg])
                APIProxy.API_LOG.info('pm.%s(%s)' % (func.__name__, formatted_all))
            return func_result

        wrapper.__name__ = func.__name__

        return wrapper

    def __getattribute__(self, item):
        result = super(APIProxy, self).__getattribute__(item)
        if callable(result):
            return APIProxy.log_function_call(result)
        else:
            return result
