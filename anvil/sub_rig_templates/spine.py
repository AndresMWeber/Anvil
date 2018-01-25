from base import SubRigTemplate
import anvil.node_types as nt
from anvil.meta_data import MetaData
import anvil.config as cfg


class Spine(SubRigTemplate):
    BUILT_IN_META_DATA = SubRigTemplate.BUILT_IN_META_DATA.merge({'name': 'spine'}, new=True)

    def build(self, parent=None, meta_data=None, **kwargs):
        if len(self.layout_joints) < 4:
            raise ValueError('Need to input more than 4 joints in order to create a %s' % self.__class__.__name__)
        super(Spine, self).build(name_tokens=meta_data, parent=parent)

        # Build Spine Curve
        self.LOG.info('blarg, %r' % self.layout_joints)
        spine_curve = nt.Curve.build_from_objects(self.layout_joints,
                                                  parent=self.group_nodes,
                                                  meta_data=self.meta_data + {'name': 'spine', 'type': 'curve'},
                                                  degree=3)
        self.register_node('curve_spine', spine_curve)

        self.rename()
        self.LOG.info('Built sub rig %s' % self.__class__.__name__)
