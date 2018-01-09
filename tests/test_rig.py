import anvil.node_types as nt
import anvil.config as cfg
from base_test import TestBase


class TestBaseRig(TestBase):
    pass


class TestRigBuild(TestBaseRig):
    @TestBase.delete_created_nodes
    def test_default(self):
        # self.test_rig.hierarchy)
        pass

class TestRigRename(TestBaseRig):
    @TestBase.delete_created_nodes
    def test_default_names(self):
        test_rig = nt.Rig()
        test_rig.build()
        print(test_rig.group_top)
        print(test_rig.control_universal)
        print(test_rig.control_universal.control)
        print(test_rig.control_universal.connection_group)
        print(test_rig.control_universal.offset_group)
        for node in test_rig.SUB_GROUPINGS:
            print(getattr('%s_%s' % (cfg.GROUP_TYPE, node)))
        """
        self.build_node(ot.Transform,
                        'group_top',
                        name_tokens={cfg.RIG: cfg.RIG, cfg.TYPE: cfg.GROUP_TYPE},
                        **kwargs)

        self.build_node(control.Control,
                    '%s_universal' % cfg.CONTROL_TYPE,
                    parent=self.group_top,
                    shape=cfg.DEFAULT_UNIVERSAL_SHAPE,
                    scale=5,
                    name_tokens={cfg.CHILD_TYPE: 'universal'})

        name_tokens={cfg.CHILD_TYPE: main_group_type, cfg.TYPE: cfg.GROUP_TYPE})
        """