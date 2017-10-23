import anvil
import anvil.runtime as runtime
import dag_node


class Transform(dag_node.DagNode):
    dcc_type = 'transform'

    def get_parent(self):
        parents = runtime.dcc.scene.list_relatives(self._dcc_id, parent=True)
        if isinstance(parents, list):
            return parents[0]
        return parents

    def parent(self, new_parent):
        anvil.LOG.debug('Parenting %s to %s' % (str(self), str(new_parent)))
        return runtime.dcc.scene.parent(str(self), str(new_parent))

    @classmethod
    def build(cls, meta_data=None, parent=None, **flags):
        node = super(Transform, cls).build(meta_data=meta_data, **flags)
        if parent:
            node.parent(parent)
        return node
