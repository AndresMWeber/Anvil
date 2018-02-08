import anvil.config as cfg
import anvil.node_types as nt
from anvil.rig_templates import Biped
from tests.base_test import TestBase, cleanup_nodes


class TestBaseTemplateRigs(TestBase):
    name_tokens = {'name': 'eye', 'purpose': 'mvp'}
    test_rig = None
    TEMPLATE_CLASS = None
    CLASS = Biped

    @classmethod
    def from_template_file(cls, template_file, **kwargs):
        cls.import_template_files(template_file)

        sub_rig_dict = {
            cfg.LEFT + '_' + cfg.ARM: {cfg.LAYOUT: nt.HierarchyChain('l_armA_JNT', 'l_armC_JNT')},
            cfg.RIGHT + '_' + cfg.ARM: {cfg.LAYOUT: nt.HierarchyChain('r_armA_JNT', 'r_armC_JNT')},
            cfg.LEFT + '_' + cfg.LEG: {cfg.LAYOUT: nt.HierarchyChain('l_legA_JNT', 'l_legC_JNT')},
            cfg.RIGHT + '_' + cfg.LEG: {cfg.LAYOUT: nt.HierarchyChain('r_legA_JNT', 'r_legC_JNT')},
            cfg.LEFT + '_' + cfg.FOOT: {cfg.LAYOUT: nt.HierarchyChain('l_legC_JNT', 'l_foot_toeEnd_JNT'),
                                        'heel': 'l_foot_heel_JNT'},
            cfg.RIGHT + '_' + cfg.FOOT: {cfg.LAYOUT: nt.HierarchyChain('r_legC_JNT', 'r_foot_toeEnd_JNT'),
                                         'heel': 'r_foot_heel_JNT'},
            cfg.SPINE: nt.HierarchyChain('spineA_JNT', 'spineE_JNT'),
            cfg.NECK: nt.HierarchyChain('neckA_JNT', 'neckEnd_JNT'),
            cfg.HEAD: nt.HierarchyChain('headA_JNT', 'headEnd_JNT'),
        }

        finger_start = '%s_finger_%s_A_JNT'
        finger_end = '%s_finger_%s_D_JNT'
        for side in [cfg.LEFT, cfg.RIGHT]:
            fingers = []
            for finger in ['thb', 'ind', 'mid', 'rng', 'pnk']:
                fingers.append(nt.HierarchyChain(finger_start % (side[0], finger), finger_end % (side[0], finger)))
            sub_rig_dict[side + '_' + cfg.HAND] = {cfg.LAYOUT: fingers, cfg.SCALE: 0.3}

        rig_instance = cls.CLASS(sub_rig_dict=sub_rig_dict, name_tokens={cfg.CHARACTER: 'hombre'}, **kwargs)
        rig_instance.build(**kwargs)
        return rig_instance


class TestBuildBiped(TestBaseTemplateRigs):
    def test_build_with_parent_t_pose(self):
        with cleanup_nodes():
            parent = nt.Transform.build(name='test')
            rig_instance = self.from_template_file(self.TPOSE, parent=parent)
            self.assertEqual(str(rig_instance.root.get_parent()), str(parent))

    def test_build_with_parent_a_pose(self):
        with cleanup_nodes():
            parent = nt.Transform.build(name='test')
            rig_instance = self.from_template_file(self.APOSE, parent=parent)
            self.assertEqual(str(rig_instance.root.get_parent()), str(parent))

    def test_sub_rigs(self):
        with cleanup_nodes():
            rig_instance = self.from_template_file(self.APOSE)
            self.assertEqual(sorted(list(rig_instance.sub_rigs)), sorted(list(rig_instance.SUB_RIG_BUILD_TABLE)))
