import base
import anvil.log as lg
import anvil.objects as ot
import anvil.runtime as rt
from control import Control


class SubRig(base.AbstractGrouping):
    LOG = lg.obtainLogger(__name__)

    def __init__(self, *args, **kwargs):
        super(SubRig, self).__init__(*args, **kwargs)

    def build(self, parent=None, meta_data=None, **flags):
        self.LOG.info('Building sub-rig %s' % self)
        self.meta_data = self.merge_dicts(self.meta_data, meta_data or {})
        if self.root is None:
            self.build_node(ot.Transform,
                            'group_top',
                            meta_data=self.merge_dicts(self.meta_data, {'rig': 'subrig', 'type': 'group'}),
                            **flags)
            self.root = self.group_top

        for main_group_type in ['surfaces', 'joints', 'controls', 'nodes', 'world']:
            group_name = 'group_%s' % main_group_type
            self.build_node(ot.Transform,
                            group_name,
                            parent=self.root,
                            meta_data=self.merge_dicts(self.meta_data, {'childtype': main_group_type, 'type': 'group'}))

        self.group_world.inheritsTransform.set(False)
        self.parent(parent)
        return self

    def build_pole_vector_control(self, joints, ik_handle, node_key='', move_by=None, meta_data=None, **flags):
        """ Point constraint to the two base positions, aim constrain to the other objects
            Delete constraints then move the control outside of the reference transforms in the aim direction.
        """
        joints = list(joints)

        if len(joints) < 3:
            raise ValueError('Cannot create a pole vector control for less than 3 joints...')

        move_by = move_by or [5, 0, 0]
        control = Control.build(meta_data=meta_data, **flags)
        point_constraint = rt.dcc.constrain.translate([joints[0], joints[-1]],
                                                      control.offset_group,
                                                      maintain_offset=False)
        aim_constraint = rt.dcc.constrain.aim(joints,
                                              control.offset_group,
                                              maintain_offset=False,
                                              upObject=str(joints[0]))
        rt.dcc.scene.delete([aim_constraint, point_constraint])
        local_movement_kwargs = {'relative': True, 'objectSpace': True, 'worldSpaceDistance': True}
        rt.dcc.scene.position(control.offset_group, translation=move_by, **local_movement_kwargs)
        rt.dcc.constrain.pole_vector(control.connection_group, ik_handle)
        self.register_node(node_key, control)
        return control
