import node_types as node_types
import anvil.runtime as runtime


@node_types.register_node
class UnicodeDelegate(object):
    dcc_type = None

    def __init__(self, node_unicode_proxy):
        self._dcc_id = runtime.dcc.scene.get_persistent_id(node_unicode_proxy)

    @classmethod
    def build(cls, flags=None, metaData=None):
        dcc_instance = runtime.dcc.create.create_node(cls.dcc_type)
        instance = cls(dcc_instance.__name__, flags=flags, metaData=metaData)
        instance._pymel_node = dcc_instance
        return instance
