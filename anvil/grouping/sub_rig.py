import base
import anvil.log as lg
import anvil.config as cfg
from anvil.objects.transform import Transform
from anvil.meta_data import MetaData


class SubRig(base.AbstractGrouping):
    BUILT_IN_NAME_TOKENS = MetaData(base.AbstractGrouping.BUILT_IN_NAME_TOKENS)
    ROOT_NAME_TOKENS = {cfg.RIG_TYPE: cfg.SUB_RIG_TOKEN, cfg.TYPE: cfg.GROUP_TYPE}
    LOG = lg.obtainLogger(__name__)
    SUB_GROUPS = ['surfaces', 'joints', 'controls', 'nodes', 'world']

    def build(self, parent=None, **kwargs):
        super(SubRig, self).build(**kwargs)
        if self.root is None:
            self.build_node(Transform, meta_data=self.meta_data,
                            name_tokens=self.name_tokens + {cfg.RIG_TYPE: cfg.SUB_RIG_TYPE, cfg.TYPE: cfg.GROUP_TYPE},
                            **self.build_kwargs)
            print(self.hierarchy)
            self.root = self.group_top = self.hierarchy[cfg.NODE_TYPE][-1]

        for main_group_type in self.SUB_GROUPS:
            self.build_node(Transform, parent=self.root, meta_data=self.meta_data,
                            name_tokens=self.name_tokens + {cfg.CHILD_TYPE: main_group_type, cfg.TYPE: cfg.GROUP_TYPE},
                            **self.build_kwargs)
            print(self.hierarchy)
            setattr(self, '%s_%s' % (cfg.GROUP_TYPE, main_group_type), self.hierarchy[cfg.NODE_TYPE][-1])
        print(self.group_world)
        self.group_world.inheritsTransform.set(False)

        self.parent(parent)
        self.initialize_sub_rig_attributes()
        self.connect_rendering_delegate()

        self.info('Built %s: %s', self.__class__.__name__, self)
