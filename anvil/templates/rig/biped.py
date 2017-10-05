import anvil.templates.sub_rig as sub_rig_template
import anvil.core.collections.rig as rig
import anvil.core.collections.hierarchy as hierarchy

class Biped(rig.Rig):

    @classmethod
    def create(cls):
        build_hierarchy = hierarchy.Hierarchy()
        build_hierarchy.set_root(sub_rig_template.center_of_mass())

        left_arm = sub_rig_template.biped_arm(side='left'),
        left_arm = sub_rig_template.biped_arm(side='right'),
        left_arm = sub_rig_template.biped_leg(side='left'),
        left_arm = sub_rig_template.biped_leg(side='right'),
        left_arm = sub_rig_template.spine(),
        left_arm = sub_rig_template.neck(),
        left_arm = sub_rig_template.head()

    def setup_sub_rig_connections(self):
        pass