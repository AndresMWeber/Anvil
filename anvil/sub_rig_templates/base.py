import anvil.runtime as rt
from anvil.meta_data import MetaData
import anvil.node_types as nt
import anvil.objects.attribute as at
import anvil.config as cfg
import anvil
from anvil.utils.generic import to_list
from anvil.grouping.base import register_built_nodes, generate_build_report


class SubRigTemplate(nt.SubRig):
    BUILT_IN_ATTRIBUTES = nt.SubRig.BUILT_IN_ATTRIBUTES.merge({cfg.IKFK_BLEND: at.ZERO_TO_ONE_KWARGS}, new=True)
    DEFAULT_FK_SHAPE = cfg.DEFAULT_FK_SHAPE

    @register_built_nodes
    @generate_build_report
    def build_ik(self, linear_hierarchy_set, solver=cfg.IK_RP_SOLVER, parent=None, name_tokens=None, **kwargs):
        name_tokens = MetaData({cfg.TYPE: cfg.IK_HANDLE}, name_tokens or {})
        kwargs.update({'endEffector': str(linear_hierarchy_set.tail), 'solver': solver})

        handle, effector = rt.dcc.rigging.ik_handle(str(linear_hierarchy_set.head), **kwargs)
        if parent:
            rt.dcc.scene.parent(handle, parent)

        handle = anvil.factory(handle, name_tokens=name_tokens, **kwargs)
        ik_handle = anvil.factory(effector, name_tokens=name_tokens.update({cfg.TYPE: cfg.IK_EFFECTOR}), **kwargs)

        return handle, ik_handle

    @register_built_nodes
    @generate_build_report
    def build_blend_chain(self, layout_joints, source_chains, duplicate=True, **kwargs):
        blend_chain = nt.LinearHierarchyNodeSet(layout_joints, duplicate=duplicate, parent=self.group_joints, **kwargs)

        for bl, source_chain in zip(blend_chain, zip(*source_chains)):
            blender = rt.dcc.create.create_node(cfg.BLEND_NODE)
            blender.output.connect(bl.rotate)

            for index, joint in enumerate(source_chain):
                joint.rotate.connect(blender.attr('color%d' % (index + 1)))

            getattr(self.root, cfg.IKFK_BLEND).connect(blender.blender)

        return blend_chain

    @register_built_nodes
    @generate_build_report
    def build_ik_chain(self, layout_joints, ik_end_index=-1, solver=cfg.IK_RP_SOLVER, duplicate=True, **kwargs):
        kwargs = MetaData(kwargs)

        ik_chain = nt.LinearHierarchyNodeSet(layout_joints, duplicate=duplicate, parent=self.group_joints, **kwargs)

        results = self.build_ik(ik_chain, chain_end=ik_chain[ik_end_index], parent=self.group_nodes,
                                name_tokens={cfg.NAME: cfg.IK}, **kwargs)
        print(results)
        handle, effector = results[cfg.NODE_TYPE]

        controls = []
        # build ik control
        controls.append(nt.Control.build(**(kwargs + {cfg.PARENT: self.group_controls,
                                                      cfg.REFERENCE_OBJECT: ik_chain[-1],
                                                      cfg.SHAPE: cfg.DEFAULT_IK_SHAPE,
                                                      cfg.NAME_TOKENS: {cfg.PURPOSE: cfg.IK}})))

        # build pole vector control if using RP solver.
        if solver == cfg.IK_RP_SOLVER:
            controls.append(self.build_pole_vector_control(ik_chain, handle,
                                                           **(kwargs + {cfg.SHAPE: cfg.DEFAULT_PV_SHAPE,
                                                                        cfg.NAME_TOKENS:
                                                                            {cfg.PURPOSE: cfg.POLE_VECTOR}})))

        rt.dcc.connections.translate(controls[0].connection_group, handle)
        return (ik_chain, controls, handle, effector)

    @register_built_nodes
    @generate_build_report
    def build_fk_chain(self, chain_start=None, chain_end=None, shape=None, duplicate=True, parent=None,
                       name_tokens=None, meta_data=None, **kwargs):
        chain = nt.LinearHierarchyNodeSet(chain_start, chain_end, duplicate=duplicate, parent=self.group_joints)

        # Ensure there are enough shapes in the shape list to pair with the chain
        controls = []
        last_node = parent or self.group_controls
        for node, shape in zip(chain, self.get_shape_list(len(chain), shape)):
            control = nt.Control.build(reference_object=node,
                                       shape=shape,
                                       parent=last_node,
                                       name_tokens=self.name_tokens.merge(self.name_tokens, name_tokens, new=True),
                                       meta_data=self.meta_data.merge(self.meta_data, meta_data, new=True),
                                       **kwargs)
            controls.append(control)
            rt.dcc.connections.parent(control.node.connection_group, node, maintainOffset=True)
            last_node = control.node.connection_group
        return (controls, chain)

    @register_built_nodes
    @generate_build_report
    def build_pole_vector_control(self, joints, ik_handle,
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

        control = nt.Control.build_pole_vector(joints, ik_handle, **kwargs)
        pv_line, clusters = nt.Curve.build_line_indicator(mid_joint, control.control, **kwargs)

        for cluster in clusters:
            cluster.visibility.set(False)
            cluster.parent(self.group_nodes)
        pv_line.parent(self.group_controls)
        return (control, pv_line, clusters)

    @classmethod
    def get_shape_list(cls, length, shape_list=None, shape=None, **kwargs):
        shape_list = to_list(shape_list or shape or cls.DEFAULT_FK_SHAPE)
        if not len(shape_list) == length:
            shape_list.extend([shape_list[-1]] * (length - len(shape_list)))
        return shape_list
