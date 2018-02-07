from base import SubRigTemplate
import anvil.node_types as nt
import anvil.config as cfg


class BipedFoot(SubRigTemplate):
    BUILT_IN_NAME_TOKENS = SubRigTemplate.BUILT_IN_NAME_TOKENS.merge({cfg.NAME: cfg.FOOT}, new=True)
    TOE_TOKEN = 'toe'
    BALL_TOKEN = 'ball'
    ANKLE_TOKEN = 'ankle'
    HEEL_TOKEN = 'heel'
    OUTSOLE_TOKEN = 'outsole'
    INSOLE_TOKEN = 'insole'

    def __init__(self, heel=None, outsole=None, insole=None, *args, **kwargs):
        super(BipedFoot, self).__init__(*args, **kwargs)
        self.ankle, self.ball, self.toe, self.toe_end = self.layout_joints
        self.heel = heel
        self.outsole = outsole
        self.insole = insole

    def build(self, **kwargs):
        super(BipedFoot, self).build(**kwargs)

        last = self.group_controls
        for reference_object, label in zip([self.ankle, self.ball, self.toe, self.heel],
                                           [self.ANKLE_TOKEN, self.BALL_TOKEN, self.TOE_TOKEN, self.HEEL_TOKEN]):
            shape = '%s_%s' % (cfg.CIRCLE, cfg.X)
            if label == self.ANKLE_TOKEN:
                shape = '_'.join([s for s in [self.meta_data.get(cfg.SIDE), cfg.FOOT] if s])

            control = self.build_node(nt.Control, '%s_%s' % (cfg.CONTROL_TYPE, label),
                                      shape=shape,
                                      reference_object=reference_object,
                                      parent=last,
                                      rotate=False,
                                      name_tokens={cfg.NAME: label})
            last = control.connection_group

        self.control_ankle.control.transform_shape(0, mode=cfg.TRANSLATE, relative=False)

        toe_ball_chain = nt.HierarchyChain(self.toe, node_filter=cfg.JOINT_TYPE)
        result = self.build_ik(toe_ball_chain, solver=cfg.IK_SC_SOLVER, parent=self.group_nodes)

        self.register_node('%s_%s' % (self.name_tokens.name, cfg.IK_HANDLE), result[cfg.NODE_TYPE][0],
                           name_tokens={cfg.NAME: self.BALL_TOKEN, cfg.TYPE: cfg.IK_HANDLE})
        self.register_node('%s_%s' % (self.name_tokens.name, cfg.IK_EFFECTOR), result[cfg.NODE_TYPE][1],
                           name_tokens={cfg.NAME: self.BALL_TOKEN, cfg.TYPE: cfg.IK_EFFECTOR})

        self.rename()
