import anvil.runtime as rt
import anvil.config as cfg


def is_exact_type(node, typename):
    return rt.dcc.scene.get_type(node) == typename


def is_types(node, types):
    return any([rt.dcc.scene.get_type(node) == object_type for object_type in types])


def safe_delete(node_or_nodes):
    if isinstance(node_or_nodes, list):
        for node in node_or_nodes:
            try:
                rt.dcc.scene.delete(node)
            except ValueError:
                pass
    else:
        try:
            rt.dcc.scene.delete(node_or_nodes)
        except ValueError:
            pass


def objects_exist(nodes):
    return all([rt.dcc.scene.exists(node) if node else False for node in nodes])


def list_scene_nodes(object_type=cfg.TRANSFORM_TYPE, has_shape=False):
    nodes = []
    for node in rt.dcc.scene.list_scene(type=object_type):
        if not node.getShape():
            nodes.append(node)
        else:
            if not node.getShape().type() == 'camera':
                nodes.append(node)
            else:
                if not rt.dcc.scene.API.camera(node.getShape(), startupCamera=True, q=True):
                    nodes.append(node)

    return nodes


def get_scene_tree():
    startup_cams = [rt.dcc.scene.list_relatives(c, parent=True) for c in rt.dcc.scene.list_scene(cameras=True)
                    if rt.dcc.scene.API.camera(c, q=True, startupCamera=True)]

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