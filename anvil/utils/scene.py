import anvil
import anvil.runtime as rt
import anvil.config as cfg
from generic import to_list
from pprint import pprint


def is_exact_type(node, typename):
    return rt.dcc.scene.get_type(node) == typename


def is_types(node, types):
    return any([rt.dcc.scene.get_type(node) == object_type for object_type in types])


def safe_delete(node_or_nodes):
    node_or_nodes = to_list(node_or_nodes)
    for node in node_or_nodes:
        try:
            rt.dcc.scene.delete(node)
        except:  # noqa
            pass


def objects_exist(*nodes):
    return all(
        [node.exists() if anvil.is_anvil(node) else rt.dcc.scene.exists(node) if node else False for node in nodes])


def list_scene_nodes(object_type=cfg.TRANSFORM_TYPE):
    nodes = []
    for node in rt.dcc.scene.list_scene(type=object_type):
        if not node.getShape():
            nodes.append(node)
        else:
            if not node.getShape().type() == 'camera':
                nodes.append(node)
            else:
                if not rt.dcc.ENGINE_API.camera(node.getShape(), startupCamera=True, q=True):
                    nodes.append(node)

    return nodes


def sanitize_scene():
    safe_delete(list_scene_nodes())


def get_scene_tree():
    startup_cams = [rt.dcc.scene.list_relatives(c, parent=True) for c in rt.dcc.scene.list_scene(cameras=True)
                    if rt.dcc.scene.DEFAULT_API.camera(c, q=True, startupCamera=True)]

    top_level_transforms = [node for node in rt.dcc.scene.list_scene(assemblies=True)
                            if node not in startup_cams]

    def recurse_scene_nodes(nodes, tree=None):
        if tree is None:
            tree = {tree_child.split('|')[-1]: dict() for tree_child in nodes}
        elif not tree:
            for tree_child in nodes:
                tree[tree_child.split('|')[-1]] = dict()

        for tree_child in nodes:
            relative_tree = tree[tree_child.split('|')[-1]]
            children = rt.dcc.scene.list_relatives(tree_child, fullPath=True, children=True, type=cfg.TRANSFORM_TYPE)
            if children:
                recurse_scene_nodes(children, relative_tree)

        return tree

    return recurse_scene_nodes(top_level_transforms)


def print_scene_tree():
    pprint(get_scene_tree())


def get_node_hierarchy_as_dict(node_or_nodes, tree=None, node_filter=None):
    nodes = to_list(node_or_nodes)

    if tree is None:
        tree = dict()

    for tree_child in nodes:
        anvil_node = anvil.factory(tree_child)
        try:
            relative_tree = tree[anvil_node]
        except KeyError:
            tree[anvil_node] = dict()
            relative_tree = tree[anvil_node]

        node_filter_kwargs = {cfg.TYPE: node_filter} if node_filter else {}
        children = rt.dcc.scene.list_relatives(tree_child, fullPath=True, children=True, **node_filter_kwargs) or []
        if children:
            get_node_hierarchy_as_dict(children, relative_tree, node_filter=node_filter)
    return tree


def check_exist_to_list(reference_objects, cast_type=str):
    reference_objects = to_list(reference_objects)
    return [cast_type(reference_object) for reference_object in reference_objects if
            reference_object is not None and rt.dcc.scene.exists(reference_object)]
