import anvil


class APIProxy(object):
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
