import base
import anvil.log as lg
import anvil.config as cfg
from anvil.objects.curve import Curve
from anvil.objects.transform import Transform
from anvil.meta_data import MetaData
from control import Control
from traversal import HierarchyChain


class SubRig(base.AbstractGrouping):
    BUILT_IN_NAME_TOKENS = MetaData(base.AbstractGrouping.BUILT_IN_NAME_TOKENS)
    ROOT_NAME_TOKENS = {cfg.RIG_TYPE: cfg.SUB_RIG_TOKEN, cfg.TYPE: cfg.GROUP_TYPE}
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

        self.info('Built %s: %s', self.__class__.__name__, self)

    def build_fk_controls(self, chain_start=None, chain_end=None, shape_list=None, parent=None,
                          name_tokens=None, meta_data=None, **kwargs):
        chain = HierarchyChain(chain_start, chain_end)
        last_node = parent
        controls = []

        # Ensure there are enough shapes in the shape list to pair with the chain
        if not len(shape_list) == len(chain) and shape_list:
            shape_list.append(shape_list[-1] * (len(chain) - len(shape_list)))
        elif shape_list is None:
            shape_list = [cfg.DEFAULT_FK_SHAPE] * len(chain)

        for node, shape in zip(chain, shape_list):
            last_node = Control.build(reference_object=node,
                                      shape=shape,
                                      parent=last_node,
                                      name_tokens=self.name_tokens.merge(self.name_tokens, name_tokens, new=True),
                                      meta_data=self.meta_data.merge(self.meta_data, meta_data, new=True),
                                      **kwargs)
            controls.append(last_node)
        return controls

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

        for cluster in clusters:
            cluster.visibility.set(False)
            cluster.parent(self.group_nodes)
        pv_line.parent(self.group_controls)
        return control
