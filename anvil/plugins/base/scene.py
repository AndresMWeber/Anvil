class Scene(object):
    def get_persistent_id(self, node_unicode_proxy):
        raise NotImplementedError

    def get_type(self, node, **kwargs):
        raise NotImplementedError

    def is_exact_type(self, node, typename):
        raise NotImplementedError

    def is_type(self, node, typename):
        raise NotImplementedError

    def get_scene_tree(self):
        raise NotImplementedError

    def list_scene_nodes(self, object_type='transform', has_shape=False):
        raise NotImplementedError

    def exists(self, node, *args, **kwargs):
        raise NotImplementedError

    def safe_delete(self, node_or_nodes):
        raise NotImplementedError

    def rename(self, node_dag, name, **kwargs):
        raise NotImplementedError

    def duplicate(self, node_dag, parent_only=True, **kwargs):
        raise NotImplementedError

    def list_relatives(self, node_dag, **flags):
        raise NotImplementedError

    def parent(self, node, new_parent, **flags):
        raise NotImplementedError

    def delete(self, nodes):
        raise NotImplementedError