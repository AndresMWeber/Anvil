from base import SubRigTemplate
import anvil.node_types as nt
import anvil.config as cfg
import anvil.runtime as rt

class BipedFoot(SubRigTemplate):
    BUILT_IN_NAME_TOKENS = SubRigTemplate.BUILT_IN_NAME_TOKENS.merge({cfg.NAME: cfg.FOOT}, new=True)
    TOE_TOKEN = 'toe'
    BALL_TOKEN = 'ball'
    ANKLE_TOKEN = 'ankle'
    HEEL_TOKEN = 'heel'
    OUTSOLE_TOKEN = 'outsole'
    INSOLE_TOKEN = 'insole'

    DEFAULT_SHAPE = '_'.join([cfg.CIRCLE, cfg.X])
    SHAPES = {
        cfg.DEFAULT: DEFAULT_SHAPE,
        TOE_TOKEN: DEFAULT_SHAPE,
        BALL_TOKEN: DEFAULT_SHAPE,
        HEEL_TOKEN: DEFAULT_SHAPE,
        ANKLE_TOKEN: {cfg.LEFT: '_'.join([cfg.LEFT, cfg.FOOT]),
                      cfg.RIGHT: '_'.join([cfg.LEFT, cfg.RIGHT])},
    }

    def __init__(self, heel=None, outsole=None, insole=None, has_ik=False, leg_ik=None, *args, **kwargs):
        super(BipedFoot, self).__init__(*args, **kwargs)
        self.ankle, self.ball, self.toe, self.toe_end = self.layout_joints
        self.heel = heel
        self.outsole = outsole
        self.insole = insole
        self.has_ik = has_ik
        self.leg_ik = leg_ik

    def get_control_shape(self, label):
        shape = self.DEFAULT_SHAPE
        if label != self.ANKLE_TOKEN:
            shape = self.SHAPES.get(label)
        else:
            try:
                shape = self.SHAPES[label].get(self.name_tokens.side)
            except AttributeError:
                pass
        return shape

    def build(self, **kwargs):
        super(BipedFoot, self).build(**kwargs)

        last = self.group_controls

        for reference_object, label in zip([self.ankle, self.heel, self.toe, self.ball],
                                           [self.ANKLE_TOKEN, self.HEEL_TOKEN, self.TOE_TOKEN, self.BALL_TOKEN]):
            control = self.build_node(nt.Control, '%s_%s' % (cfg.CONTROL_TYPE, label),
                                      shape=self.get_control_shape(label),
                                      reference_object=reference_object,
                                      parent=last,
                                      rotate=False,
                                      name_tokens={cfg.PURPOSE: label})
            if not self.has_ik:
                rt.dcc.connections.parent(control.connection_group, reference_object, maintainOffset=True)
            last = control.connection_group

        # self.control_ankle.control.transform_shape(0, mode=cfg.TRANSLATE, relative=False)
        if self.has_ik:
            self.build_ik_toe()

        self.rename()

    def build_ik_toe(self):
        toe_ball_chain = nt.HierarchyChain(self.toe, node_filter=cfg.JOINT_TYPE)
        result = self.build_ik(toe_ball_chain, solver=cfg.IK_SC_SOLVER, parent=self.group_nodes)
        handle, effector = result[cfg.NODE_TYPE]
        self.register_node('%s_%s' % (self.name_tokens.name, cfg.IK_HANDLE), handle,
                           name_tokens={cfg.NAME: self.BALL_TOKEN, cfg.TYPE: cfg.IK_HANDLE})
        self.register_node('%s_%s' % (self.name_tokens.name, cfg.IK_EFFECTOR), effector,
                           name_tokens={cfg.NAME: self.BALL_TOKEN, cfg.TYPE: cfg.IK_EFFECTOR})
        if self.leg_ik:
            self.leg_ik.parent(self.ball)
