import base
import anvil
import anvil.log as lg
import anvil.config as cfg
from control import Control
from anvil.objects.curve import Curve
from anvil.objects.transform import Transform
from anvil.meta_data import MetaData


class SubRig(base.AbstractGrouping):
    BUILT_IN_NAME_TOKENS = MetaData(base.AbstractGrouping.BUILT_IN_NAME_TOKENS)
    ROOT_NAME_TOKENS = {cfg.RIG_TYPE: cfg.SUBRIG, cfg.TYPE: cfg.GROUP_TYPE}
    LOG = lg.obtainLogger(__name__)
    SUB_GROUPS = ['surfaces', 'joints', 'controls', 'nodes', 'world']

    def build(self, parent=None, **kwargs):
        super(SubRig, self).build(**kwargs)
        if self.root is None:
            self.build_node(Transform, '%s_%s' % (cfg.GROUP_TYPE, 'top'),
                            meta_data=self.meta_data,
                            name_tokens=self.name_tokens + {cfg.RIG_TYPE: cfg.SUB_RIG_TYPE, cfg.TYPE: cfg.GROUP_TYPE},
                            **self.build_kwargs)
            self.root = self.group_top

        for main_group_type in self.SUB_GROUPS:
            group_name = '%s_%s' % (cfg.GROUP_TYPE, main_group_type)
            self.build_node(Transform, group_name, parent=self.root,
                            meta_data=self.meta_data,
                            name_tokens=self.name_tokens + {cfg.CHILD_TYPE: main_group_type, cfg.TYPE: cfg.GROUP_TYPE})
        self.group_world.inheritsTransform.set(False)

        self.parent(parent)
        self.initialize_sub_rig_attributes()
        self.connect_rendering_delegate()

        anvil.LOG.info('Built %s: %s' % (self.__class__.__name__, self))

    def build_pole_vector_control(self, joints, ik_handle, node_key='',
                                  up_vector=None,
                                  aim_vector=None,
                                  up_object=None,
                                  move_by=None,
                                  meta_data=None,
                                  name_tokens=None,
                                  **kwargs):
        """ Point constraint to the two base positions, aim constrain to the other objects
            Delete constraints then move the control outside of the reference transforms in the aim direction.
        """
        mid_joint = joints[len(joints) / 2]

        kwargs.update({cfg.NAME_TOKENS: MetaData(self.name_tokens, name_tokens),
                       cfg.META_DATA: MetaData(self.meta_data, meta_data),
                       'move_by': move_by,
                       'parent': self.group_controls,
                       'up_vector': up_vector,
                       'aim_vector': aim_vector,
                       'up_object': up_object})

        control = Control.build_pole_vector(joints, ik_handle, **kwargs)
        pv_line, clusters = Curve.build_line_indicator(mid_joint, control.control, **kwargs)
        self.register_node(node_key, control)
        self.register_node(node_key + '_line', pv_line)
        for cluster in clusters + [pv_line]:
            cluster.parent(self.group_nodes)
        return control
