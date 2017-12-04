import base
import anvil.log as lg
import anvil.objects as ot
import anvil.runtime as rt
from control import Control


class SubRig(base.AbstractGrouping):
    LOG = lg.obtainLogger(__name__)
    POLE_VECTOR_MIN_JOINTS = 2
    POLE_VECTOR_MOVE_DEFAULT = [5, 0, 0]
    LOCAL_MOVE_KWARGS = {'relative': True, 'objectSpace': True, 'worldSpaceDistance': True}

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
        self.assign_rendering_delegate()
        return self

    def build_pole_vector_control(self, joints, ik_handle, node_key='', move_by=None, meta_data=None, **flags):
        """ Point constraint to the two base positions, aim constrain to the other objects
            Delete constraints then move the control outside of the reference transforms in the aim direction.
        """
        joints = list(joints)
        if len(joints) < self.POLE_VECTOR_MIN_JOINTS:
            raise ValueError('Pole vector control needs more than %d joints...' % self.POLE_VECTOR_MIN_JOINTS)
        start_joint, end_joint = joints[0], joints[-1]

        control = Control.build(parent=self.group_controls, meta_data=meta_data, **flags)

        rt.dcc.scene.delete(
            rt.dcc.constrain.translate([start_joint, end_joint], control.offset_group, maintain_offset=False))

        rt.dcc.scene.delete(
            rt.dcc.constrain.aim(joints, control.offset_group, maintain_offset=False, upObject=start_joint))

        rt.dcc.scene.position(control.offset_group, translation=move_by or self.POLE_VECTOR_MOVE_DEFAULT,
                              **self.LOCAL_MOVE_KWARGS)

        control.offset_group.rotate.set([0, 0, 0])

        rt.dcc.constrain.pole_vector(control.connection_group, ik_handle)

        self.register_node(node_key, control)

        return control
