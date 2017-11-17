from anvil.plugins.maya.dependencies import *
import anvil.plugins.base.api_proxy as api_proxy


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "isAType": {"type": "string"},
                                            "isType": {"type": "string"},
                                            "tagFromType": {"type": "string"},
                                            "typeFromTag": {"type": "number"},
                                            "typeTag": {"type": "boolean"},
                                        },
                                        },
                                       API,
                                       'objectType')
def get_type(node, **kwargs):
    pass


def is_exact_type(node, typename):
    return type(node) == typename


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "apiType": {"type": "boolean"},
                                            "derived": {"type": "boolean"},
                                            "inherited": {"type": "boolean"},
                                            "isTypeName": {"type": "boolean"},
                                        },
                                        },
                                       API,
                                       'nodeType')
def is_type(node, apiType="", **kwargs):
    pass


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "absoluteName": {"type": "boolean"},
                                            "allPaths": {"type": "boolean"},
                                            "assemblies": {"type": "boolean"},
                                            "cameras": {"type": "boolean"},
                                            "containerType": {"type": "string"},
                                            "containers": {"type": "boolean"},
                                            "dagObjects": {"type": "boolean"},
                                            "defaultNodes": {"type": "boolean"},
                                            "dependencyNodes": {"type": "boolean"},
                                            "exactType": {"type": "string"},
                                            "excludeType": {"type": "string"},
                                            "flatten": {"type": "boolean"},
                                            "geometry": {"type": "boolean"},
                                            "ghost": {"type": "boolean"},
                                            "head": {"type": "number"},
                                            "hilite": {"type": "boolean"},
                                            "intermediateObjects": {"type": "boolean"},
                                            "invisible": {"type": "boolean"},
                                            "leaf": {"type": "boolean"},
                                            "lights": {"type": "boolean"},
                                            "live": {"type": "boolean"},
                                            "lockedNodes": {"type": "boolean"},
                                            "long": {"type": "boolean"},
                                            "materials": {"type": "boolean"},
                                            "modified": {"type": "boolean"},
                                            "noIntermediate": {"type": "boolean"},
                                            "nodeTypes": {"type": "boolean"},
                                            "objectsOnly": {"type": "boolean"},
                                            "orderedSelection": {"type": "boolean"},
                                            "partitions": {"type": "boolean"},
                                            "persistentNodes": {"type": "boolean"},
                                            "planes": {"type": "boolean"},
                                            "preSelectHilite": {"type": "boolean"},
                                            "readOnly": {"type": "boolean"},
                                            "recursive": {"type": "boolean"},
                                            "referencedNodes": {"type": "boolean"},
                                            "references": {"type": "boolean"},
                                            "renderGlobals": {"type": "boolean"},
                                            "renderQualities": {"type": "boolean"},
                                            "renderResolutions": {"type": "boolean"},
                                            "renderSetups": {"type": "boolean"},
                                            "selection": {"type": "boolean"},
                                            "sets": {"type": "boolean"},
                                            "shapes": {"type": "boolean"},
                                            "shortNames": {"type": "boolean"},
                                            "showNamespace": {"type": "boolean"},
                                            "showType": {"type": "boolean"},
                                            "tail": {"type": "number"},
                                            "templated": {"type": "boolean"},
                                            "textures": {"type": "boolean"},
                                            "transforms": {"type": "boolean"},
                                            "type": {"type": "string"},
                                            "undeletable": {"type": "boolean"},
                                            "untemplated": {"type": "boolean"},
                                            "uuid": {"type": "boolean"},
                                            "visible": {"type": "boolean"}
                                        }
                                        },
                                       API,
                                       'ls')
def list_scene(*args, **kwargs):
    pass


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {},
                                        },
                                       API,
                                       'objExists')
def exists(node):
    pass


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "ignoreShape": {"type": "boolean"},
                                            "uuid": {"type": "boolean"}
                                        },
                                        },
                                       API,
                                       'rename')
def rename(node_dag, name, **flags):
    pass


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "inputConnections": {"type": "boolean"},
                                            "instanceLeaf": {"type": "boolean"},
                                            "name": {"type": "string"},
                                            "parentOnly": {"type": "boolean"},
                                            "renameChildren": {"type": "boolean"},
                                            "returnRootsOnly": {"type": "boolean"},
                                            "smartTransform": {"type": "boolean"},
                                            "upstreamNodes": {"type": "boolean"}
                                        },
                                        },
                                       API,
                                       'duplicate')
def duplicate(parent_only=True, *node_dags, **flags):
    pass


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "allDescendents": {"type": "boolean"},
                                            "allParents": {"type": "boolean"},
                                            "children": {"type": "boolean"},
                                            "fullPath": {"type": "boolean"},
                                            "noIntermediate": {"type": "boolean"},
                                            "parent": {"type": "boolean"},
                                            "path": {"type": "boolean"},
                                            "shapes": {"type": "boolean"},
                                            "type": {"type": "string"},
                                        },
                                        },
                                       API,
                                       'listRelatives')
def list_relatives(node_dag, **flags):
    pass


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "absolute": {"type": "boolean"},
                                            "addObject": {"type": "boolean"},
                                            "noConnections": {"type": "boolean"},
                                            "noInvScale": {"type": "boolean"},
                                            "relative": {"type": "boolean"},
                                            "removeObject": {"type": "boolean"},
                                            "shape": {"type": "boolean"},
                                            "world": {"type": "boolean"},
                                        }
                                        },
                                       API,
                                       'parent')
