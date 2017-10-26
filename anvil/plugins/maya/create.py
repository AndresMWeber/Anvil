import anvil.plugins.base.create as create
from anvil.plugins.maya.dependencies import *
from jsonschema import validate

m_api = pm


class Create(create.Create):
    def create_node(self, dcc_node_type, flags=None):
        if dcc_node_type is None:
            raise KeyError('Node type %s is unsupported at this time' % dcc_node_type)
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
        flags = self._initialize_and_filter_flags(flags, schema)

        return m_api.createNode(dcc_node_type, **flags)

    def create_curve(self, flags=None):
        schema = {
            "type": ["object", "null"],
            "required": ["point"],
            "properties": {
                "name": {"type": "string"},
                "append": {"type": "boolean"},
                "bezier": {"type": "boolean"},
                "degree": {"type": "number"},
                "editPoint": {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3},
                "knot": {"type": "number"},
                "objectSpace": {"type": "boolean"},
                "periodic": {"type": "boolean"},
                "point": {"type": "array",
                          "items": {"type": "array",
                                    "items": {"type": "number"},
                                    "minItems": 3,
                                    "maxItems": 3}
                          },
                "pointWeight": {"type": "array", "items": {"type": "number"}, "minItems": 4, "maxItems": 4},
                "replace": {"type": "boolean"},
                "worldSpace": {"type": "boolean"},
            },
        }
        validate(flags, schema)
        flags = self._initialize_and_filter_flags(flags, schema)
        return m_api.curve(**flags)

    def create_transform(self, flags=None):
        schema = {
            "type": ["object", "null"],
            "properties": {
                "name": {"type": "string"},
                "world": {"type": "boolean"},
                "parent": {},
                "empty": {"type": "boolean"},
                "relative": {"type": "boolean"},
                "absolute": {"type": "boolean"},
            },
        }
        validate(flags, schema)
        flags = self._initialize_and_filter_flags(flags, schema)
        flags['empty'] = flags.get('empty', True)
        return m_api.group(**flags)

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
                "radius": {"type": "number"},
                "relative": {"type": "boolean"},
                "rotationOrder": {"type": "string"},
                "scale": {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3},
                "scaleOrientation": {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3},
                "stiffnessX": {"type": "number"},
                "stiffnessY": {"type": "number"},
                "stiffnessZ": {"type": "number"},
                "symmetry": {"type": "boolean"},
                "symmetryAxis": {"type": "string"},
            },
        }
        validate(flags, schema)
        flags = self._initialize_and_filter_flags(flags, schema)
        return m_api.joint(**flags)
