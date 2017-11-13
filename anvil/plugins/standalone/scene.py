
def get_persistent_id(node_unicode_proxy):
    return node_unicode_proxy

def get_type(node, **kwargs):
    return type(node)

def is_exact_type(node, typename):
    return type(node) == typename

def is_type(node, typename):
    return typename in ['Transform', 'Curve', 'Joint', 'Shape', 'UnicodeDelegate', 'DagNode']

def get_scene_tree(self):
    return {'standalone': None}

def list_scene_nodes(object_type='transform', has_shape=False):
    return ['standalone']

def exists(node, *args, **kwargs):
    return True

def safe_delete(node_or_nodes):
    return True

def rename(node_dag, name, **kwargs):
    return name

def duplicate(node_dag, parent_only=True, **kwargs):
    return node_dag + '_duplicate'

def list_relatives(node_dag, **flags):
    return node_dag

def parent(node, new_parent, **flags):
    return new_parent

def delete(nodes):
    del(nodes)