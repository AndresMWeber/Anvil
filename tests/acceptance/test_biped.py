import anvil.config as cfg
import anvil.node_types as nt
from anvil.rig_templates import Biped
from tests.base_test import TestBase, clean_up_scene, auto_save_result


class TestBaseTemplateRigs(TestBase):
    meta_data = {'name': 'eye', 'purpose': 'mvp'}
    test_rig = None
    TEMPLATE_CLASS = None
    CLASS = Biped

    @classmethod
    def from_template_file(cls, template_file, **kwargs):
        cls.import_template_files(template_file)
        sub_rig_dict = {
            cfg.LEFT + '_' + cfg.ARM: {cfg.LAYOUT: nt.NodeChain('l_armA_JNT', 'l_armC_JNT')},
            cfg.RIGHT + '_' + cfg.ARM: {cfg.LAYOUT: nt.NodeChain('r_armA_JNT', 'r_armC_JNT')},
            cfg.LEFT + '_' + cfg.LEG: {cfg.LAYOUT: nt.NodeChain('l_legA_JNT', 'l_legC_JNT')},
            cfg.RIGHT + '_' + cfg.LEG: {cfg.LAYOUT: nt.NodeChain('r_legA_JNT', 'r_legC_JNT')},
            cfg.LEFT + '_' + cfg.FOOT: {cfg.LAYOUT: nt.NodeChain('l_legC_JNT', 'l_foot_toe_JNT'),
                                        'heel': 'l_foot_heel_JNT'},
            cfg.RIGHT + '_' + cfg.FOOT: {cfg.LAYOUT: nt.NodeChain('r_legC_JNT', 'r_foot_toe_JNT'),
                                         'heel': 'r_foot_heel_JNT'},
            cfg.SPINE: nt.NodeChain('spineA_JNT', 'spineE_JNT'),
            cfg.NECK: nt.NodeChain('neckA_JNT', 'neckEnd_JNT'),
            cfg.HEAD: nt.NodeChain('headA_JNT', 'headEnd_JNT'),
        }
        finger_labels = ['thb', 'ind', 'mid', 'rng', 'pnk']
        finger_start, finger_end = '%s_finger_%s_A_JNT', '%s_finger_%s_D_JNT'
        for side in [cfg.LEFT, cfg.RIGHT]:
            fingers = []
            for finger in finger_labels:
                fingers.append(
                    nt.NodeChain(finger_start % (side[0], finger), finger_end % (side[0], finger)))
            sub_rig_dict[side + '_' + cfg.HAND] = {cfg.LAYOUT: fingers, 'scale': 0.3}

        rig_instance = cls.CLASS(sub_rig_dict=sub_rig_dict, meta_data={cfg.CHARACTER: 'hombre'}, **kwargs)
        rig_instance.build(**kwargs)
        return rig_instance


class TestBuildBiped(TestBaseTemplateRigs):
    @clean_up_scene
    @auto_save_result
    def test_build_with_parent_t_pose(self):
        parent = nt.Transform.build(name='test')
        rig_instance = self.from_template_file(self.TPOSE, parent=parent)
        self.assertEqual(str(rig_instance.root.get_parent()), str(parent))

    @clean_up_scene
    @auto_save_result
    def test_build_with_parent_a_pose(self):
        parent = nt.Transform.build(name='test')
        rig_instance = self.from_template_file(self.APOSE, parent=parent)
        self.assertEqual(str(rig_instance.root.get_parent()), str(parent))

    @clean_up_scene
    def test_sub_rigs(self):
        rig_instance = self.from_template_file(self.APOSE)
        self.assertEqual(sorted(list(rig_instance.sub_rigs)), sorted(list(rig_instance.SUB_RIG_BUILD_TABLE)))
