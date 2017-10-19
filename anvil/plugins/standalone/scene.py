import anvil.plugins.base.scene as scene


class Scene(scene.Scene):
    def get_persistent_id(self, node_unicode_proxy):
        return node_unicode_proxy

    def get_type(self, node, **kwargs):
        return type(node)

    def is_exact_type(self, node, typename):
        return type(node) == typename

    def is_type(self, node, typename):
        return typename in ['Transform', 'Curve', 'Joint', 'Shape', 'UnicodeDelegate', 'DagNode']

    def get_scene_tree(self):
        return {'standalone': None}

    def list_scene_nodes(self, object_type='transform', has_shape=False):
        return ['standalone']

    def exists(self, node, *args, **kwargs):
        return True

    def safe_delete(self, node_or_nodes):
        return True

    def rename(self, node_dag, name, **kwargs):
        return name

    def duplicate(self, node_dag, parent_only=True, **kwargs):
        return node_dag + '_duplicate'

    def list_relatives(self, node_dag, **flags):
        return node_dag

    def parent(self, node, new_parent, **flags):
        return new_parent

    def delete(self, nodes):
        del(nodes)