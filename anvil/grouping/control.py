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

    def __init__(self, control, layout=None, meta_data=None, offset_group=None, connection_group=None, name_tokens=None,
                 **flags):
        super(Control, self).__init__(name_tokens=name_tokens)
        self.flags = flags or {}
        self.hierarchy['control'] = control

    @classmethod
    def build(cls, meta_data=None, **flags):
        validate(flags, cls.schema)
        instance = cls(objects.Curve.build(), **flags)
        instance.add_node(objects.Transform, 'offset_group')
        instance.add_node(objects.Transform, 'connection_group')
        instance.build_layout()
        return instance

    def build_layout(self):
        if self.flags.get('parent'):
            self.parent(self.flags.get('parent'))
        rt.dcc.scene.parent(str(self.control), str(self.offset_group))
        rt.dcc.scene.parent(str(self.connection_group), str(self.control))

    def rename(self, *input_dicts, **name_tokens):
        merged_dicts = {}
        for input_dict in input_dicts:
            merged_dicts.update(input_dict)
        merged_dicts.update(name_tokens)

        anvil.LOG.info('Renaming control %s with dict %s' % (self, merged_dicts))
        self._nomenclate.merge_dict(merged_dicts)

        self.offset_group.rename(self._nomenclate.get(type='offset_group'))
        self.connection_group.rename(self._nomenclate.get(type='connection_group'))
        self.control.rename(self._nomenclate.get(type='control'))

    def parent(self, new_parent):
        if self.offset_group:
            anvil.LOG.info('Parenting control offset group %s to %s' % (str(self), str(new_parent)))
            return rt.dcc.scene.parent(str(self.offset_group), str(new_parent))
        else:
            return super(Control, self).parent(new_parent)
