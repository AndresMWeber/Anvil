import anvil
import anvil.runtime as rt
import anvil.node_types as nt
import anvil.objects.attribute as at
import anvil.config as cfg
from anvil.meta_data import MetaData
from grouping.base_grouping import register_built_nodes, generate_build_report
from anvil.utils.generic import to_size_list, to_list, extend_parent_kwarg


class SubRigTemplate(nt.SubRig):
    BUILT_IN_ATTRIBUTES = nt.SubRig.BUILT_IN_ATTRIBUTES.merge({cfg.IKFK_BLEND: at.ZERO_TO_ONE_KWARGS}, new=True)

    @register_built_nodes
    @generate_build_report
    @extend_parent_kwarg(3)
    def build_pole_vector_control(self, joints, ik_handle, parent=None, up_vector=None, aim_vector=None,
                                  up_object=None, move_by=None, meta_data=None, name_tokens=None, **kwargs):
        """ Builds a pole vector control based on positions of joints and existing ik handle.
            Runs as follows:
                - Point constraint to the two base positions, aim constrain to the other objects
                - Delete constraints then move the control outside of the reference transforms in the aim direction.

        :param parent: list or object: list of up to length 3, [control parent, clusters parent, pv line parent]
        :param joints: LinearHierarchyNodeSet(Joint), linear hierarchy set of joints.
        :param ik_handle: DagNode, ik handle node
        :param kwargs: dict, build kwargs for the control build call
        :return: (Control, DagNode, NonLinearHierarchyNodeSet(DagNode))
        """
        name_tokens = MetaData(self.name_tokens, name_tokens) if hasattr(self, cfg.NAME_TOKENS) else name_tokens
        meta_data = MetaData(self.meta_data, meta_data) if hasattr(self, cfg.META_DATA) else meta_data
        kwargs.update({cfg.NAME_TOKENS: name_tokens,
                       cfg.META_DATA: meta_data,
                       'move_by': move_by,
                       'parent': next(parent),
                       'up_vector': up_vector,
                       'aim_vector': aim_vector,
                       'up_object': up_object})

        control = nt.Control.build_pole_vector(joints, ik_handle, **kwargs)
        pv_line, clusters = nt.Curve.build_line_indicator(joints[len(joints) // 2], control.controller, **kwargs)

        cluster_parent = next(parent)
        for cluster in clusters:
            cluster.visibility.set(False)
            cluster.parent(cluster_parent)

        pv_line.parent(next(parent))

        return control, pv_line, nt.NodeSet(clusters)

    DEFAULT_FK_SHAPE = cfg.DEFAULT_FK_SHAPE

    @register_built_nodes
    @generate_build_report
    @extend_parent_kwarg(1)
    def build_ik(self, linear_hierarchy_set, solver=cfg.IK_RP_SOLVER, parent=None, name_tokens=None, **kwargs):
        """

        :param parent: list or object: list of up to length 1, [handle parent]
        :return: (NonLinearHierarchyNodeSet(Control), LinearHierarchyNodeSet(Joint))
        """
        name_tokens = MetaData({cfg.TYPE: cfg.IK_HANDLE}, name_tokens or {})
        kwargs.update({'endEffector': str(linear_hierarchy_set.tail), 'solver': solver})

        handle, effector = anvil.factory_list(rt.dcc.rigging.ik_handle(str(linear_hierarchy_set.head), **kwargs))
        if parent:
            rt.dcc.scene.parent(handle, next(parent))

        handle.name_tokens.update(name_tokens)
        effector.name_tokens.update({cfg.TYPE: cfg.IK_EFFECTOR})

        return handle, effector

    @register_built_nodes
    @generate_build_report
    def build_blend_chain(self, layout_joints=None, source_chains=None, blend_attr=None, parent=None, duplicate=True,
                          **kwargs):
        """

        :param layout_joints: list, list of joints to use as the main joints in the set.
        :param source_chains: list, list of chains to use as the source input rotation chains
                                    -  length can only be up to 2 due to blend node limitations
        :param blend_attr: anvil.objects.attribute.Attribute, attribute to use as the blender for the ik/fk blend.
        :param parent: list or object: list of up to length 1, [blend chain parent]
        :param duplicate: bool, whether or not to duplicate the layout joints chain
        :return: (NonLinearHierarchyNodeSet(Control), LinearHierarchyNodeSet(Joint))
        """
        blend_chain = nt.NodeChain(layout_joints[0], duplicate=duplicate, parent=parent, **kwargs)
        blend_nodes = []
        for blend_chain_joint, source_chain_joints in zip(blend_chain, zip(*to_list(source_chains))):
            blend_nodes.append(rt.dcc.create.create_node(cfg.BLEND_NODE))
            blend_nodes[-1].output.connect(blend_chain_joint.rotate)
            if blend_attr:
                blend_attr.connect(blend_nodes[-1].blender)

            for index, source_chain_joint in enumerate(source_chain_joints):
                source_chain_joint.rotate.connect(blend_nodes[-1].attr('color%d' % (index + 1)))

        return blend_chain

    @register_built_nodes
    @generate_build_report
    @extend_parent_kwarg(5)
    def build_ik_chain(self, layout_joints=None, ik_end_index=-1, solver=cfg.IK_RP_SOLVER, parent=None, duplicate=True,
                       **kwargs):
        """

        :param parent: list or object: list of up to length 5:
                       [ik chain parent, handle
                       parent,
                       pv control parent,
                       pole vector clusters parent,
                       pole vector line parent]
        :return: (NonLinearHierarchyNodeSet(Control), LinearHierarchyNodeSet(Joint))
        """
        kwargs[cfg.SKIP_REGISTER] = True
        kwargs[cfg.SKIP_REPORT] = True
        ik_chain = nt.NodeChain(layout_joints, duplicate=duplicate, parent=next(parent), **kwargs)

        handle, effector = self.build_ik(ik_chain,
                                         chain_end=ik_chain[ik_end_index],
                                         parent=next(parent),
                                         name_tokens=MetaData({cfg.NAME: cfg.IK}, kwargs.pop(cfg.NAME_TOKENS, {})),
                                         **kwargs)

        controls = nt.NodeSet()
        # build ik control
        controls.append(nt.Control.build(**MetaData(kwargs, {cfg.PARENT: next(parent),
                                                             cfg.REFERENCE_OBJECT: ik_chain[-1],
                                                             cfg.SHAPE: cfg.DEFAULT_IK_SHAPE,
                                                             cfg.NAME_TOKENS: {cfg.PURPOSE: cfg.IK}}).to_dict()))

        # build pole vector control if using RP solver.
        if solver == cfg.IK_RP_SOLVER:
            pv_control = self.build_pole_vector_control(ik_chain, handle,
                                                        parent=[next(parent), next(parent)],
                                                        **MetaData(kwargs, {cfg.SHAPE: cfg.DEFAULT_PV_SHAPE,
                                                                            cfg.NAME_TOKENS: {
                                                                                cfg.PURPOSE: cfg.POLE_VECTOR}}))
            controls.append(pv_control)

        rt.dcc.connections.translate(controls[0].connection_group, handle)

        return ik_chain, controls, handle, effector

    @register_built_nodes
    @generate_build_report
    @extend_parent_kwarg(2)
    def build_fk_chain(self, layout_joints=None, chain_end=None, shape=None, duplicate=True, parent=None,
                       name_tokens=None, meta_data=None, **kwargs):
        """

        :param parent: list or object: list of up to length 2, [fk chain parent, control chain parent]
        :return: (NonLinearHierarchyNodeSet(Control), LinearHierarchyNodeSet(Joint))
        """
        name_tokens = MetaData(self.name_tokens, name_tokens) if hasattr(self, cfg.NAME_TOKENS) else name_tokens
        meta_data = MetaData(self.meta_data, meta_data) if hasattr(self, cfg.META_DATA) else meta_data
        kwargs['skip_register'] = True
        kwargs['skip_report'] = True
        fk_chain = nt.NodeChain(layout_joints, end_node=chain_end, duplicate=duplicate,
                                parent=next(parent))
        fk_controls = nt.NodeSet()
        control_parent = next(parent)
        for node, shape in zip(fk_chain, to_size_list(shape or self.DEFAULT_FK_SHAPE, len(fk_chain))):
            if node.get_children():
                control = self.build_node(nt.Control,
                                          reference_object=node,
                                          shape=shape,
                                          parent=control_parent,
                                          name_tokens=name_tokens,
                                          meta_data=meta_data,
                                          **kwargs)
                control.parent(control_parent)
                control_parent = control.node.connection_group
                rt.dcc.connections.parent(control_parent, node, maintainOffset=True)
                fk_controls.append(control)
            else:
                break
        return fk_chain, fk_controls
