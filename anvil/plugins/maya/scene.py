from anvil.plugins.maya.dependencies import *
import anvil.config as cfg
import anvil.plugins.base.api_proxy as api_proxy


@api_proxy.APIProxy.validate({"type": ["object", "null"],
                              "properties": {
                                  "activate": api_proxy.BOOL_TYPE,
                                  "activeProxy": api_proxy.BOOL_TYPE,
                                  "add": api_proxy.BOOL_TYPE,
                                  "anyModified": api_proxy.BOOL_TYPE,
                                  "applyTo": api_proxy.STR_TYPE,
                                  "buildLoadSettings": api_proxy.BOOL_TYPE,
                                  "channels": api_proxy.BOOL_TYPE,
                                  "cleanReference": api_proxy.STR_TYPE,
                                  "command": api_proxy.LINEAR_STRING_TYPE,
                                  "compress": api_proxy.BOOL_TYPE,
                                  "constraints": api_proxy.BOOL_TYPE,
                                  "constructionHistory": api_proxy.BOOL_TYPE,
                                  "copyNumberList": api_proxy.BOOL_TYPE,
                                  "defaultExtensions": api_proxy.BOOL_TYPE,
                                  "defaultNamespace": api_proxy.BOOL_TYPE,
                                  "deferReference": api_proxy.BOOL_TYPE,
                                  "editCommand": api_proxy.STR_TYPE,
                                  "errorStatus": api_proxy.BOOL_TYPE,
                                  "executeScriptNodes": api_proxy.BOOL_TYPE,
                                  "exists": api_proxy.BOOL_TYPE,
                                  "expandName": api_proxy.BOOL_TYPE,
                                  "exportAll": api_proxy.BOOL_TYPE,
                                  "exportAnim": api_proxy.BOOL_TYPE,
                                  "exportAnimFromReference": api_proxy.BOOL_TYPE,
                                  "exportAsReference": api_proxy.BOOL_TYPE,
                                  "exportAsSegment": api_proxy.BOOL_TYPE,
                                  "exportSelected": api_proxy.BOOL_TYPE,
                                  "exportSelectedAnim": api_proxy.BOOL_TYPE,
                                  "exportSelectedAnimFromReference": api_proxy.BOOL_TYPE,
                                  "exportSelectedNoReference": api_proxy.BOOL_TYPE,
                                  "exportSelectedStrict": api_proxy.BOOL_TYPE,
                                  "exportUnloadedReferences": api_proxy.BOOL_TYPE,
                                  "expressions": api_proxy.BOOL_TYPE,
                                  "fileMetaData": api_proxy.BOOL_TYPE,
                                  "flushReference": api_proxy.STR_TYPE,
                                  "force": api_proxy.BOOL_TYPE,
                                  "groupLocator": api_proxy.BOOL_TYPE,
                                  "groupName": api_proxy.STR_TYPE,
                                  "groupReference": api_proxy.BOOL_TYPE,
                                  "i": api_proxy.BOOL_TYPE,
                                  "ignoreVersion": api_proxy.BOOL_TYPE,
                                  "importFrameRate": api_proxy.BOOL_TYPE,
                                  "importReference": api_proxy.BOOL_TYPE,
                                  "importTimeRange": api_proxy.STR_TYPE,
                                  "lastFileOption": api_proxy.BOOL_TYPE,
                                  "lastTempFile": api_proxy.BOOL_TYPE,
                                  "list": api_proxy.BOOL_TYPE,
                                  "loadAllDeferred": api_proxy.BOOL_TYPE,
                                  "loadAllReferences": api_proxy.BOOL_TYPE,
                                  "loadNoReferences": api_proxy.BOOL_TYPE,
                                  "loadReference": api_proxy.STR_TYPE,
                                  "loadReferenceDepth": api_proxy.STR_TYPE,
                                  "loadReferencePreview": api_proxy.STR_TYPE,
                                  "loadSettings": api_proxy.STR_TYPE,
                                  "location": api_proxy.BOOL_TYPE,
                                  "lockContainerUnpublished": api_proxy.BOOL_TYPE,
                                  "lockFile": api_proxy.BOOL_TYPE,
                                  "lockReference": api_proxy.BOOL_TYPE,
                                  "mapPlaceHolderNamespace": api_proxy.LINEAR_STRING_TYPE,
                                  "mergeNamespaceWithParent": api_proxy.BOOL_TYPE,
                                  "mergeNamespaceWithRoot": api_proxy.BOOL_TYPE,
                                  "mergeNamespacesOnClash": api_proxy.BOOL_TYPE,
                                  "modified": api_proxy.BOOL_TYPE,
                                  "moveSelected": api_proxy.BOOL_TYPE,
                                  "namespace": api_proxy.STR_TYPE,
                                  "newFile": api_proxy.BOOL_TYPE,
                                  "open": api_proxy.BOOL_TYPE,
                                  "options": api_proxy.STR_TYPE,
                                  "parentNamespace": api_proxy.BOOL_TYPE,
                                  "postSaveScript": api_proxy.STR_TYPE,
                                  "preSaveScript": api_proxy.STR_TYPE,
                                  "preserveName": api_proxy.BOOL_TYPE,
                                  "preserveReferences": api_proxy.BOOL_TYPE,
                                  "preview": api_proxy.BOOL_TYPE,
                                  "prompt": api_proxy.BOOL_TYPE,
                                  "proxyManager": api_proxy.STR_TYPE,
                                  "proxyTag": api_proxy.STR_TYPE,
                                  "reference": api_proxy.BOOL_TYPE,
                                  "referenceDepthInfo": api_proxy.INT_TYPE,
                                  "referenceNode": api_proxy.STR_TYPE,
                                  "relativeNamespace": api_proxy.STR_TYPE,
                                  "removeDuplicateNetworks": api_proxy.BOOL_TYPE,
                                  "removeReference": api_proxy.BOOL_TYPE,
                                  "rename": api_proxy.STR_TYPE,
                                  "renameAll": api_proxy.BOOL_TYPE,
                                  "renameToSave": api_proxy.BOOL_TYPE,
                                  "renamingPrefix": api_proxy.STR_TYPE,
                                  "renamingPrefixList": api_proxy.BOOL_TYPE,
                                  "replaceName": api_proxy.LINEAR_STRING_TYPE,
                                  "resetError": api_proxy.BOOL_TYPE,
                                  "returnNewNodes": api_proxy.BOOL_TYPE,
                                  "save": api_proxy.BOOL_TYPE,
                                  "saveDiskCache": api_proxy.STR_TYPE,
                                  "saveReference": api_proxy.BOOL_TYPE,
                                  "saveReferencesUnloaded": api_proxy.BOOL_TYPE,
                                  "saveTextures": api_proxy.STR_TYPE,
                                  "sceneName": api_proxy.BOOL_TYPE,
                                  "segment": api_proxy.STR_TYPE,
                                  "selectAll": api_proxy.BOOL_TYPE,
                                  "shader": api_proxy.BOOL_TYPE,
                                  "sharedNodes": api_proxy.STR_TYPE,
                                  "sharedReferenceFile": api_proxy.BOOL_TYPE,
                                  "shortName": api_proxy.BOOL_TYPE,
                                  "strict": api_proxy.BOOL_TYPE,
                                  "swapNamespace": api_proxy.LINEAR_STRING_TYPE,
                                  "type": api_proxy.STR_TYPE,
                                  "uiConfiguration": api_proxy.BOOL_TYPE,
                                  "unloadReference": api_proxy.STR_TYPE,
                                  "unresolvedName": api_proxy.BOOL_TYPE,
                                  "usingNamespaces": api_proxy.BOOL_TYPE,
                                  "withoutCopyNumber": api_proxy.BOOL_TYPE,
                                  "writable": api_proxy.BOOL_TYPE}},
                             APIs['cmds'], 'file')
