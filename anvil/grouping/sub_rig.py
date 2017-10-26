import base
import anvil.objects as ot


class SubRig(base.AbstractGrouping):
    def __init__(self, *args, **kwargs):
        super(SubRig, self).__init__(*args, **kwargs)
        self.meta_data['purpose'] = 'subRig'

    @classmethod
    def build(cls, meta_data=None, **flags):
        instance = cls(meta_data=meta_data, **flags)
        instance.build_node(ot.Transform,
                            'group_top',
                            meta_data={'childtype': 'rig', 'type': 'group'},
                            **flags)

        for main_group_type in ['surfaces', 'joints', 'controls', 'nodes', 'world']:
            group_name = 'group_%s' % main_group_type
            instance.build_node(ot.Transform,
                                group_name,
                                parent=instance.group_top,
                                meta_data={'childtype': main_group_type, 'type': 'group'})

        instance.top_node = instance.group_top
        return instance
