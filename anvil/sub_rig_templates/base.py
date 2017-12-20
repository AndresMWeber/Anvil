import anvil.runtime as rt
from anvil.meta_data import MetaData
import anvil.node_types as nt
import anvil.config as cfg


class SubRigTemplate(nt.SubRig):
    BUILT_IN_META_DATA = MetaData(nt.SubRig.BUILT_IN_META_DATA + {cfg.NAME: 'untitled'})
    BUILT_IN_ATTRIBUTES = nt.SubRig.BUILT_IN_ATTRIBUTES + {cfg.IKFK_BLEND: {cfg.ATTRIBUTE: cfg.FLOAT,
                                                                            cfg.MIN_VALUE: 0,
                                                                            cfg.MAX_VALUE: 1,
                                                                            cfg.DEFAULT_VALUE: 0,
                                                                            cfg.KEYABLE: True}}

    def __init__(self, *args, **kwargs):
        super(SubRigTemplate, self).__init__(*args, **kwargs)

    def build_fk_chain(self, layout_joints, **kwargs):
        self.fk_chain = nt.HierarchyChain(layout_joints, duplicate=True, parent=self.group_joints)
        parent = self.group_controls

        for index, joint in enumerate(self.fk_chain):
            control = self.build_node(nt.Control, '%s_%s_%d' % (cfg.CONTROL_TYPE, cfg.FK, index),
                                      parent=parent,
                                      reference_object=joint,
                                      meta_data={cfg.PURPOSE: cfg.FK, cfg.VARIATION: index},
                                      **kwargs)
            parent = control.connection_group
            rt.dcc.connections.parent(control.connection_group, joint)

    def build_ik_chain(self, layout_joints, ik_end_index=-1, solver=cfg.IK_RP_SOLVER, **kwargs):
        kwargs = MetaData(kwargs)
        self.ik_chain = nt.HierarchyChain(layout_joints, duplicate=True, parent=self.group_joints)

        handle, effector = self.ik_chain.build_ik(chain_end=self.ik_chain[ik_end_index], parent=self.group_nodes)
        for node, label in zip([handle, effector], [cfg.IK_HANDLE, cfg.IK_EFFECTOR]):
            self.register_node(label, handle, meta_data=self.meta_data + {cfg.NAME: cfg.IK, cfg.TYPE: label})

        self.build_node(nt.Control, '%s_%s' % (cfg.CONTROL_TYPE, cfg.IK),
                        meta_data=self.meta_data + {cfg.PURPOSE: cfg.IK},
                        **(kwargs + {cfg.PARENT: self.group_controls,
                                     cfg.REFERENCE_OBJECT: self.ik_chain[-1],
                                     cfg.SHAPE: cfg.DEFAULT_IK_SHAPE}))

        if solver == cfg.IK_RP_SOLVER:
            self.build_pole_vector_control(self.ik_chain, self.ik_handle,
                                           '%s_%s_%s' % (cfg.CONTROL_TYPE, cfg.IK, cfg.POLE_VECTOR),
                                           meta_data=self.meta_data + {cfg.PURPOSE: cfg.POLE_VECTOR},
                                           **(kwargs + {cfg.SHAPE: cfg.DEFAULT_PV_SHAPE}))

        rt.dcc.connections.translate(self.control_ik.connection_group, self.ik_handle)

    def build_blend_chain(self, layout_joints, use_layout, **kwargs):
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

    def prep_joint_chain_for_rigging(self, joint_chain):
        for joint in joint_chain:
            pass
        # joint_chain[-1].jointOrient.set([0, 0, 0])
