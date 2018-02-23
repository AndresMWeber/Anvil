import anvil.runtime as rt
from anvil.meta_data import MetaData
import anvil.node_types as nt
import anvil.objects.attribute as at
import anvil.config as cfg
import anvil
from anvil.utils.generic import to_list, to_size_list
from anvil.grouping.base import register_built_nodes, generate_build_report


class SubRigTemplate(nt.SubRig):
    BUILT_IN_ATTRIBUTES = nt.SubRig.BUILT_IN_ATTRIBUTES.merge({cfg.IKFK_BLEND: at.ZERO_TO_ONE_KWARGS}, new=True)

    @register_built_nodes
    @generate_build_report
    def build_pole_vector_control(self, joints, ik_handle,
                                  parent=None,
                                  up_vector=None,
                                  aim_vector=None,
                                  up_object=None,
                                  move_by=None,
                                  meta_data=None,
                                  name_tokens=None,
                                  **kwargs):
        """ Builds a pole vector control based on positions of joints and existing ik handle.
            Runs as follows:
                - Point constraint to the two base positions, aim constrain to the other objects
                - Delete constraints then move the control outside of the reference transforms in the aim direction.


        :param joints: LinearHierarchyNodeSet(Joint), linear hierarchy set of joints.
        :param ik_handle: DagNode, ik handle node
        :param kwargs: dict, build kwargs for the control build call
        :return: (Control, DagNode, NonLinearHierarchyNodeSet(DagNode))
        """
        parent = list(reversed(to_size_list(parent, 3)))

        name_tokens = MetaData(self.name_tokens, name_tokens) if hasattr(self, cfg.NAME_TOKENS) else name_tokens
        meta_data = MetaData(self.meta_data, meta_data) if hasattr(self, cfg.META_DATA) else meta_data
        kwargs.update({cfg.NAME_TOKENS: name_tokens,
                       cfg.META_DATA: meta_data,
                       'move_by': move_by,
                       'parent': parent.pop(),
                       'up_vector': up_vector,
                       'aim_vector': aim_vector,
                       'up_object': up_object})

        control = nt.Control.build_pole_vector(joints, ik_handle, **kwargs)
        pv_line, clusters = nt.Curve.build_line_indicator(joints[len(joints) // 2], control.controller, **kwargs)

        cluster_parent = parent.pop()
        for cluster in clusters:
            cluster.visibility.set(False)
            cluster.parent(cluster_parent)

        pv_line.parent(parent.pop())

        return control, pv_line, nt.NonLinearHierarchyNodeSet(clusters)

    DEFAULT_FK_SHAPE = cfg.DEFAULT_FK_SHAPE

    @register_built_nodes
    @generate_build_report
    def build_ik(self, linear_hierarchy_set, solver=cfg.IK_RP_SOLVER, parent=None, name_tokens=None, **kwargs):
        name_tokens = MetaData({cfg.TYPE: cfg.IK_HANDLE}, name_tokens or {})
        kwargs.update({'endEffector': str(linear_hierarchy_set.tail), 'solver': solver})

        handle, effector = anvil.factory_list(rt.dcc.rigging.ik_handle(str(linear_hierarchy_set.head), **kwargs))
        if parent:
            rt.dcc.scene.parent(handle, parent)

        handle.name_tokens.update(name_tokens)
        effector.name_tokens.update({cfg.TYPE: cfg.IK_EFFECTOR})

        return handle, effector

    @register_built_nodes
    @generate_build_report
    def build_blend_chain(self, layout_joints, source_chains, blend_attr=None, parent=None, duplicate=True, **kwargs):
        blend_chain = nt.LinearHierarchyNodeSet(layout_joints, duplicate=duplicate, parent=parent, **kwargs)

        for bl, source_chain in zip(blend_chain, zip(*source_chains)):
            blender = rt.dcc.create.create_node(cfg.BLEND_NODE)
            blender.output.connect(bl.rotate)

            for index, joint in enumerate(source_chain):
                joint.rotate.connect(blender.attr('color%d' % (index + 1)))

            if blend_attr:
                blend_attr.connect(blender.blender)

        return blend_chain

    @register_built_nodes
    @generate_build_report
    def build_ik_chain(self,
                       layout_joints,
                       ik_end_index=-1,
                       solver=cfg.IK_RP_SOLVER,
                       chain_parent=None,
                       parent=None,
                       duplicate=True,
                       **kwargs):
        parent = list(reversed(to_size_list(parent, 3)))

        ik_chain = nt.LinearHierarchyNodeSet(layout_joints, duplicate=duplicate, parent=chain_parent, **kwargs)

        results = self.build_ik(ik_chain,
                                chain_end=ik_chain[ik_end_index],
                                parent=parent.pop(),
                                name_tokens={cfg.NAME: cfg.IK}, **kwargs)
        handle, effector = results[cfg.NODE_TYPE][cfg.DEFAULT]

        controls = nt.NonLinearHierarchyNodeSet()
        # build ik control
        controls.append(nt.Control.build(**MetaData(kwargs, {cfg.PARENT: parent.pop(),
                                                             cfg.REFERENCE_OBJECT: ik_chain[-1],
                                                             cfg.SHAPE: cfg.DEFAULT_IK_SHAPE,
                                                             cfg.NAME_TOKENS: {cfg.PURPOSE: cfg.IK}}).to_dict()))

        # build pole vector control if using RP solver.
        if solver == cfg.IK_RP_SOLVER:
            controls.append(self.build_pole_vector_control(ik_chain, handle,
                                                           **MetaData(kwargs, {cfg.SHAPE: cfg.DEFAULT_PV_SHAPE,
                                                                               cfg.NAME_TOKENS:
                                                                                   {cfg.PURPOSE: cfg.POLE_VECTOR}})))

        rt.dcc.connections.translate(controls[0].connection_group, handle)
        return ik_chain, controls, handle, effector

    @register_built_nodes
    @generate_build_report
    def build_fk_chain(self, chain_start=None, chain_end=None, shape=None, duplicate=True, parent=None,
                       name_tokens=None, meta_data=None, **kwargs):
        """

        :param parent: list or object: list of up to length 2, [fk chain parent, control chain parent]
        :return: (NonLinearHierarchyNodeSet(Control), LinearHierarchyNodeSet(Joint))
        """
        parent = to_size_list(parent, 2)

        chain = nt.LinearHierarchyNodeSet(chain_start, chain_end, duplicate=duplicate, parent=parent.pop())
        controls = nt.NonLinearHierarchyNodeSet()
        control_parent = parent.pop()
        name_tokens = MetaData(self.name_tokens, name_tokens) if hasattr(self, cfg.NAME_TOKENS) else name_tokens
        meta_data = MetaData(self.meta_data, meta_data) if hasattr(self, cfg.META_DATA) else meta_data

        for node, shape in zip(chain, to_size_list(shape or self.DEFAULT_FK_SHAPE, len(chain))):
            control = nt.Control.build(reference_object=node,
                                       shape=shape,
                                       parent=control_parent,
                                       name_tokens=name_tokens,
                                       meta_data=meta_data,
                                       **kwargs)
            controls.append(control)
            rt.dcc.connections.parent(control.node.connection_group, node, maintainOffset=True)
            control_parent = control.node.connection_group
        return controls, chain
