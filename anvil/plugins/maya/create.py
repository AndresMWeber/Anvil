import anvil.plugins.abstract.create as create
from anvil.plugins.maya.dependencies import *
from jsonschema import validate


class Create(create.Create):
    def initialize_flags(self, flags):
        if flags is None:
            flags = {}
        return flags

    def create_node(self, dcc_node_type, flags=None):
        function_name_query = 'create_%s' % dcc_node_type
        if hasattr(self, function_name_query):
            getattr(self, function_name_query)(flags)
        else:
            schema = {
                "type": ["object", "null"],
                "properties": {
                    "name": {"type": "string"},
                    "parent": {"type": "string"},
                    "shared": {"type": "boolean"},
                    "skipSelect": {"type": "boolean"},
                },
            }
            validate(flags, schema)
            flags = self.initialize_flags(flags)

            return pm.createNode(dcc_node_type, **flags)

    def create_transform(self, flags=None):
        schema = {
            "type": ["object", "null"],
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
        flags = self.initialize_flags(flags)
        flags['empty'] = flags.get('empty', True)
        return pm.group(**flags)

    def create_joint(self, flags=None):
        schema = {
            "type": ["object", "null"],
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
        flags = self.initialize_flags(flags)
        return pm.joint(**flags)
