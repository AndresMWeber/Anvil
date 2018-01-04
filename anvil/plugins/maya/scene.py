from anvil.plugins.maya.dependencies import *
import anvil
import anvil.config as cfg
import anvil.plugins.base.api_proxy as api_proxy


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "isAType": api_proxy.STR_TYPE,
                                            "isType": api_proxy.STR_TYPE,
                                            "tagFromType": api_proxy.STR_TYPE,
                                            "typeFromTag": api_proxy.NUM_TYPE,
                                            "typeTag": api_proxy.BOOL_TYPE, }},
                                       API, 'objectType')
def get_type(node, **kwargs):
    pass


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "apiType": api_proxy.BOOL_TYPE,
                                            "derived": api_proxy.BOOL_TYPE,
                                            "inherited": api_proxy.BOOL_TYPE,
                                            "isTypeName": api_proxy.BOOL_TYPE}},
                                       API, 'nodeType')
def node_type(node, apiType="", **kwargs):
    pass


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "absoluteName": api_proxy.BOOL_TYPE,
                                            "allPaths": api_proxy.BOOL_TYPE,
                                            "assemblies": api_proxy.BOOL_TYPE,
                                            "cameras": api_proxy.BOOL_TYPE,
                                            "containerType": api_proxy.STR_TYPE,
                                            "containers": api_proxy.BOOL_TYPE,
                                            "dagObjects": api_proxy.BOOL_TYPE,
                                            "defaultNodes": api_proxy.BOOL_TYPE,
                                            "dependencyNodes": api_proxy.BOOL_TYPE,
                                            "exactType": api_proxy.STR_TYPE,
                                            "excludeType": api_proxy.STR_TYPE,
                                            "flatten": api_proxy.BOOL_TYPE,
                                            "geometry": api_proxy.BOOL_TYPE,
                                            "ghost": api_proxy.BOOL_TYPE,
                                            "head": api_proxy.NUM_TYPE,
                                            "hilite": api_proxy.BOOL_TYPE,
                                            "intermediateObjects": api_proxy.BOOL_TYPE,
                                            "invisible": api_proxy.BOOL_TYPE,
                                            "leaf": api_proxy.BOOL_TYPE,
                                            "lights": api_proxy.BOOL_TYPE,
                                            "live": api_proxy.BOOL_TYPE,
                                            "lockedNodes": api_proxy.BOOL_TYPE,
                                            "long": api_proxy.BOOL_TYPE,
                                            "materials": api_proxy.BOOL_TYPE,
                                            "modified": api_proxy.BOOL_TYPE,
                                            "noIntermediate": api_proxy.BOOL_TYPE,
                                            "nodeTypes": api_proxy.BOOL_TYPE,
                                            "objectsOnly": api_proxy.BOOL_TYPE,
                                            "orderedSelection": api_proxy.BOOL_TYPE,
                                            "partitions": api_proxy.BOOL_TYPE,
                                            "persistentNodes": api_proxy.BOOL_TYPE,
                                            "planes": api_proxy.BOOL_TYPE,
                                            "preSelectHilite": api_proxy.BOOL_TYPE,
                                            "readOnly": api_proxy.BOOL_TYPE,
                                            "recursive": api_proxy.BOOL_TYPE,
                                            "referencedNodes": api_proxy.BOOL_TYPE,
                                            "references": api_proxy.BOOL_TYPE,
                                            "renderGlobals": api_proxy.BOOL_TYPE,
                                            "renderQualities": api_proxy.BOOL_TYPE,
                                            "renderResolutions": api_proxy.BOOL_TYPE,
                                            "renderSetups": api_proxy.BOOL_TYPE,
                                            "selection": api_proxy.BOOL_TYPE,
                                            "sets": api_proxy.BOOL_TYPE,
                                            "shapes": api_proxy.BOOL_TYPE,
                                            "shortNames": api_proxy.BOOL_TYPE,
                                            "showNamespace": api_proxy.BOOL_TYPE,
                                            "showType": api_proxy.BOOL_TYPE,
                                            "tail": api_proxy.NUM_TYPE,
                                            "templated": api_proxy.BOOL_TYPE,
                                            "textures": api_proxy.BOOL_TYPE,
                                            "transforms": api_proxy.BOOL_TYPE,
                                            "type": api_proxy.STR_TYPE,
                                            "undeletable": api_proxy.BOOL_TYPE,
                                            "untemplated": api_proxy.BOOL_TYPE,
                                            "uuid": api_proxy.BOOL_TYPE,
                                            "visible": api_proxy.BOOL_TYPE}},
                                       API, 'ls')
def list_scene(*args, **kwargs):
    pass


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {}},
                                       API, 'objExists')
def exists(node):
    pass


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "ignoreShape": api_proxy.BOOL_TYPE,
                                            "uuid": api_proxy.BOOL_TYPE}},
                                       API, 'rename')
def rename(node_dag, name, **flags):
    pass


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "inputConnections": api_proxy.BOOL_TYPE,
                                            "instanceLeaf": api_proxy.BOOL_TYPE,
                                            "name": api_proxy.STR_TYPE,
                                            "parentOnly": api_proxy.BOOL_TYPE,
                                            "renameChildren": api_proxy.BOOL_TYPE,
                                            "returnRootsOnly": api_proxy.BOOL_TYPE,
                                            "smartTransform": api_proxy.BOOL_TYPE,
                                            "upstreamNodes": api_proxy.BOOL_TYPE}},
                                       API, 'duplicate')
