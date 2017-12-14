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
            cfg.LEFT + '_' + cfg.ARM: {cfg.LAYOUT: nt.HierarchyChain('l_armA_JNT', 'l_armC_JNT'), 'pre_scale': .3},
            cfg.RIGHT + '_' + cfg.ARM: {cfg.LAYOUT: nt.HierarchyChain('r_armA_JNT', 'r_armC_JNT'), 'pre_scale': .3},
            cfg.LEFT + '_' + cfg.LEG: {cfg.LAYOUT: nt.HierarchyChain('l_legA_JNT', 'l_legC_JNT'), 'pre_scale': .3},
            cfg.RIGHT + '_' + cfg.LEG: {cfg.LAYOUT: nt.HierarchyChain('r_legA_JNT', 'r_legC_JNT'), 'pre_scale': .3},
            cfg.LEFT + '_' + cfg.FOOT: nt.HierarchyChain('l_legC_JNT', 'l_foot_toeEnd_JNT'),
            cfg.RIGHT + '_' + cfg.FOOT: nt.HierarchyChain('r_legC_JNT', 'r_foot_toeEnd_JNT'),
            cfg.SPINE: nt.HierarchyChain('spineA_JNT', 'spineE_JNT'),
            cfg.NECK: nt.HierarchyChain('neckA_JNT', 'neckEnd_JNT'),
            cfg.HEAD: nt.HierarchyChain('headA_JNT', 'headEnd_JNT'),
        }

        finger_start = '%s_finger_%s_A_JNT'
        finger_end = '%s_finger_%s_D_JNT'
        for side in [cfg.LEFT, cfg.RIGHT]:
            fingers = []
            for finger in ['thb', 'ind', 'mid', 'rng', 'pnk']:
                fingers.append(nt.HierarchyChain(finger_start % (side[0], finger),
                                                 finger_end % (side[0], finger)))
            sub_rig_dict[side + '_' + cfg.HAND] = {'finger_joints': fingers, 'pre_scale': 0.1}

        rig_instance = cls.CLASS(sub_rig_dict, meta_data={cfg.NAME: 'hombre'}, **kwargs)
        rig_instance.build(**kwargs)
        return rig_instance

    @base_test.TestBase.delete_created_nodes
    def test_build_with_parent_t_pose(self):
        parent = nt.Transform.build(name='test')
        rig_instance = self.from_template_file(self.TPOSE, parent=parent)
        self.assertEqual(str(rig_instance.root.get_parent()), str(parent))

    @base_test.TestBase.delete_created_nodes
    def test_build_with_parent_a_pose(self):
        parent = nt.Transform.build(name='test')
        rig_instance = self.from_template_file(self.APOSE, parent=parent)
        self.assertEqual(str(rig_instance.root.get_parent()), str(parent))
