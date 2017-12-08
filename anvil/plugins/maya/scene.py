from anvil.plugins.maya.dependencies import *
import anvil
import anvil.plugins.base.api_proxy as api_proxy


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "isAType": {"type": "string"},
                                            "isType": {"type": "string"},
                                            "tagFromType": {"type": "string"},
                                            "typeFromTag": {"type": "number"},
                                            "typeTag": api_proxy.APIProxy.BOOLEAN_TYPE,
                                        },
                                        },
                                       API,
                                       'objectType')
def get_type(node, **kwargs):
    pass


def is_exact_type(node, typename):
    return get_type(node) == typename


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "apiType": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "derived": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "inherited": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "isTypeName": api_proxy.APIProxy.BOOLEAN_TYPE,
                                        },
                                        },
                                       API,
                                       'nodeType')
def node_type(node, apiType="", **kwargs):
    pass


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "absoluteName": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "allPaths": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "assemblies": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "cameras": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "containerType": {"type": "string"},
                                            "containers": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "dagObjects": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "defaultNodes": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "dependencyNodes": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "exactType": {"type": "string"},
                                            "excludeType": {"type": "string"},
                                            "flatten": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "geometry": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "ghost": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "head": {"type": "number"},
                                            "hilite": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "intermediateObjects": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "invisible": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "leaf": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "lights": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "live": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "lockedNodes": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "long": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "materials": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "modified": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "noIntermediate": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "nodeTypes": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "objectsOnly": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "orderedSelection": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "partitions": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "persistentNodes": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "planes": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "preSelectHilite": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "readOnly": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "recursive": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "referencedNodes": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "references": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "renderGlobals": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "renderQualities": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "renderResolutions": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "renderSetups": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "selection": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "sets": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "shapes": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "shortNames": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "showNamespace": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "showType": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "tail": {"type": "number"},
                                            "templated": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "textures": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "transforms": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "type": {"type": "string"},
                                            "undeletable": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "untemplated": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "uuid": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "visible": api_proxy.APIProxy.BOOLEAN_TYPE
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
                                            "ignoreShape": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "uuid": api_proxy.APIProxy.BOOLEAN_TYPE
                                        },
                                        },
                                       API,
                                       'rename')
def rename(node_dag, name, **flags):
    pass


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "inputConnections": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "instanceLeaf": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "name": {"type": "string"},
                                            "parentOnly": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "renameChildren": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "returnRootsOnly": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "smartTransform": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "upstreamNodes": api_proxy.APIProxy.BOOLEAN_TYPE
                                        },
                                        },
                                       API,
                                       'duplicate')
def duplicate(parent_only=True, *node_dags, **flags):
    pass


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "allDescendents": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "allParents": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "children": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "fullPath": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "noIntermediate": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "parent": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "path": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "shapes": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "type": api_proxy.APIProxy.STR_OR_STR_LIST_TYPE,
                                        },
                                        },
                                       API,
                                       'listRelatives')
def list_relatives(node_dag, **flags):
    pass


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "absolute": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "addObject": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "noConnections": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "noInvScale": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "relative": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "removeObject": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "shape": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "world": api_proxy.APIProxy.BOOLEAN_TYPE,
                                        }
                                        },
                                       API,
                                       'parent')
def parent(node_dags, new_parent_dag=None, **flags):
    pass


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "all": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "attribute": {"type": "string"},
                                            "channels": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "constraints": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "constructionHistory": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "controlPoints": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "expressions": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "hierarchy": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "inputConnectionsAndNodes": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "shape": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "staticChannels": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "timeAnimationCurves": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "unitlessAnimationCurves": api_proxy.APIProxy.BOOLEAN_TYPE,
                                        }
                                        },
                                       API,
                                       'delete')
def delete(*node_dags, **flags):
    pass


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "absolute": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "boundingBox": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "boundingBoxInvisible": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "centerPivots": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "centerPivotsOnComponents": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "deletePriorHistory": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "euler": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "matrix": api_proxy.APIProxy.QUERYABLE_MATRIX,
                                            "pivots": api_proxy.APIProxy.QUERYABLE_POSITION,
                                            "objectSpace": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "preserve": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "preserveUV": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "reflection": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "reflectionAboutBBox": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "reflectionAboutOrigin": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "reflectionAboutX": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "reflectionAboutY": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "reflectionAboutZ": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "reflectionTolerance": {"type": "number"},
                                            "relative": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "rotateAxis": api_proxy.APIProxy.QUERYABLE_POSITION,
                                            "rotateOrder": {"type": "string"},
                                            "rotatePivot": api_proxy.APIProxy.QUERYABLE_POSITION,
                                            "rotateTranslation": api_proxy.APIProxy.QUERYABLE_POSITION,
                                            "rotation": api_proxy.APIProxy.QUERYABLE_POSITION,
                                            "scale": api_proxy.APIProxy.QUERYABLE_POSITION,
                                            "scalePivot": api_proxy.APIProxy.QUERYABLE_POSITION,
                                            "scaleTranslation": api_proxy.APIProxy.QUERYABLE_POSITION,
                                            "shear": api_proxy.APIProxy.QUERYABLE_POSITION,
                                            "translation": api_proxy.APIProxy.QUERYABLE_POSITION,
                                            "worldSpace": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "worldSpaceDistance": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "zeroTransformPivots": api_proxy.APIProxy.BOOLEAN_TYPE,
                                            "query": api_proxy.APIProxy.BOOLEAN_TYPE,
                                        }
                                        },
                                       API,
                                       'xform')
def position(*node_dags, **flags):
    pass


def is_types(node, types):
    return any([get_type(node) == object_type for object_type in types])


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
    startup_cams = [list_relatives(c, parent=True) for c in list_scene(cameras=True)
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


def node_hierarchy_as_dict(nodes, tree=None, node_filter=None):
    if not isinstance(nodes, list):
        nodes = [nodes]

    if tree is None:
        tree = dict()

    for tree_child in nodes:
        anvil_node = anvil.factory(tree_child)
        try:
            relative_tree = tree[anvil_node]
        except KeyError:
            tree[anvil_node] = dict()
            relative_tree = tree[anvil_node]

        node_filter_kwargs = {'type': node_filter} if node_filter else {}
        children = list_relatives(tree_child, fullPath=True, children=True, **node_filter_kwargs) or []
        if children:
            node_hierarchy_as_dict(children, relative_tree, node_filter=node_filter)

    return tree


def get_persistent_id(node_unicode_proxy):
    try:
        selection_list = om.MSelectionList()
        selection_list.add(str(node_unicode_proxy))
        return selection_list.getDagPath(0)
    except RuntimeError:
        raise KeyError('Requested node-ID %r does not exist in the scene.' % node_unicode_proxy)


APIWrapper = API.PyNode