def duplicate(parent_only=True, *node_dags, **flags):
    pass


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "allDescendents": api_proxy.BOOL_TYPE,
                                            "allParents": api_proxy.BOOL_TYPE,
                                            "children": api_proxy.BOOL_TYPE,
                                            "fullPath": api_proxy.BOOL_TYPE,
                                            "noIntermediate": api_proxy.BOOL_TYPE,
                                            "parent": api_proxy.BOOL_TYPE,
                                            "path": api_proxy.BOOL_TYPE,
                                            "shapes": api_proxy.BOOL_TYPE,
                                            "type": api_proxy.STR_OR_STR_LIST_TYPE}},
                                       API, 'listRelatives')
def list_relatives(node_dag, **flags):
    pass


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "absolute": api_proxy.BOOL_TYPE,
                                            "addObject": api_proxy.BOOL_TYPE,
                                            "noConnections": api_proxy.BOOL_TYPE,
                                            "noInvScale": api_proxy.BOOL_TYPE,
                                            "relative": api_proxy.BOOL_TYPE,
                                            "removeObject": api_proxy.BOOL_TYPE,
                                            "shape": api_proxy.BOOL_TYPE,
                                            "world": api_proxy.BOOL_TYPE, }},
                                       API, 'parent')
def parent(node_dags, new_parent_dag=None, **flags):
    pass


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "all": api_proxy.BOOL_TYPE,
                                            "attribute": api_proxy.STR_TYPE,
                                            "channels": api_proxy.BOOL_TYPE,
                                            "constraints": api_proxy.BOOL_TYPE,
                                            "constructionHistory": api_proxy.BOOL_TYPE,
                                            "controlPoints": api_proxy.BOOL_TYPE,
                                            "expressions": api_proxy.BOOL_TYPE,
                                            "hierarchy": api_proxy.BOOL_TYPE,
                                            "inputConnectionsAndNodes": api_proxy.BOOL_TYPE,
                                            "shape": api_proxy.BOOL_TYPE,
                                            "staticChannels": api_proxy.BOOL_TYPE,
                                            "timeAnimationCurves": api_proxy.BOOL_TYPE,
                                            "unitlessAnimationCurves": api_proxy.BOOL_TYPE}},
                                       API, 'delete')
def delete(*node_dags, **flags):
    pass


@api_proxy.APIProxy._validate_function({"type": ["object", "null"],
                                        "properties": {
                                            "absolute": api_proxy.BOOL_TYPE,
                                            "boundingBox": api_proxy.BOOL_TYPE,
                                            "boundingBoxInvisible": api_proxy.BOOL_TYPE,
                                            "centerPivots": api_proxy.BOOL_TYPE,
                                            "centerPivotsOnComponents": api_proxy.BOOL_TYPE,
                                            "deletePriorHistory": api_proxy.BOOL_TYPE,
                                            "euler": api_proxy.BOOL_TYPE,
                                            "matrix": api_proxy.QUERYABLE_MATRIX,
                                            "pivots": api_proxy.QUERYABLE_POSITION,
                                            "objectSpace": api_proxy.BOOL_TYPE,
                                            "preserve": api_proxy.BOOL_TYPE,
                                            "preserveUV": api_proxy.BOOL_TYPE,
                                            "reflection": api_proxy.BOOL_TYPE,
                                            "reflectionAboutBBox": api_proxy.BOOL_TYPE,
                                            "reflectionAboutOrigin": api_proxy.BOOL_TYPE,
                                            "reflectionAboutX": api_proxy.BOOL_TYPE,
                                            "reflectionAboutY": api_proxy.BOOL_TYPE,
                                            "reflectionAboutZ": api_proxy.BOOL_TYPE,
                                            "reflectionTolerance": api_proxy.NUM_TYPE,
                                            "relative": api_proxy.BOOL_TYPE,
                                            "rotateAxis": api_proxy.QUERYABLE_POSITION,
                                            "rotateOrder": api_proxy.STR_TYPE,
                                            "rotatePivot": api_proxy.QUERYABLE_POSITION,
                                            "rotateTranslation": api_proxy.QUERYABLE_POSITION,
                                            "rotation": api_proxy.QUERYABLE_POSITION,
                                            "scale": api_proxy.QUERYABLE_POSITION,
                                            "scalePivot": api_proxy.QUERYABLE_POSITION,
                                            "scaleTranslation": api_proxy.QUERYABLE_POSITION,
                                            "shear": api_proxy.QUERYABLE_POSITION,
                                            "translation": api_proxy.QUERYABLE_POSITION,
                                            "worldSpace": api_proxy.BOOL_TYPE,
                                            "worldSpaceDistance": api_proxy.BOOL_TYPE,
                                            "zeroTransformPivots": api_proxy.BOOL_TYPE,
                                            "query": api_proxy.BOOL_TYPE}},
                                       API, 'xform')
def position(*node_dags, **flags):
    pass


def is_exact_type(node, typename):
    return get_type(node) == typename


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


def get_persistent_id(node_unicode_proxy):
    try:
        selection_list = om.MSelectionList()
        if cfg.ATTR_DELIMITER in node_unicode_proxy and not '[' in node_unicode_proxy:
            node_name, attr_name = node_unicode_proxy.split('.')
            selection_list.add(node_name)
            depend_node = om.MFnDependencyNode(selection_list.getDependNode(0))
            return depend_node.findPlug(attr_name, False)

        selection_list.add(str(node_unicode_proxy))
        return selection_list.getDagPath(0)

    except RuntimeError:
        raise KeyError('Requested node-ID %r does not exist in the scene.' % node_unicode_proxy)


def get_path_from_api_object(mobject):
    return om.MDagPath.getAPathTo(mobject)


APIWrapper = API.PyNode
