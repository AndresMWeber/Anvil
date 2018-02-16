from base import SubRigTemplate
import anvil
import anvil.node_types as nt
import anvil.config as cfg
import anvil.runtime as rt
from anvil.meta_data import MetaData


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

    def __init__(self, heel=None, outsole=None, insole=None, has_ik=True, leg_ik=None, *args, **kwargs):
        super(BipedFoot, self).__init__(*args, **kwargs)
        self.ankle, self.ball, self.toe = self.layout_joints
        self.heel = anvil.factory(heel) if heel else heel
        self.outsole = anvil.factory(outsole) if outsole else outsole
        self.insole = anvil.factory(insole) if insole else insole
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

    def build(self, duplicate=True, leg_ik=None, **kwargs):
        super(BipedFoot, self).build(**kwargs)
        self.leg_ik = leg_ik or self.leg_ik
        if duplicate:
            self.ankle, self.ball, self.toe = nt.HierarchyChain(self.layout_joints[0], end_node=self.layout_joints[-1],
                                                                duplicate=True)

        ankle_control = self.build_node(nt.Control, '%s_%s' % (cfg.CONTROL_TYPE, self.ANKLE_TOKEN),
                                        shape=self.get_control_shape(self.ANKLE_TOKEN),
                                        reference_object=self.ankle,
                                        parent=self.group_controls,
                                        rotate=False,
                                        name_tokens={cfg.PURPOSE: self.ANKLE_TOKEN})
        last = ankle_control.connection_group

        for reference_object, label in zip([self.heel, self.toe, self.ball],
                                           [self.HEEL_TOKEN, self.TOE_TOKEN, self.BALL_TOKEN]):
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
        else:
            self.build_fk_toe()

        control_hierarchy = nt.HierarchyChain(ankle_control.connection_group)
        self.insert_pivot_buffer(self.OUTSOLE_TOKEN, control_hierarchy, 0, reference_object=self.outsole)
        self.insert_pivot_buffer(self.INSOLE_TOKEN, control_hierarchy, 0, reference_object=self.insole)

        self.rename()

    def build_ik_toe(self):
        foot_ball_result = self.build_ik(nt.HierarchyChain(self.ankle, self.ball, node_filter=cfg.JOINT_TYPE),
                                         solver=cfg.IK_SC_SOLVER, parent=self.control_ball.connection_group)
        handle, effector = foot_ball_result[cfg.NODE_TYPE]
        self.register_node('%s_%s' % (self.name_tokens.name, cfg.IK_HANDLE), handle,
                           name_tokens={cfg.NAME: self.ANKLE_TOKEN, cfg.TYPE: cfg.IK_HANDLE})
        self.register_node('%s_%s' % (self.name_tokens.name, cfg.IK_EFFECTOR), effector,
                           name_tokens={cfg.NAME: self.ANKLE_TOKEN, cfg.TYPE: cfg.IK_EFFECTOR})

        ball_toe_result = self.build_ik(nt.HierarchyChain(self.ball, self.toe, node_filter=cfg.JOINT_TYPE),
                                        solver=cfg.IK_SC_SOLVER, parent=self.control_toe.connection_group)
        handle, effector = ball_toe_result[cfg.NODE_TYPE]
        self.register_node('%s_%s' % (self.name_tokens.name, cfg.IK_HANDLE), handle,
                           name_tokens={cfg.NAME: self.BALL_TOKEN, cfg.TYPE: cfg.IK_HANDLE})
        self.register_node('%s_%s' % (self.name_tokens.name, cfg.IK_EFFECTOR), effector,
                           name_tokens={cfg.NAME: self.BALL_TOKEN, cfg.TYPE: cfg.IK_EFFECTOR})
        if self.leg_ik:
            self.leg_ik.parent(self.control_ball.connection_group)
        else:
            rt.dcc.connections.parent(self.control_ball.connection_group, self.ankle)

    def insert_pivot_buffer(self, pivot, hierarchy, index, name_tokens=None, meta_data=None, **kwargs):
        try:
            buffer = hierarchy.insert_buffer(index, reference_node=getattr(self, pivot), **kwargs)
            self.register_node(pivot + '_pivot', buffer,
                               name_tokens=MetaData(name=pivot, purpose='pivot', protected='purpose') + name_tokens,
                               meta_data=meta_data)
            return buffer
        except AttributeError:
            self.warning('%r does not have pivot attribute %s...skipping' % (self, pivot))

    def build_fk_toe(self):
        md = self.register_node('ball_rotation_cancel_out',
                                rt.dcc.create.create_node(cfg.MULT_DIV_TYPE),
                                name_tokens={cfg.PURPOSE: 'cancel',
                                             cfg.TYPE: cfg.MULT_DIV_TYPE,
                                             'protected': cfg.TYPE})
        # md.input1D.connect()
