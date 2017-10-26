from anvil.plugins.maya.dependencies import *
import anvil.plugins.base.scene as scene
from jsonschema import validate




class Scene(scene.Scene):
    def get_persistent_id(self, node_unicode_proxy):
        selection_list = om.MSelectionList()
        selection_list.add(str(node_unicode_proxy))
        return selection_list.getDagPath(0)

    def get_type(self, node, **kwargs):
        return str(self._log_and_run_api_call(API, 'objectType', node, **kwargs))

    def is_exact_type(self, node, typename):
        return type(node) == typename

    def is_type(self, node, typename):
        self.CURRENT_API = None
        return typename in API.nodeType(node, inherited=True)

    def get_scene_tree(self):
        startup_cams = [API.listRelatives(c, p=True)[0] for c in mc.ls(cameras=True)
                        if API.camera(c, q=True, startupCamera=True)]

        top_level_transforms = [node for node in API.ls(assemblies=True)
                                if node not in startup_cams]

        def recurse_scene_nodes(nodes, tree=None):
            if tree is None:
                tree = {tree_child.split('|')[-1]: dict() for tree_child in nodes}
            elif not tree:
                for tree_child in nodes:
                    tree[tree_child.split('|')[-1]] = dict()

            for tree_child in nodes:
                relative_tree = tree[tree_child.split('|')[-1]]
                children = API.listRelatives(tree_child, fullPath=True, children=True, type='transform')
                if children:
                    recurse_scene_nodes(children, relative_tree)

            return tree

        return recurse_scene_nodes(top_level_transforms)

    def list_scene_nodes(self, object_type='transform', has_shape=False):
        nodes = []
        for node in API.ls(type=object_type):
            if not node.getShape():
                nodes.append(node)
            else:
                if not node.getShape().type() == 'camera':
                    nodes.append(node)
                else:
                    if not API.camera(node.getShape(), startupCamera=True, q=True):
                        nodes.append(node)

        return nodes

    def list_scene(self, node_dags=None, **flags):
        schema = {"type": ["object", "null"],
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
                  }

        validate(flags, schema)
        if node_dags:
            return self._log_and_run_api_call(API, 'ls', node_dags, **flags)
        else:
            return self._log_and_run_api_call(API, 'ls', **flags)

    def exists(self, *nodes):
        return all([API.objExists(node) if node else False for node in nodes])

    def safe_delete(self, node_or_nodes):
        if isinstance(node_or_nodes, list):
            for node in node_or_nodes:
                try:
                    self._log_and_run_api_call(API, 'delete', node)
                except ValueError:
                    pass
        else:
            try:
                self._log_and_run_api_call(API, 'delete', node_or_nodes)
            except ValueError:
                pass

    def rename(self, node_dag, name, **flags):
        if not name:
            return node_dag
        return self._log_and_run_api_call(API, 'rename', node_dag, name, **flags)

    def duplicate(self, node_dag, parent_only=True, **flags):
        return self._log_and_run_api_call(API, 'duplicate', node_dag, parentOnly=parent_only, **flags)

    def list_relatives(self, node_dag, **flags):
        schema = {
            "type": ["object", "null"],
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
        }
        validate(flags, schema)
        return self._log_and_run_api_call(API, 'listRelatives', node_dag, **flags)

    def parent(self, node_dags, new_parent_dag, **flags):
        schema = {
            "type": ["object", "null"],
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
        }
        if node_dags is not None and new_parent_dag is not None:
            validate(flags, schema)
            try:
                return self._log_and_run_api_call(API, 'parent', node_dags, new_parent_dag, **flags)
            except RuntimeError as e:
                self.API_LOG.info('# Child was already parented to that dag node.')
            except API.general.MayaNodeError:
                self.API_LOG.info('# Invalid parent(%s) or child(%s.' % (new_parent_dag, node_dags))

    def delete(self, node_dags, **flags):
        schema = {
            "type": ["object", "null"],
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
        }
        validate(flags, schema)
        return self._log_and_run_api_call(API, 'delete', node_dags, **flags)
