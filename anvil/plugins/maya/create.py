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
def create_curve(*args, **kwargs):
    if args is None:
        raise KeyError('Node type %s is unsupported at this time' % args)


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "required": ["point"],
                                        "properties": {
                                            "name": {"type": "string"},
                                            "append": {"type": "boolean"},
                                            "bezier": {"type": "boolean"},
                                            "degree": {"type": "number"},
                                            "editPoint": {"type": "array", "items": {"type": "number"}, "minItems": 3,
                                                          "maxItems": 3},
                                            "knot": {"type": "number"},
                                            "objectSpace": {"type": "boolean"},
                                            "periodic": {"type": "boolean"},
                                            "point": {"type": "array",
                                                      "items": {"type": "array",
                                                                "items": {"type": "number"},
                                                                "minItems": 3,
                                                                "maxItems": 3}
                                                      },
                                            "pointWeight": {"type": "array", "items": {"type": "number"}, "minItems": 4,
                                                            "maxItems": 4},
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
                                            "empty": {"type": "boolean", "default": True},
                                            "relative": {"type": "boolean"},
                                            "absolute": {"type": "boolean"},
                                        },
                                        },
                                       API,
                                       'group')
def create_transform(flags=None):
    flags['empty'] = flags.get('empty', True)
