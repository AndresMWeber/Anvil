import anvil
import anvil.config as cfg
import anvil.log as log
from anvil.meta_data import MetaData
import anvil.runtime as rt
import anvil.utils.generic as gc


class UnicodeDelegate(log.LogMixin):
    LOG = log.obtainLogger(__name__)
    DCC_TYPE = None
    ANVIL_TYPE = 'unicode'
    BUILT_IN_METADATA = MetaData({})
    BUILT_IN_NAME_TOKENS = MetaData({cfg.TYPE: ANVIL_TYPE, cfg.NAME: 'untitled'}, protected=cfg.TYPE)

    def __init__(self, node_pointer, meta_data=None, name_tokens=None, **kwargs):
        """ All nodes must be initialized with a string representation that the encompassing platform
            uses as DAG path representation for the object.

        :param node_pointer: str, DAG path to the object we want to encapsulate
        :param kwargs: dict, creation flags specific for the platform environment node creation function
        :param meta_data: dict, any object specific meta data we want to record
        """
        self.debug('Initializing node %s with ID %s, name_tokens=%s, meta_data=%s, %s',
                  self.__class__, node_pointer, name_tokens, meta_data, kwargs)
        self._dcc_id = rt.dcc.scene.get_persistent_id(str(node_pointer))

        self.meta_data = self.BUILT_IN_METADATA.merge(meta_data, new=True)
        self.meta_data.set_protected(self.BUILT_IN_METADATA)

        self.name_tokens = self.BUILT_IN_NAME_TOKENS.merge(name_tokens, new=True)
        self.name_tokens.set_protected(self.BUILT_IN_NAME_TOKENS)

        self.build_kwargs = MetaData(kwargs)

        try:
            self._api_class_instance = rt.dcc.scene.APIWrapper(str(node_pointer))
        except:
            self._api_class_instance = object()

    def name(self):
        return self._dcc_id.partialPathName()

    def exists(self):
        return rt.dcc.scene.exists(self)

    def rename(self, new_name):
        return rt.dcc.scene.rename(self.name(), new_name)

    def type(self):
        return rt.dcc.scene.get_type(self)

    @staticmethod
    def create_engine_instance(**flags):
        raise NotImplementedError('Cannot instantiate nodes from this class')

    @classmethod
    def build(cls, **kwargs):
        cls.info('Building node %s: %s(%s)', cls.__name__, cls.DCC_TYPE, kwargs)
        dcc_instance = cls.create_engine_instance(**kwargs)
        instance = cls(dcc_instance, **kwargs)

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
                return getattr(_api_class_instance, gc.to_camel_case(item))

    def __eq__(self, other):
        return str(self) == str(other)

    def __repr__(self):
        return '<%s.%s @ 0x%x (%s)>' % (self.__class__.__module__, self.__class__.__name__, id(self), str(self))

    def __str__(self):
        return str(self.name())
