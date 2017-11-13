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

        return self._log_and_run_api_call(API, 'createNode', dcc_node_type, **flags)

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
        return self._log_and_run_api_call(API, 'curve', **flags)

    def create_transform(self, flags=None):
        schema = {
            "type": ["object", "null"],
            "properties": {
                "name": {"type": "string"},
                "world": {"type": "boolean"},
                "parent": {},
                "empty": {"type": "boolean", "default": True},
                "relative": {"type": "boolean"},
                "absolute": {"type": "boolean"},
            },
        }
        validate(flags, schema)
        flags = self._initialize_and_filter_flags(flags, schema)
        flags['empty'] = flags.get('empty', True)
        return self._log_and_run_api_call(API, 'group', **flags)


# maya/create.py
@create.joint
@validate({
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
    })
def create_joint(flags=None):
    return log_and_run_api_call(API, 'joint', **flags)



# base/create.py

JOINT = 'joint'

registry = {}

def get_create_method():
    return registry[thename]

def register(name):
    pass

def joint(f):
    register(JOINT, f)
    return f


# anvil/dcc.py

def create_abstract(name):
    def wrapped(func):
        def wrappped(**flags):
            return get_create_method(name)(**flags)
        return wrappped
    return wrapped

def create_things(name, flags):
    return get_create_method(name)(flags)

# maybe double decorate here for abstracted schema
@create_abstract(JOINT)
def create_joint(**flags):
    pass

def create_curve(**flags):
    return get_create_method(CURVE)(flags)



import anvil

anvil.dcc.create_joint()