from anvil.plugins.abstract.dependencies import *
from jsonschema import validate


class Create(object):
    def create_node(self, dcc_node_type, flags=None):
        function_name_query = 'create_%s' % dcc_node_type
        if hasattr(self, function_name_query):
            getattr(self, function_name_query)(flags)
        else:
            schema = {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "parent": {"type": "string"},
                    "shared": {"type": "boolean"},
                    "skipSelect": {"type": "boolean"},
                },
            }
            validate(flags, schema)

            return dcc_node_type

    def create_transform(self, flags=None):
        schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "world": {"type": "boolean"},
                "parent": {"type": "string"},
                "empty": {"type": "boolean"},
                "relative": {"type": "boolean"},
                "absolute": {"type": "boolean"},
            },
        }
        validate(flags, schema)
        flags['empty'] = flags.get('empty', True)
        return 'group'

    def create_joint(self, flags=None):
        schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "world": {"type": "boolean"},
                "absolute": {"type": "boolean"},
                "angleX": {"type": "number"},
                "angleY": {"type": "number"},
                "angleZ": {"type": "number"},
                "degreeOfFreedom": {"type": "string"},
                "limitSwitchX": {"type": "boolean"},
                "limitSwitchY": {"type": "boolean"},
                "limitSwitchZ": {"type": "boolean"},
                "limitX": {"type": "array", "items": {"type": "number"}, "minItems": 2, "maxItems": 2},
                "limitY": {"type": "array", "items": {"type": "number"}, "minItems": 2, "maxItems": 2},
                "limitZ": {"type": "array", "items": {"type": "number"}, "minItems": 2, "maxItems": 2},
                "orientJoint": {"type": "string"},
                "orientation": {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3},
                "position": {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3},
                "radius": {"type": "float"},
                "relative": {"type": "boolean"},
                "rotationOrder": {"type": "string"},
                "scale": {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3},
                "scaleOrientation": {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3},
                "stiffnessX": {"type": "float"},
                "stiffnessY": {"type": "float"},
                "stiffnessZ": {"type": "float"},
                "symmetry": {"type": "boolean"},
                "symmetryAxis": {"type": "string"},
            },
        }
        validate(flags, schema)
        return 'joint'
