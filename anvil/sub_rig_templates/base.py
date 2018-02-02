import anvil.runtime as rt
from anvil.meta_data import MetaData
import anvil.node_types as nt
import anvil.objects.attribute as at
import anvil.config as cfg


class SubRigTemplate(nt.SubRig):
    BUILT_IN_ATTRIBUTES = nt.SubRig.BUILT_IN_ATTRIBUTES.merge({cfg.IKFK_BLEND: at.ZERO_TO_ONE_KWARGS}, new=True)

    def build_fk_chain(self, layout_joints, **kwargs):
        self.fk_chain = nt.HierarchyChain(layout_joints, duplicate=True, parent=self.group_joints)
        kwargs[cfg.PARENT] = self.group_controls

        for index, joint in enumerate(self.fk_chain):
            kwargs[cfg.REFERENCE_OBJECT] = joint
            kwargs[cfg.NAME_TOKENS] = {cfg.PURPOSE: cfg.FK, cfg.VARIATION: index}
            control = self.build_node(nt.Control, '%s_%s_%d' % (cfg.CONTROL_TYPE, cfg.FK, index), **kwargs)
            kwargs[cfg.PARENT] = getattr(control, cfg.CONNECTION_GROUP)
            rt.dcc.connections.parent(getattr(control, cfg.CONNECTION_GROUP), joint)

    def build_ik_chain(self, layout_joints, ik_end_index=-1, solver=cfg.IK_RP_SOLVER, **kwargs):
        kwargs = MetaData(kwargs)

        # build ik from joint chain
        self.ik_chain = nt.HierarchyChain(layout_joints, duplicate=True, parent=self.group_joints)
        handle, effector = self.ik_chain.build_ik(chain_end=self.ik_chain[ik_end_index], parent=self.group_nodes)

        # register ik handle and ik effector for passing metadata
        for node, label in zip([handle, effector], [cfg.IK_HANDLE, cfg.IK_EFFECTOR]):
            self.register_node(label, handle, name_tokens={cfg.NAME: cfg.IK, cfg.TYPE: label})

        # build ik control
        self.build_node(nt.Control, '%s_%s' % (cfg.CONTROL_TYPE, cfg.IK),
                        **(kwargs + {cfg.PARENT: self.group_controls,
                                     cfg.REFERENCE_OBJECT: self.ik_chain[-1],
                                     cfg.SHAPE: cfg.DEFAULT_IK_SHAPE,
                                     cfg.NAME_TOKENS: {cfg.PURPOSE: cfg.IK}}))

        # build pole vector control if using RP solver.
        if solver == cfg.IK_RP_SOLVER:
            self.build_pole_vector_control(self.ik_chain, self.ik_handle,
                                           '%s_%s_%s' % (cfg.CONTROL_TYPE, cfg.IK, cfg.POLE_VECTOR),
                                           **(kwargs + {cfg.SHAPE: cfg.DEFAULT_PV_SHAPE,
                                                        cfg.NAME_TOKENS: {cfg.PURPOSE: cfg.POLE_VECTOR}}))

        rt.dcc.connections.translate(self.control_ik.connection_group, self.ik_handle)

    def build_blend_chain(self, layout_joints, use_layout, source_chains=None, **kwargs):
        if source_chains is None:
            source_chains = [getattr(self, chain) for chain in ['%s_chain' % cfg.IK, '%s_chain' % cfg.FK] if
                             hasattr(self, chain)]

        if not source_chains:
            raise ValueError('No fk/ik chains detected...cannot build a blend chain without something to blend to!')

        self.blend_chain = nt.HierarchyChain(layout_joints, duplicate=not use_layout, parent=self.group_joints)

        for bl, source_chains in zip(self.blend_chain, zip(*source_chains)):
            blender = rt.dcc.create.create_node(cfg.BLENDER)
            blender.output.connect(bl.rotate)

            for index, source_chain in enumerate(source_chains):
                source_chain.rotate.connect(blender.attr('color%d' % (index + 1)))

            getattr(self.root, cfg.IKFK_BLEND).connect(blender.blender)
