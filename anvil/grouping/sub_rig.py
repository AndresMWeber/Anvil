import base
import anvil
import anvil.log as lg
import anvil.config as cfg
from control import Control
from anvil.objects.transform import Transform


class SubRig(base.AbstractGrouping):
    LOG = lg.obtainLogger(__name__)
    SUB_GROUPS = ['surfaces', 'joints', 'controls', 'nodes', 'world']

    def __init__(self, *args, **kwargs):
        super(SubRig, self).__init__(*args, **kwargs)

    def build(self, parent=None, **kwargs):
        super(SubRig, self).build(**kwargs)
        if self.root is None:
            self.build_node(Transform, '%s_%s' % (cfg.GROUP_TYPE, 'top'),
                            meta_data={cfg.RIG: cfg.SUB_RIG, cfg.TYPE: cfg.GROUP_TYPE}, **self.build_kwargs)
            self.root = self.group_top

        for main_group_type in self.SUB_GROUPS:
            group_name = '%s_%s' % (cfg.GROUP_TYPE, main_group_type)
            self.build_node(Transform, group_name, parent=self.root,
                            meta_data={cfg.CHILD_TYPE: main_group_type, cfg.TYPE: cfg.GROUP_TYPE})
        self.group_world.inheritsTransform.set(False)

        self.parent(parent)
        self.initialize_sub_rig_attributes()
        self.connect_rendering_delegate()

        anvil.LOG.info('Built %s: %s' % (self.__class__.__name__, self))

    def build_pole_vector_control(self, joints, ik_handle, node_key='', move_by=None, meta_data=None, **kwargs):
        """ Point constraint to the two base positions, aim constrain to the other objects
            Delete constraints then move the control outside of the reference transforms in the aim direction.
        """
        meta_data = self.meta_data + meta_data
        control = Control.build_pole_vector(joints, ik_handle, move_b=move_by, meta_data=meta_data, **kwargs)
        self.register_node(node_key, control)
        return control
