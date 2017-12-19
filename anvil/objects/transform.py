import anvil.runtime as rt
import dag_node


class Transform(dag_node.DagNode):
    dcc_type = 'transform'

    @staticmethod
    def create_engine_instance(**flags):
        return rt.dcc.create.create_transform(**flags)

    def get_parent(self):
        parents = rt.dcc.scene.list_relatives(self.name(), parent=True)
        try:
            return parents[0]
        except IndexError:
            return parents

    def parent(self, new_parent):
        self.LOG.debug('Parenting %s to %s' % (self, new_parent))
        top_node, new_parent = self, new_parent
        nodes_exist = [rt.dcc.scene.exists(node) for node in [top_node, new_parent] if node != None]
        if all(nodes_exist or [False]):
            rt.dcc.scene.parent(top_node, new_parent)
            return True
        elif new_parent is None:
            rt.dcc.scene.parent(top_node, world=True)
        else:
            raise KeyError('Node %s or %s does not exist.' % (self, new_parent))

    @classmethod
    def build(cls, reference_object=None, meta_data=None, parent=None, **kwargs):
        node = super(Transform, cls).build(meta_data=meta_data, **kwargs)
        node.parent(parent)
        node.match_position(reference_object)
        return node

    def match_position(self, reference_object):
        if reference_object and rt.dcc.scene.exists(reference_object):
            self.LOG.info('Matching position of %s to %s' % (self, reference_object))
            constraint = rt.dcc.connections.parent(reference_object, self, maintainOffset=False)
            rt.dcc.scene.delete(constraint)

    def colorize(self, color):
        if isinstance(color, int):
            pass
        if isinstance(color, list) and len(color) == 3:
            pass
