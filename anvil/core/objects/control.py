from jsonschema import validate
import anvil.runtime as runtime
import node_types
import curve


@node_types.register_node
class Control(curve.Curve):
    schema = {
        "type": ["object", "null"],
        "properties": {
            "offset_group": {"type": "string"},
            "connection_group": {"type": "string"}
        },
    }

    def __init__(self, node_unicode_proxy, meta_data=None, name_tokens=None, **flags):
        super(Control, self).__init__(node_unicode_proxy, meta_data=meta_data, name_tokens=name_tokens, **flags)
        validate(flags, self.schema)
        flags = flags or {}
        self.offset_group = flags.get('offset_group')
        self.connection_group = flags.get('connection_group')

    @classmethod
    def build(cls, meta_data=None, name_tokens=None, **flags):
        instance = super(Control, cls).build(meta_data=meta_data, name_tokens=name_tokens, **flags)
        instance.flags['offset_group'] = runtime.dcc.create.create_node('transform')
        instance.flags['connection_group'] = runtime.dcc.create.create_node('transform')
        return instance
