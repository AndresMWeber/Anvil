import base
import anvil.log as lg
import anvil.objects as ot
import anvil.runtime as rt
from control import Control


class SubRig(base.AbstractGrouping):
    LOG = lg.obtainLogger(__name__)

    def __init__(self, *args, **kwargs):
        super(SubRig, self).__init__(*args, **kwargs)

    def build(self, parent=None, meta_data=None, **flags):
        self.LOG.info('Building sub-rig %s' % self)
        self.meta_data = self.merge_dicts(self.meta_data, meta_data or {})
        if self.root is None:
            self.build_node(ot.Transform,
                            'group_top',
                            meta_data=self.merge_dicts(self.meta_data, {'rig': 'subrig', 'type': 'group'}),
                            **flags)
            self.root = self.group_top

        for main_group_type in ['surfaces', 'joints', 'controls', 'nodes', 'world']:
            group_name = 'group_%s' % main_group_type
            self.build_node(ot.Transform,
                            group_name,
                            parent=self.root,
                            meta_data=self.merge_dicts(self.meta_data, {'childtype': main_group_type, 'type': 'group'}))

        self.group_world.inheritsTransform.set(False)
        self.parent(parent)
        return self

    def build_pole_vector_control(self, reference_transforms, meta_data=None, **flags):
        """ Point constraint to the two base positions, aim constrain to the other objects
            Delete constraints then move the control outside of the reference transforms in the aim direction.
        """
        control = Control.build(meta_data=meta_data, **flags)
        aim_constraint = rt.dcc.constrain.aim(reference_transforms[1:-1],
                                              str(control),
                                              maintain_offset=False,
                                              upObject=str(reference_transforms[0]))
        point_constraint = rt.dcc.constrain.position([reference_transforms[0], reference_transforms[-1]],
                                                     str(control),
                                                     maintain_offset=False)
