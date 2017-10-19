from jsonschema import validate

import anvil
import anvil.objects as objects
import anvil.runtime as rt
import base


class Control(base.AbstractGrouping):
    ANVIL_TYPE = 'control'

    def __init__(self,
                 control=None,
                 offset_group=None,
                 connection_group=None,
                 **flags):
        super(Control, self).__init__(**flags)
        self.hierarchy['control'] = control
        self.hierarchy['offset_group'] = offset_group
        self.hierarchy['connection_group'] = connection_group

    @classmethod
    def build(cls, meta_data=None, **flags):
        instance = cls(meta_data=meta_data, **flags)
        instance.add_node(objects.Curve, 'control', meta_data={'type': 'control'}, **flags)
        instance.add_node(objects.Transform, 'offset_group', meta_data={'type': 'offset_group'})
        instance.add_node(objects.Transform, 'connection_group', meta_data={'type': 'connection_group'})
        instance.build_layout()
        return instance

    def build_layout(self):
        if self.flags.get('parent'):
            self.parent(self.flags.get('parent'))
        rt.dcc.scene.parent(str(self.control), str(self.offset_group))
        rt.dcc.scene.parent(str(self.connection_group), str(self.control))

    def parent(self, new_parent):
        if self.offset_group:
            anvil.LOG.info('Parenting control offset group %s to %s' % (str(self), str(new_parent)))
            return rt.dcc.scene.parent(str(self.offset_group), str(new_parent))
        else:
            return super(Control, self).parent(new_parent)

    def __str__(self):
        try:
            return str(self.find_node('control'))
        except (TypeError, AttributeError):
            return super(Control, self).__str__()
