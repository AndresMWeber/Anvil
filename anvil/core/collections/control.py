import anvil.plugins as plugins
from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "offset_group": {"type": "string"},
        "connection_group": {"type": "string"},
        "world": {"type": "boolean"},
        "parent": {"type": "string"},
        "empty": {"type": "boolean"},
        "relative": {"type": "boolean"},
        "absolute": {"type": "boolean"},
    },
}

class Control(object):
    def __init__(self, flags=None, metaData=None):
        validate(flags, schema)
        self.offset_group = flags.get('offset_group')
        self.connection_group = flags.get('connection_group')

    @classmethod
    def build(cls, flags=None, metaData=None):
        curve = plugins.current_dcc.create_node('curve')
        flags['offset_group'] = plugins.current_dcc.create_node('transform')
        flags['connection_group'] = plugins.current_dcc.create_node('transform')

        instance = cls(flags=flags, metaData=metaData)
        instance._pymel_node = curve
        return instance
