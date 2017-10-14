from jsonschema import validate

import anvil
import anvil.runtime as runtime
import rig


class Control(rig.Rig):
    schema = {
        "type": ["object", "null"],
        "properties": {
            "offset_group": {"type": "string"},
            "connection_group": {"type": "string"}
        },
    }

    def __init__(self, control, layout=None, meta_data=None, offset_group=None, connection_group=None, name_tokens=None, **flags):
        super(Control, self).__init__(name_tokens=name_tokens)
        self.flags = flags or {}
        self.control = control
        self.offset_group = offset_group
        self.connection_group = connection_group

    @classmethod
    def build(cls, meta_data=None, **flags):
        validate(flags, cls.schema)
        flags['offset_group'] = runtime.dcc.create.create_node('transform')
        flags['connection_group'] = runtime.dcc.create.create_node('transform')
        return cls(runtime.dcc.create.create_node('curve'), **flags)

    def build_layout(self):
        runtime.dcc.scene.parent(str(self), str(self.offset_group))
        runtime.dcc.scene.parent(str(self.connection_group), str(self))

    def rename(self, *input_dicts, **name_tokens):
        for input_dict in input_dicts:
            name_tokens.update(input_dict)
        self._nomenclate.merge_dict(name_tokens)
        self.offset_group.rename(self._nomenclate.get(type='offset_group'))
        self.connection_group.rename(self._nomenclate.get(type='connection_group'))
        self.control.rename(self._nomenclate.get(type='control'))

    def parent(self, new_parent):
        if self.offset_group:
            anvil.LOG.info('Parenting control offset group %s to %s' % (str(self), str(new_parent)))
            return runtime.dcc.scene.parent(str(self.offset_group), str(new_parent))
        else:
            return super(Control, self).parent(new_parent)