import base
import anvil.log as lg
import anvil.config as cfg
from anvil.objects.transform import Transform
from anvil.meta_data import MetaData


class SubRig(base.AbstractGrouping):
    BUILT_IN_NAME_TOKENS = MetaData(base.AbstractGrouping.BUILT_IN_NAME_TOKENS)
    ROOT_NAME_TOKENS = {cfg.RIG_TYPE: cfg.SUB_RIG_TOKEN, cfg.TYPE: cfg.GROUP_TYPE}
    LOG = lg.obtain_logger(__name__)
    SUB_GROUPS = ['surfaces', 'joints', 'controls', 'nodes', 'world']

    def build(self, parent=None, **kwargs):
        super(SubRig, self).build(**kwargs)
        if self.root is None:
            self.build_node(Transform,
                            hierarchy_id='%s_%s' % (cfg.GROUP_TYPE, 'top'),
                            meta_data=self.meta_data,
                            name_tokens=self.name_tokens + {cfg.RIG_TYPE: cfg.SUB_RIG_TYPE, cfg.TYPE: cfg.GROUP_TYPE},
                            **self.build_kwargs)
            self.root = self.hierarchy[cfg.NODE_TYPE][cfg.DEFAULT][-1]

        for main_group_type in self.SUB_GROUPS:
            hierarchy_id = '%s_%s' % (cfg.GROUP_TYPE, main_group_type)
            self.build_node(Transform,
                            hierarchy_id=hierarchy_id,
                            parent=self.root,
                            meta_data=self.meta_data,
                            name_tokens=self.name_tokens + {cfg.CHILD_TYPE: main_group_type, cfg.TYPE: cfg.GROUP_TYPE},
                            **self.build_kwargs)
            setattr(self, hierarchy_id, self.hierarchy[cfg.NODE_TYPE][hierarchy_id])
        self.group_world.inheritsTransform.set(False)

        self.parent(parent)
        self.initialize_sub_rig_attributes()
        self.connect_rendering_delegate()

        self.info('Built %s: %s', self.__class__.__name__, self)
