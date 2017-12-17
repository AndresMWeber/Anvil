import anvil
import anvil.log as log
from anvil.meta_data import MetaData
import anvil.runtime as rt


class UnicodeDelegate(object):
    LOG = log.obtainLogger(__name__)
    dcc_type = None
    BUILTIN_METADATA = {'type': dcc_type}

    def __init__(self, node_pointer, meta_data=None, **kwargs):
        """ All nodes must be initialized with a string representation that the encompassing platform
            uses as DAG path representation for the object.

        :param node_pointer: str, DAG path to the object we want to encapsulate
        :param kwargs: dict, creation flags specific for the platform environment node creation function
        :param meta_data: dict, any object specific meta data we want to record
        """

        self.LOG.debug('Initializing node %s with ID %s' % (self.__class__, node_pointer))
        self._dcc_id = rt.dcc.scene.get_persistent_id(str(node_pointer))
        self.meta_data = MetaData(meta_data, kwargs)

        try:
            self._api_class_instance = rt.dcc.scene.APIWrapper(str(node_pointer))
        except:
            self._api_class_instance = object()

    def name(self):
        return str(self._dcc_id)

    def exists(self):
        return rt.dcc.scene.exists(self)

    def rename(self, new_name):
        return rt.dcc.scene.rename(self.name(), new_name)

    @staticmethod
    def create_engine_instance(**flags):
        raise NotImplementedError('Cannot instantiate nodes from this class')

    @classmethod
    def build(cls, meta_data=None, **kwargs):
        cls.LOG.info('Building node %s: %s(kwargs=%s, meta_data=%s)' % (cls.__name__, cls.dcc_type, kwargs, meta_data))
        dcc_instance = cls.create_engine_instance(**kwargs)
        instance = cls(dcc_instance, meta_data=meta_data, **kwargs)

        # If the instance isn't a string we can assume it's some API class instance we can use later.
        if not isinstance(dcc_instance, str):
            instance._api_class_instance = dcc_instance
        anvil.register_encapsulation(instance)
        return instance

    def get_history(self, **kwargs):
        return rt.dcc.connections.list_history(self, **kwargs)

    def get_future(self, **kwargs):
        kwargs['future'] = True
        return rt.dcc.connections.list_history(self, **kwargs)

    def __getattr__(self, item):
        try:
            return super(UnicodeDelegate, self).__getattribute__(item)
        except AttributeError:
            _api_class_instance = super(UnicodeDelegate, self).__getattribute__('_api_class_instance')
            try:
                return getattr(_api_class_instance, item)
            except AttributeError:
                def to_camel_case(input_string):
                    tokens = input_string.split('_')
                    return tokens[0] + ''.join([token.capitalize() for token in tokens[1:]])

                return getattr(_api_class_instance, to_camel_case(item))

    def __eq__(self, other):
        return str(self) == str(other)

    def __repr__(self):
        return '<%s.%s @ 0x%x (%s)>' % (self.__class__.__module__, self.__class__.__name__, id(self), str(self))

    def __str__(self):
        return str(self.name())
