import anvil.plugins.base.connections as connections
from anvil.plugins.maya.dependencies import *
import anvil.plugins.base.api_proxy as api_proxy

m_api = pm


class Attribute(connections.Attribute):
    def get(object, attr, **flags):
        return m_api.getAttr(object, attr)

    def set(object, attr, value, **flags):
        return m_api.setAttr(object, attr, value, **flags)


default_schema = {
    "type": ["object", "null"],
    "properties": {
        "layer": {"type": "string"},
        "name": {"type": "string"},
        "remove": {"type": "boolean"},
        "targetList": {"type": "boolean"},
        "weight": {"type": "number"},
        "weightAliasList": {"type": "boolean"},
    },
}

cacheable_schema = {
    "createCache": {"type": "array", "items": {"type": "number"}, "minItems": 2, "maxItems": 2},
    "deleteCache": {"type": "boolean"},
}

offset_schema = {
    "maintainOffset": {"type": "boolean"},
    "offset": {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3},
    "skip": {"type": "string"},
}

aim_schema = {
    "aimVector": {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3},
    "upVector": {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3},
    "worldUpObject": {"type": "string"},
    "worldUpType": {"type": "string"},
    "worldUpVector": {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3},
}


def merge_dicts(*dicts):
    result = {}
    for dictionary in dicts:
        result.update(dictionary)
    return result


@api_proxy.APIProxy._validate_function(merge_dicts(default_schema, offset_schema),
                                       API,
                                       'pointConstraint')
def translate(source, targets, **flags):
    pass


@api_proxy.APIProxy._validate_function(merge_dicts(default_schema, offset_schema, cacheable_schema),
                                       API,
                                       'orientConstraint')
def rotate(source, targets, **flags):
    pass


@api_proxy.APIProxy._validate_function(merge_dicts(default_schema, offset_schema, aim_schema),
                                       API,
                                       'aimConstraint')
def aim(source, targets, **flags):
    pass


@api_proxy.APIProxy._validate_function(merge_dicts({"properties":
                                                        {"scaleCompensate": {"type": "boolean"},
                                                         "targetList": {"type": "boolean"}, },
                                                    },
                                                   default_schema,
                                                   offset_schema),
                                       API,
                                       'scaleConstraint')
def scale(source, targets, **flags):
    pass


@api_proxy.APIProxy._validate_function(merge_dicts({"properties":
                                                        {"decompRotationToChild": {"type": "boolean"},
                                                         "skipRotate": {"type": "string"},
                                                         "skipTranslate": {"type": "string"},
                                                         },
                                                    },
                                                   default_schema,
                                                   offset_schema,
                                                   cacheable_schema),
                                       API,
                                       'parentConstraint')
def parent(source, targets, **flags):
    pass


@api_proxy.APIProxy._validate_function(merge_dicts(default_schema, aim_schema),
                                       API,
                                       'tangentConstraint')
def tangent(source, targets, **flags):
    pass


@api_proxy.APIProxy._validate_function(merge_dicts(default_schema),
                                       API,
                                       'geometryConstraint')
def geometry_point(source, targets, **flags):
    pass


@api_proxy.APIProxy._validate_function(merge_dicts(default_schema, aim_schema),
                                       API,
                                       'normalConstraint')
def geometry_normal(source, targets, **flags):
    pass


@api_proxy.APIProxy._validate_function(merge_dicts(default_schema),
                                       API,
                                       'poleVectorConstraint')
def pole_vector(source, targets, **flags):
    pass
