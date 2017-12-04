def get_persistent_id(node_unicode_proxy, *args, **kwargs):
    return node_unicode_proxy


def get_type(node, *args, **kwargs):
    return type(node)


def is_exact_type(node, typename, *args, **kwargs):
    return type(node) == typename


def is_type(node, typename, *args, **kwargs):
    return typename in ['Transform', 'Curve', 'Joint', 'Shape', 'UnicodeDelegate', 'DagNode']


def rename(node_dag, name, *args, **kwargs):
    return name


def duplicate(node_dag, parent_only=True, *args, **kwargs):
    return node_dag + '_duplicate'


def list_relatives(node_dag, *args, **kwargs):
    return node_dag


def parent(node, new_parent, *args, **kwargs):
    return new_parent


def delete(nodes, *args, **kwargs):
    del (nodes)


def get_scene_tree():
    return {'standalone': None}


def list_scene(object_type='transform', *args, **kwargs):
    return []


def list_scene_nodes(object_type='transform', has_shape=False):
    return ['standalone']


def exists(node, *args, **kwargs):
    return True


def safe_delete(node_or_nodes):
    return True
