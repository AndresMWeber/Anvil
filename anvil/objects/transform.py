import anvil
import anvil.runtime as runtime
import dag_node


class Transform(dag_node.DagNode):
    dcc_type = 'transform'

    def get_parent(self):
        parents = runtime.dcc.scene.list_relatives(str(self._dcc_id), parent=True)
        if isinstance(parents, list):
            return parents[0]
        return parents

    def parent(self, new_parent):
        anvil.LOG.debug('Parenting %s to %s' % (str(self), str(new_parent)))
        top_node, new_parent = str(self), str(new_parent)
        nodes_exist = [runtime.dcc.scene.exists(node) for node in [top_node, new_parent] if node != 'None']
        if all(nodes_exist or [False]):
            runtime.dcc.scene.parent(top_node, new_parent)
            return True
        else:
            raise KeyError('Node %s or %s does not exist.' % (str(self), str(new_parent)))


    @classmethod
    def build(cls, meta_data=None, parent=None, **flags):
        node = super(Transform, cls).build(meta_data=meta_data, **flags)
        if parent:
            node.parent(parent)
        return node

    def colorize(self, color):
        if isinstance(color, int):
            pass
        if isinstance(color, list) and len(color) == 3:
            pass
