from jsonschema import validate

import anvil
import anvil.objects as objects
import anvil.runtime as rt
import base


class Control(base.AbstractGrouping):
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
        flags['offset_group'] = objects.Transform.build()
        flags['connection_group'] = objects.Transform.build()
        return cls(objects.Curve.build(), **flags)

    def build_layout(self):
        rt.dcc.scene.parent(str(self), str(self.offset_group))
        rt.dcc.scene.parent(str(self.connection_group), str(self))

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
            return rt.dcc.scene.parent(str(self.offset_group), str(new_parent))
        else:
            return super(Control, self).parent(new_parent)