def parent(node_dags, new_parent_dag, **flags):
    pass


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "all": {"type": "boolean"},
                                            "attribute": {"type": "string"},
                                            "channels": {"type": "boolean"},
                                            "constraints": {"type": "boolean"},
                                            "constructionHistory": {"type": "boolean"},
                                            "controlPoints": {"type": "boolean"},
                                            "expressions": {"type": "boolean"},
                                            "hierarchy": {"type": "boolean"},
                                            "inputConnectionsAndNodes": {"type": "boolean"},
                                            "shape": {"type": "boolean"},
                                            "staticChannels": {"type": "boolean"},
                                            "timeAnimationCurves": {"type": "boolean"},
                                            "unitlessAnimationCurves": {"type": "boolean"},
                                        }
                                        },
                                       API,
                                       'delete')
def delete(*node_dags, **flags):
    pass


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "absolute": {"type": "boolean"},
                                            "boundingBox": {"type": "boolean"},
                                            "boundingBoxInvisible": {"type": "boolean"},
                                            "centerPivots": {"type": "boolean"},
                                            "centerPivotsOnComponents": {"type": "boolean"},
                                            "deletePriorHistory": {"type": "boolean"},
                                            "euler": {"type": "boolean"},
                                            "matrix": {"type": "array", "items": {"type": "number"}, "minItems": 16,
                                                       "maxItems": 16},
                                            "pivots": {"type": "array", "items": {"type": "number"}, "minItems": 3,
                                                       "maxItems": 3},
                                            "objectSpace": {"type": "boolean"},
                                            "preserve": {"type": "boolean"},
                                            "preserveUV": {"type": "boolean"},
                                            "reflection": {"type": "boolean"},
                                            "reflectionAboutBBox": {"type": "boolean"},
                                            "reflectionAboutOrigin": {"type": "boolean"},
                                            "reflectionAboutX": {"type": "boolean"},
                                            "reflectionAboutY": {"type": "boolean"},
                                            "reflectionAboutZ": {"type": "boolean"},
                                            "reflectionTolerance": {"type": "number"},
                                            "relative": {"type": "boolean"},
                                            "rotateAxis": {"type": "array", "items": {"type": "number"}, "minItems": 3,
                                                           "maxItems": 3},
                                            "rotateOrder": {"type": "string"},
                                            "rotatePivot": {"type": "array", "items": {"type": "number"}, "minItems": 3,
                                                            "maxItems": 3},
                                            "rotateTranslation": {"type": "array", "items": {"type": "number"},
                                                                  "minItems": 3,
                                                                  "maxItems": 3},
                                            "rotation": {"type": "array", "items": {"type": "number"}, "minItems": 3,
                                                         "maxItems": 3},
                                            "scale": {"type": "array", "items": {"type": "number"}, "minItems": 3,
                                                      "maxItems": 3},
                                            "scalePivot": {"type": "array", "items": {"type": "number"}, "minItems": 3,
                                                           "maxItems": 3},
                                            "scaleTranslation": {"type": "array", "items": {"type": "number"},
                                                                 "minItems": 3,
                                                                 "maxItems": 3},
                                            "shear": {"type": "array", "items": {"type": "number"}, "minItems": 3,
                                                      "maxItems": 3},
                                            "translation": {"type": "array", "items": {"type": "number"}, "minItems": 3,
                                                            "maxItems": 3},
                                            "worldSpace": {"type": "boolean"},
                                            "worldSpaceDistance": {"type": "boolean"},
                                            "zeroTransformPivots": {"type": "boolean"},
                                        }
                                        },
                                       API,
                                       'xform')
def position(*node_dags, **flags):
    pass


def safe_delete(node_or_nodes):
    if isinstance(node_or_nodes, list):
        for node in node_or_nodes:
            try:
                delete(node)
            except ValueError:
                pass
    else:
        try:
            delete(node_or_nodes)
        except ValueError:
            pass


def objects_exist(nodes):
    return all([exists(node) for node in nodes])


def list_scene_nodes(object_type='transform', has_shape=False):
    nodes = []
    for node in list_scene(type=object_type):
        if not node.getShape():
            nodes.append(node)
        else:
            if not node.getShape().type() == 'camera':
                nodes.append(node)
            else:
                if not API.camera(node.getShape(), startupCamera=True, q=True):
                    nodes.append(node)

    return nodes


def get_scene_tree():
    startup_cams = [list_relatives(c, p=True) for c in list_scene(cameras=True)
                    if API.camera(c, q=True, startupCamera=True)]

    top_level_transforms = [node for node in list_scene(assemblies=True)
                            if node not in startup_cams]

    def recurse_scene_nodes(nodes, tree=None):
        if tree is None:
            tree = {tree_child.split('|')[-1]: dict() for tree_child in nodes}
        elif not tree:
            for tree_child in nodes:
                tree[tree_child.split('|')[-1]] = dict()

        for tree_child in nodes:
            relative_tree = tree[tree_child.split('|')[-1]]
            children = list_relatives(tree_child, fullPath=True, children=True, type='transform')
            if children:
                recurse_scene_nodes(children, relative_tree)

        return tree

    return recurse_scene_nodes(top_level_transforms)


def get_persistent_id(node_unicode_proxy):
    selection_list = om.MSelectionList()
    selection_list.add(str(node_unicode_proxy))
    return selection_list.getDagPath(0)
