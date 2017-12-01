from six import iteritems
import anvil
import anvil.runtime as rt
from inspect import isclass


class UnicodeDelegate(object):
    dcc_type = None

    def __init__(self, node_pointer, meta_data=None, **flags):
        """ All nodes must be initialized with a string representation that the encompassing platform
            uses as DAG path representation for the object.

        :param node_pointer: str, DAG path to the object we want to encapsulate
        :param flags: dict, creation flags specific for the platform environment node creation function
        :param meta_data: dict, any object specific meta data we want to record
        """
        anvil.LOG.debug('Initializing node %s with ID %s' % (self.__class__, node_pointer))
        self._dcc_id = rt.dcc.scene.get_persistent_id(str(node_pointer))

        try:
            self._api_class_instance = rt.dcc.scene.APIWrapper(str(node_pointer))
        except:
            self._api_class_instance = object()

        self.flags = flags or {}
        default_meta_data = {'type': self.dcc_type}
        default_meta_data.update(meta_data or {})
        self.meta_data = default_meta_data

    @staticmethod
    def create_engine_instance(**flags):
        return rt.dcc.create.create_node('transform', **flags)

    @classmethod
    def build(cls, meta_data=None, **flags):
        anvil.LOG.info(
            'Building anvil node %s: %s(flags = %s, meta_data = %s)' % (cls.__name__, cls.dcc_type, flags, meta_data))
        dcc_instance = cls.create_engine_instance(**flags)
        instance = cls(dcc_instance, meta_data=meta_data, **flags)

        # If the instance isn't a string we can assume it's some API class instance we can use later.
        if not isinstance(dcc_instance, str):
            instance._api_class_instance = dcc_instance

        return instance

    def __getattr__(self, item):
        try:
            return super(UnicodeDelegate, self).__getattribute__(item)
        except AttributeError as e:
            try:
                _api_class_instance = super(UnicodeDelegate, self).__getattribute__('_api_class_instance')
                try:
                    return getattr(_api_class_instance, item)
                except AttributeError:
                    def to_camel_case(input_string):
                        tokens = input_string.split('_')
                        return tokens[0] + ''.join([token.capitalize() for token in tokens[1:]])
                    return getattr(_api_class_instance, to_camel_case(item))
            except:
                raise e
