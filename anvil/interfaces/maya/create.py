import anvil.interfaces.api_proxy as api_proxy
from anvil.interfaces.maya.dependencies import *
import anvil.config as cfg


@api_proxy.APIProxy.validate({"type": ["object", "null"],
                                        "properties": {
                                            "name": api_proxy.STR_TYPE,
                                            "parent": api_proxy.STR_TYPE,
                                            "shared": api_proxy.BOOL_TYPE,
                                            "skipSelect": api_proxy.BOOL_TYPE, }},
                             DEFAULT_API, 'createNode')
def create_node(*args, **kwargs):
    if args is None:
        raise KeyError('Node type %s is unsupported at this time' % args)


@api_proxy.APIProxy.validate({"type": ["object", "null"],
                                        "required": ["point"],
                                        "properties": {
                                            "name": api_proxy.STR_TYPE,
                                            "append": api_proxy.BOOL_TYPE,
                                            "bezier": api_proxy.BOOL_TYPE,
                                            "degree": api_proxy.NUM_TYPE,
                                            "editPoint": api_proxy.POSITION_TYPE,
                                            "knot": api_proxy.NUM_TYPE,
                                            "objectSpace": api_proxy.BOOL_TYPE,
                                            "periodic": api_proxy.BOOL_TYPE,
                                            "point": api_proxy.POSITION_LIST,
                                            "pointWeight": api_proxy.POSITION_WEIGHT_TYPE,
                                            "replace": api_proxy.BOOL_TYPE,
                                            "worldSpace": api_proxy.BOOL_TYPE, }},
                             DEFAULT_API, 'curve')
def create_curve(*args, **kwargs):
    pass


@api_proxy.APIProxy.validate({"type": ["object", "null"],
                                        "properties": {
                                            "name": api_proxy.STR_TYPE,
                                            "world": api_proxy.BOOL_TYPE,
                                            "parent": {},
                                            "empty": {cfg.TYPE: cfg.BOOLEAN, cfg.DEFAULT: True},
                                            "relative": api_proxy.BOOL_TYPE,
                                            "absolute": api_proxy.BOOL_TYPE}},
                             DEFAULT_API, 'group')
def create_transform(*args, **flags):
    pass


@api_proxy.APIProxy.validate({"type": ["object", "null"],
                                        "properties": {
                                            "absolute": api_proxy.BOOL_TYPE,
                                            "angleX": api_proxy.NUM_TYPE,
                                            "angleY": api_proxy.NUM_TYPE,
                                            "angleZ": api_proxy.NUM_TYPE,
                                            "assumePreferredAngles": api_proxy.BOOL_TYPE,
                                            "automaticLimits": api_proxy.BOOL_TYPE,
                                            "children": api_proxy.BOOL_TYPE,
                                            "component": api_proxy.BOOL_TYPE,
                                            "degreeOfFreedom": api_proxy.STR_TYPE,
                                            "exists": api_proxy.STR_TYPE,
                                            "limitSwitchX": api_proxy.BOOL_TYPE,
                                            "limitSwitchY": api_proxy.BOOL_TYPE,
                                            "limitSwitchZ": api_proxy.BOOL_TYPE,
                                            "limitX": api_proxy.LINEAR_ANGLE_TYPE,
                                            "limitY": api_proxy.LINEAR_ANGLE_TYPE,
                                            "limitZ": api_proxy.LINEAR_ANGLE_TYPE,
                                            "name": api_proxy.STR_TYPE,
                                            "orientJoint": api_proxy.STR_TYPE,
                                            "orientation": api_proxy.POSITION_TYPE,
                                            "position": api_proxy.POSITION_TYPE,
                                            "radius": api_proxy.NUM_TYPE,
                                            "relative": api_proxy.BOOL_TYPE,
                                            "rotationOrder": api_proxy.STR_TYPE,
                                            "scale": api_proxy.POSITION_TYPE,
                                            "scaleCompensate": api_proxy.BOOL_TYPE,
                                            "scaleOrientation": api_proxy.POSITION_TYPE,
                                            "secondaryAxisOrient": api_proxy.STR_TYPE,
                                            "setPreferredAngles": api_proxy.BOOL_TYPE,
                                            "stiffnessX": api_proxy.NUM_TYPE,
                                            "stiffnessY": api_proxy.NUM_TYPE,
                                            "stiffnessZ": api_proxy.NUM_TYPE,
                                            "symmetry": api_proxy.BOOL_TYPE,
                                            "symmetryAxis": api_proxy.STR_TYPE,
                                            "zeroScaleOrient": api_proxy.BOOL_TYPE}},
                             DEFAULT_API, 'joint')
def create_joint(**flags):
    pass
