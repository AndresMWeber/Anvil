import anvil
import anvil.runtime as rt


def normalize_scale(desired_scale):
    import pymel.core as pm
    for obj in pm.ls(sl=True):
        biggest_value = abs(max([max([abs(p) for p in points]) for points in obj.boundingBox()]))
        normalized = max([desired_scale, biggest_value]) / min([desired_scale, biggest_value])
        pm.scale(obj, [normalized] * 3)


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
    return all([rt.dcc.scene.exists(node) for node in nodes])


def list_scene_nodes(object_type='transform', has_shape=False):
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
            children = rt.dcc.scene.list_relatives(tree_child, fullPath=True, children=True, type='transform')
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
        children = rt.dcc.scene.list_relatives(tree_child, fullPath=True, children=True, **node_filter_kwargs) or []
        if children:
            node_hierarchy_as_dict(children, relative_tree, node_filter=node_filter)

    return tree


def cast_to_list(query):
    if isinstance(query, list):
        return query
    else:
        return [query]


def validate_and_cast_to_str_list(reference_objects):
    reference_objects = cast_to_list(reference_objects)
    return [str(reference_object) for reference_object in reference_objects if
            reference_object is not None and rt.dcc.scene.exists(reference_object)]


def validate_and_cast_to_anvil_list(reference_objects):
    reference_objects = cast_to_list(reference_objects)
    return [anvil.factory(reference_object) for reference_object in reference_objects if
            reference_object is not None and rt.dcc.scene.exists(reference_object)]
