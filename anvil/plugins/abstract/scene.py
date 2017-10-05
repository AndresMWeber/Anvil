

class Scene(object):
    def get_persistent_id(self, node_unicode_proxy):
        return node_unicode_proxy

    def is_exact_type(self, node, typename):
        return type(node) == typename

    def is_type(self, node, typename):
        return typename in ['Transform', 'Curve', 'Joint', 'Shape', 'UnicodeDelegate', 'DagNode']

    def get_scene_tree(self):
        return {'abstract': None}

    def list_scene_nodes(self, object_type='transform', has_shape=False):
        return ['abstract']

    def exists(self, node, *args, **kwargs):
        return True

    def safe_delete(self, node_or_nodes):
        pass

    def rename(self, node_dag, name, **kwargs):
        return name

    def duplicate(self, node_dag, parent_only=True, **kwargs):
        return node_dag + '_duplicate'
