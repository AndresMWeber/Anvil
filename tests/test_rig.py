import anvil.node_types as nt
import anvil.config as cfg
from base_test import TestBase, clean_up_scene


class TestBaseRig(TestBase):
    pass


class TestRigBuild(TestBaseRig):
    @clean_up_scene
    def test_hierarchy_length(self):
        test_rig = nt.Rig()
        test_rig.build()
        self.assertEqual(len(list(test_rig.hierarchy)), 5)


class TestRigRename(TestBaseRig):
    @clean_up_scene
    def test_default_names(self):
        test_rig = nt.Rig()
        test_rig.build()
        self.assertEqual(str(test_rig.group_top), "rig_untitled_GRP")
        self.assertEqual(str(test_rig.control_universal.control), "untitled_universal_CTR")
        self.assertEqual(str(test_rig.control_universal.connection_group), "untitled_universal_CGP")
        self.assertEqual(str(test_rig.control_universal.offset_group), "untitled_universal_OGP")

        for node in test_rig.SUB_GROUPINGS:
            self.assertEqual(getattr(test_rig, '%s_%s' % (cfg.GROUP_TYPE, node)), 'untitled_%s_GRP' % node)
