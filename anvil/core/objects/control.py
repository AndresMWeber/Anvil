from jsonschema import validate
import anvil.runtime as runtime
import anvil
import node_types
import curve


@node_types.register_node
class Control(curve.Curve):
    schema = {
        "type": ["object", "null"],
        "properties": {
            "offset_group": {"type": "string"},
            "connection_group": {"type": "string"}
        },
    }

    def __init__(self, node_unicode_proxy, meta_data=None, **flags):
        super(Control, self).__init__(node_unicode_proxy, meta_data=meta_data, **flags)
        validate(flags, self.schema)
        flags = flags or {}
        self.offset_group = flags.get('offset_group')
        self.connection_group = flags.get('connection_group')

    @classmethod
    def build(cls, meta_data=None, **flags):
        flags['offset_group'] = runtime.dcc.create.create_node('transform')
        flags['connection_group'] = runtime.dcc.create.create_node('transform')
        instance = super(Control, cls).build(meta_data=meta_data, **flags)
        instance.reset_hierarchy()
        return instance

    def reset_hierarchy(self):
        runtime.dcc.scene.parent(str(self), str(self.offset_group))
        runtime.dcc.scene.parent(str(self), str(self.connection_group))

    def parent(self, new_parent):
        if self.offset_group:
            anvil.LOG.info('Parenting control offset group %s to %s' % (str(self), str(new_parent)))
            return runtime.dcc.scene.parent(str(self.offset_group), str(new_parent))
        else:
            return super(Control, self).parent(new_parent)