import base
import anvil.objects as ot


class SubRig(base.AbstractGrouping):
    def __init__(self, *args, **kwargs):
        super(SubRig, self).__init__(*args, **kwargs)
        self.meta_data['rig'] = 'subrig'

    def build(self, meta_data=None, **flags):
        self.build_node(ot.Transform,
                        'group_top',
                        meta_data={'childtype': 'rig', 'type': 'group'},
                        **flags)

        for main_group_type in ['surfaces', 'joints', 'controls', 'nodes', 'world']:
            group_name = 'group_%s' % main_group_type
            self.build_node(ot.Transform,
                            group_name,
                            parent=self.group_top,
                            meta_data={'childtype': main_group_type, 'type': 'group'})

        self.top_node = self.group_top
        return self
