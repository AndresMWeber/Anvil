import anvil
import anvil.runtime as rt
from anvil.meta_data import MetaData
import anvil.node_types as nt
import anvil.config as cfg


class SubRigTemplate(nt.SubRig):
    BUILT_IN_META_DATA = MetaData.merge_dicts({'name': 'untitled'}, nt.SubRig.BUILT_IN_META_DATA)
    BUILT_IN_ATTRIBUTES = {cfg.IKFK_BLEND: {'attributeType': cfg.FLOAT,
                                            'min':0, 'max':1, 'defaultValue':0, 'keyable':True}}

    def __init__(self, *args, **kwargs):
        super(SubRigTemplate, self).__init__(*args, **kwargs)
        self.ini
        self.root.add_attr()


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
            rt.dcc.constrain.parent(control.connection_group, joint)

    def build_ik_chain(self, layout_joints, ik_end_index=-1, solver=cfg.IK_RP_SOLVER, **kwargs):
        self.ik_chain = nt.HierarchyChain(layout_joints, duplicate=True, parent=self.group_joints)
        handle, effector = self.ik_chain.build_ik(chain_end=self.ik_chain[ik_end_index], parent=self.group_nodes)

        self.register_node(cfg.IK_HANDLE, handle, meta_data=self.meta_data + {cfg.NAME: cfg.IK,
                                                                              cfg.TYPE: cfg.IK_HANDLE})

        self.register_node(cfg.IK_EFFECTOR, effector, meta_data=self.meta_data + {cfg.NAME: cfg.IK,
                                                                                  cfg.TYPE: cfg.IK_EFFECTOR})

        control_kwargs = {'parent': self.group_controls, 'reference_object': self.ik_chain[-1]}
        control_kwargs.update(kwargs)
        self.build_node(nt.Control, '%s_%s' % (cfg.CONTROL_TYPE, cfg.IK),
                        meta_data=self.meta_data + {cfg.PURPOSE: cfg.IK},
                        **control_kwargs)

        if solver == cfg.IK_RP_SOLVER:
            self.build_pole_vector_control(self.ik_chain, self.ik_handle,
                                           '%s_%s_%s' % (cfg.CONTROL_TYPE, cfg.IK, cfg.POLE_VECTOR),
                                           meta_data=self.meta_data + {cfg.PURPOSE: cfg.POLE_VECTOR},
                                           **kwargs)

        rt.dcc.constrain.translate(self.control_ik.connection_group, self.ik_handle)

    def build_blend_chain(self, layout_joints, use_layout, **kwargs):
        source_chains = [getattr(self, chain) for chain in ['fk_chain', 'ik_chain'] if hasattr(self, chain)]

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
