import anvil.config as cfg
import anvil.node_types as nt
from anvil.rig_templates import Biped
import base_test


class TestBaseTemplateRigs(base_test.TestBase):
    name_tokens = {'name': 'eye', 'purpose': 'mvp'}
    test_rig = None
    TEMPLATE_CLASS = None


class TestBuildBiped(TestBaseTemplateRigs):
    CLASS = Biped

    @classmethod
    def from_template_file(cls, template_file, **kwargs):
        cls.import_template_files(template_file)
        sub_rig_dict = {
            cfg.LEFT + '_' + cfg.ARM: nt.HierarchyChain('l_armA_JNT'),
            cfg.RIGHT + '_' + cfg.ARM: nt.HierarchyChain('r_armA_JNT'),
            #cfg.LEFT + '_' + cfg.HAND: nt.HierarchyChain('l_handA_JNT'),
            #cfg.RIGHT + '_' + cfg.HAND: nt.HierarchyChain('r_handA_JNT'),
            cfg.LEFT + '_' + cfg.LEG: nt.HierarchyChain('l_legA_JNT'),
            cfg.RIGHT + '_' + cfg.LEG: nt.HierarchyChain('r_legA_JNT'),
            #cfg.LEFT + '_' + cfg.FOOT: nt.HierarchyChain('l_footA_JNT'),
            #cfg.RIGHT + '_' + cfg.FOOT: nt.HierarchyChain('r_footA_JNT'),
            cfg.SPINE: nt.HierarchyChain('spineA_JNT'),
            #cfg.NECK: nt.HierarchyChain('neckA_JNT'),
            #cfg.HEAD: nt.HierarchyChain('headA_JNT'),
        }
        rig_instance = cls.CLASS(sub_rig_dict, meta_data= {cfg.NAME: 'hombre'}, **kwargs).build()
        return rig_instance

    @base_test.TestBase.delete_created_nodes
    def test_build_with_parent_t_pose(self):
        parent = nt.Transform.build(name='test')
        rig_instance = self.from_template_file(self.TPOSE, parent=parent)
        self.assertEqual(str(rig_instance.group_top.get_parent()), str(parent))

    @base_test.TestBase.delete_created_nodes
    def test_build_with_parent_a_pose(self):
        parent = nt.Transform.build(name='test')
        rig_instance = self.from_template_file(self.APOSE, parent=parent)
        self.assertEqual(str(rig_instance.root.get_parent()), str(parent))
