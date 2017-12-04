import anvil
import anvil.runtime as rt
import anvil.node_types as nt
import anvil.templates.rig.biped as biped
import base_test


class TestBaseTemplateRigs(base_test.TestBase):
    name_tokens = {'name': 'eye', 'purpose': 'mvp'}
    test_rig = None
    TEMPLATE_CLASS = None


class TestBuildBiped(TestBaseTemplateRigs):
    CLASS = biped.Biped()

    def test_build(self, template_file):
        self.import_template_files(template_file)
        l_arm = nt.HierarchyChain('l_armA_JNT')
        r_arm = nt.HierarchyChain('r_armA_JNT')
        l_leg = nt.HierarchyChain('l_legA_JNT')
        r_leg = nt.HierarchyChain('r_legA_JNT')
        spine = nt.HierarchyChain('spineA_JNT')
        head = nt.HierarchyChain('headA_JNT')
        neck = nt.HierarchyChain('neckA_JNT')
        l_hand = nt.HierarchyChain('l_handA_JNT')
        r_hand = nt.HierarchyChain('r_handA_JNT')
        l_foot = nt.HierarchyChain('l_footA_JNT')
        r_foot = nt.HierarchyChain('r_footA_JNT')

        rig_instance = self.CLASS(l_arm=l_arm,
                                  r_arm=l_arm,
                                  l_leg=l_leg,
                                  r_leg=r_leg,
                                  l_hand=l_hand,
                                  r_hand=r_hand,
                                  l_foot=l_foot,
                                  r_foot=r_foot,
                                  neck=neck,
                                  head=head,
                                  spine=spine,
                                  template_flags={'meta_data': {'side': 'left'}})
        return rig_instance

    @base_test.TestBase.delete_created_nodes
    def test_build_with_parent(self):
        parent = nt.Transform.build(name='test')
        sub_rig_instance = self.runner(template_flags={'parent': parent})
        self.assertEqual(str(sub_rig_instance.group_top.get_parent()), str(parent))
