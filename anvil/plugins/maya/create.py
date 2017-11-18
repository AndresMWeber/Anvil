import anvil.plugins.base.api_proxy as api_proxy
from anvil.plugins.maya.dependencies import *


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "name": {"type": "string"},
                                            "parent": {"type": "string"},
                                            "shared": {"type": "boolean"},
                                            "skipSelect": {"type": "boolean"},
                                        },
                                        },
                                       API,
                                       'createNode')
def create_node(*args, **kwargs):
    if args is None:
        raise KeyError('Node type %s is unsupported at this time' % args)


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "required": ["point"],
                                        "properties": {
                                            "name": {"type": "string"},
                                            "append": {"type": "boolean"},
                                            "bezier": {"type": "boolean"},
                                            "degree": {"type": "number"},
                                            "editPoint": api_proxy.APIProxy.POSITION_TYPE,
                                            "knot": {"type": "number"},
                                            "objectSpace": {"type": "boolean"},
                                            "periodic": {"type": "boolean"},
                                            "point": api_proxy.APIProxy.POSITION_LIST,
                                            "pointWeight": api_proxy.APIProxy.POSITION_WEIGHT_TYPE,
                                            "replace": {"type": "boolean"},
                                            "worldSpace": {"type": "boolean"},
                                        },
                                        },
                                       API,
                                       'curve')
def create_curve(*args, **kwargs):
    pass


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "name": {"type": "string"},
                                            "world": {"type": "boolean"},
                                            "parent": {},
                                            "empty": {"type": "boolean",
                                                      "default": True},
                                            "relative": {"type": "boolean"},
                                            "absolute": {"type": "boolean"},
                                        },
                                        },
                                       API,
                                       'group')
def create_transform(*args, **flags):
    pass

@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "absolute": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "angleX": {"type": "number"},
                                            "angleY": {"type": "number"},
                                            "angleZ": {"type": "number"},
                                            "assumePreferredAngles": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "automaticLimits": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "children": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "component": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "degreeOfFreedom": {"type": "string"},
                                            "exists": {"type": "string"},
                                            "limitSwitchX": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "limitSwitchY": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "limitSwitchZ": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "limitX": api_proxy.APIProxy.LINEAR_ANGLE_TYPE,
                                            "limitY": api_proxy.APIProxy.LINEAR_ANGLE_TYPE,
                                            "limitZ": api_proxy.APIProxy.LINEAR_ANGLE_TYPE,
                                            "name": {"type": "string"},
                                            "orientJoint": {"type": "string"},
                                            "orientation": api_proxy.APIProxy.POSITION_TYPE,
                                            "position": api_proxy.APIProxy.POSITION_TYPE,
                                            "radius": {"type": "number"},
                                            "relative": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "rotationOrder": {"type": "string"},
                                            "scale": api_proxy.APIProxy.POSITION_TYPE,
                                            "scaleCompensate": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "scaleOrientation": api_proxy.APIProxy.POSITION_TYPE,
                                            "secondaryAxisOrient": {"type": "string"},
                                            "setPreferredAngles": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "stiffnessX": {"type": "number"},
                                            "stiffnessY": {"type": "number"},
                                            "stiffnessZ": {"type": "number"},
                                            "symmetry": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "symmetryAxis": {"type": "string"},
                                            "zeroScaleOrient": api_proxy.APIProxy.BOOLEAN_TYPE,

                                        },
                                        },
                                       API,
                                       'joint')
def create_joint(**flags):
    pass
