from base import SubRigTemplate
import anvil.node_types as nt
import anvil.config as cfg
from anvil.meta_data import MetaData


class BipedFoot(SubRigTemplate):
    TOE = 'toe'
    BALL = 'ball'
    ANKLE = 'ankle'
    HEEL = 'heel'
    OUTSOLE = 'outsole'
    INSOLE = 'insole'
    BUILT_IN_META_DATA = MetaData(SubRigTemplate.BUILT_IN_META_DATA + {'name': 'foot'})

    def __init__(self, heel, outsole=None, insole=None, *args, **kwargs):
        super(BipedFoot, self).__init__(*args, **kwargs)
        self.heel = heel
        self.outsole = outsole
        self.insole = insole

    def build(self, parent=None, meta_data=None, **kwargs):
        super(BipedFoot, self).build(meta_data=meta_data, parent=parent, **kwargs)
        last = self.group_controls
        for reference_object, label in zip(self.layout_joints + self.heel,
                                           [self.ANKLE, self.TOE, self.BALL, self.HEEL]):
            shape = '%s_%s' % (cfg.CIRCLE, cfg.X) if not label == self.ANKLE else '_'.join(
                [s for s in [self.meta_data.get(cfg.SIDE), cfg.FOOT] if s])

            control = self.build_node(nt.Control, '%s_%s' % (cfg.CONTROL_TYPE, label),
                                      shape=shape,
                                      reference_object=reference_object,
                                      parent=last,
                                      meta_data=self.meta_data + {cfg.NAME: label})
            # if label == self.ANKLE:
            # control.offset_group.translate_node(absolute=True)
            last = control.connection_group

        toe_ball_chain = nt.HierarchyChain(*self.layout_joints[1:], node_filter=cfg.JOINT_TYPE)
        ball_handle, ball_effector = toe_ball_chain.build_ik(solver=cfg.IK_SC_SOLVER)
        self.register_node('%s_%s' % (self.meta_data.name, cfg.IK_HANDLE), ball_handle)
        self.register_node('%s_%s' % (self.meta_data.name, cfg.IK_EFFECTOR), ball_effector)

        self.rename()
