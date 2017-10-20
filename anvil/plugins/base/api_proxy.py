import anvil


class APIProxy(object):
    LOG = anvil.log.obtainLogger(__name__)

    def initialize_and_filter_flags(self, flags, schema):
        if flags is None or flags == {}:
            return {}
        else:
            new_flags = flags.copy()
            schema_properties = [key for key in list(schema.get('properties'))]
            anvil.LOG.debug('Filtering flags %s for the schema properties %s' % (new_flags, schema_properties))
            for flag_key in list(new_flags):
                if flag_key not in schema_properties:
                    anvil.LOG.info('  Flag %s not in schema...removing from flags' % (flag_key))
                    new_flags.pop(flag_key)
            return new_flags

    @staticmethod
    def log_function_call(func):
        print('wrapping function %s' % func.__name__)
        def wrapper(*args, **kwargs):
            func_result = func(*args, **kwargs)
            APIProxy.LOG.info('%s(%s, %s) -> %s' % (func.__name__, args, kwargs, func_result))
            return func_result

        wrapper.__name__ = func.__name__

        return wrapper

    def __getattribute__(self, item):
        print('trying to get item %s from %s' % (item, self))
        result = super(APIProxy, self).__getattribute__(item)
        if callable(result):
            return APIProxy.log_function_call(result)
        else:
            return result
