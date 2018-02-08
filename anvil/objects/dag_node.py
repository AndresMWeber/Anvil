import anvil.runtime as rt
import unicode_delegate
import attribute as at
import anvil.config as cfg
from anvil.colors import RGB


class DagNode(unicode_delegate.UnicodeDelegate):
    def buffer_connect(self, attribute, other_attribute, buffer_value, **kwargs):
        pma = rt.dcc.create.create_node(cfg.ADD_SUB_TYPE)
        self.attr(attribute).connect(pma.input1D[0])
        pma.input1D[1].set(buffer_value)
        pma.output1D.connect(other_attribute, **kwargs)

    def _resolve_attribute_name(self, attribute_name):
        return '%s%s%s' % (self, cfg.ATTR_DELIMITER, attribute_name)

    def duplicate(self, keep_inputs=False, include_children=False, include_parents=False, rename_children=True,
                  **kwargs):
        kwargs['inputConnections'] = keep_inputs
        kwargs['parentOnly'] = include_children
        kwargs['renameChildren'] = rename_children
        kwargs['upstreamNodes'] = include_parents
        return self.__class__(rt.dcc.scene.duplicate(self.name(), **kwargs)[0])

    def add_attr(self, attribute, **kwargs):
        rt.dcc.connections.add_attr(self, longName=attribute, **kwargs)
        return at.Attribute(self._resolve_attribute_name(attribute))

    def get_attr(self, attribute, **kwargs):
        return self.attr(attribute).get(**kwargs)

    def attr(self, attribute):
        return at.Attribute(self._resolve_attribute_name(attribute))

    def connect_attr(self, attribute_source, attribute_destination, **kwargs):
        self.attr(attribute_source).connect(at.Attribute(attribute_destination), **kwargs)

    def colorize(self, rgb_or_index):
        self.attr(cfg.OVERRIDE_ENABLED).set(True)

        if isinstance(rgb_or_index, int):
            self.info('Setting display as index on %s from %s', self, rgb_or_index)
            self.attr(cfg.OVERRIDE_RGB).set(False)
            self.attr(cfg.OVERRIDE_COLOR_INDEX).set(rgb_or_index)

        elif len(rgb_or_index) == 3:
            rgb_or_index = RGB(*rgb_or_index) if isinstance(rgb_or_index, (list, tuple)) else rgb_or_index
            self.info('Setting display as rgb on %s from %s', self, rgb_or_index)
            self.attr(cfg.OVERRIDE_RGB).set(True)
            self.attr(cfg.OVERRIDE_COLOR_RGB).set(rgb_or_index.as_rgb_normalized())

        return rgb_or_index

    def __getattr__(self, item):
        if item in rt.dcc.connections.list_attr(self):
            return at.Attribute('%s.%s' % (self, item))
        else:
            return super(DagNode, self).__getattr__(item)
