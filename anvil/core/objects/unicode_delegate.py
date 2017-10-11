from six import iteritems
import node_types as node_types
import anvil
import anvil.runtime as runtime


@node_types.register_node
class UnicodeDelegate(object):
    dcc_type = None

    def __init__(self, node_unicode_proxy, flags=None, meta_data=None):
        anvil.LOG.info('Initializing node with ID %s' % node_unicode_proxy)
        self._dcc_id = runtime.dcc.scene.get_persistent_id(node_unicode_proxy)
        self.flags = flags or {}
        self.meta_data = meta_data or {}

    def name(self):
        return self._dcc_id

    @classmethod
    def build(cls, meta_data=None, name_tokens=None, **flags):
        cls.convert_subclass_kwargs(flags)
        dcc_instance = runtime.dcc.create.create(cls.dcc_type, flags=flags)

        try:
            dcc_dag_path = dcc_instance.name()
        except AttributeError:
            dcc_dag_path = dcc_instance
        print(flags, meta_data, dcc_dag_path)
        instance = cls(dcc_dag_path, meta_data=meta_data)#, flags=flags)
        instance._pymel_node = dcc_instance

        return instance

    @classmethod
    def convert_subclass_kwargs(cls, flags):
        if isinstance(flags, dict):
            for k, v in iteritems(flags):
                try:
                    if issubclass(type(v), cls):
                        flags[k] = v.name()
                except (AttributeError, TypeError):
                    pass