def fileop(file, **kwargs):
    pass


@api_proxy.APIProxy.validate({"type": ["object", "null"],
                              "properties": {
                                  "isAType": api_proxy.STR_TYPE,
                                  "isType": api_proxy.STR_TYPE,
                                  "tagFromType": api_proxy.STR_TYPE,
                                  "typeFromTag": api_proxy.NUM_TYPE,
                                  "typeTag": api_proxy.BOOL_TYPE, }},
                             DEFAULT_API, 'objectType')
def get_type(node, **kwargs):
    pass


@api_proxy.APIProxy.validate({"type": ["object", "null"],
                              "properties": {
                                  "apiType": api_proxy.BOOL_TYPE,
                                  "derived": api_proxy.BOOL_TYPE,
                                  "inherited": api_proxy.BOOL_TYPE,
                                  "isTypeName": api_proxy.BOOL_TYPE}},
                             DEFAULT_API, 'nodeType')
def node_type(node, apiType="", **kwargs):
    pass


@api_proxy.APIProxy.validate({"type": ["object", "null"],
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
                             DEFAULT_API, 'ls')
def list_scene(*args, **kwargs):
    pass


@api_proxy.APIProxy.validate({"type": ["object", "null"],
                              "properties": {}},
                             DEFAULT_API, 'objExists')
def exists(node):
    pass


@api_proxy.APIProxy.validate({"type": ["object", "null"],
                              "properties": {
                                  "ignoreShape": api_proxy.BOOL_TYPE,
                                  "uuid": api_proxy.BOOL_TYPE}},
                             DEFAULT_API, 'rename')
def rename(node_dag, name, **flags):
    pass


@api_proxy.APIProxy.validate({"type": ["object", "null"],
                              "properties": {
                                  "inputConnections": api_proxy.BOOL_TYPE,
                                  "instanceLeaf": api_proxy.BOOL_TYPE,
                                  "name": api_proxy.STR_TYPE,
                                  "parentOnly": api_proxy.BOOL_TYPE,
                                  "renameChildren": api_proxy.BOOL_TYPE,
                                  "returnRootsOnly": api_proxy.BOOL_TYPE,
                                  "smartTransform": api_proxy.BOOL_TYPE,
                                  "upstreamNodes": api_proxy.BOOL_TYPE}},
                             DEFAULT_API, 'duplicate')
def duplicate(parent_only=True, *node_dags, **flags):
    pass


@api_proxy.APIProxy.validate({"type": ["object", "null"],
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
                             DEFAULT_API, 'listRelatives')
def list_relatives(node_dag, **flags):
    pass


@api_proxy.APIProxy.validate({"type": ["object", "null"],
                              "properties": {
                                  "absolute": api_proxy.BOOL_TYPE,
                                  "addObject": api_proxy.BOOL_TYPE,
                                  "noConnections": api_proxy.BOOL_TYPE,
                                  "noInvScale": api_proxy.BOOL_TYPE,
                                  "relative": api_proxy.BOOL_TYPE,
                                  "removeObject": api_proxy.BOOL_TYPE,
                                  "shape": api_proxy.BOOL_TYPE,
                                  "world": api_proxy.BOOL_TYPE, }},
                             DEFAULT_API, 'parent')
def parent(node_dags, new_parent_dag=None, **flags):
    pass


@api_proxy.APIProxy.validate({"type": ["object", "null"],
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
                             DEFAULT_API, 'delete')
def delete(*node_dags, **flags):
    pass


@api_proxy.APIProxy.validate({"type": ["object", "null"],
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
                             DEFAULT_API, 'xform')
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
                if not DEFAULT_API.camera(node.getShape(), startupCamera=True, q=True):
                    nodes.append(node)

    return nodes


def get_scene_tree():
    startup_cams = [list_relatives(c, parent=True) for c in list_scene(cameras=True)
                    if DEFAULT_API.camera(c, q=True, startupCamera=True)]

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


APIWrapper = DEFAULT_API.PyNode
