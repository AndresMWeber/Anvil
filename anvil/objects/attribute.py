import unicode_delegate
import anvil
import anvil.config as cfg
import anvil.runtime as rt


class Attribute(unicode_delegate.UnicodeDelegate):
    query = rt.dcc.connections.query_attr

    def attr_parent(self):
        return rt.dcc.scene.get_path_from_api_object(self._dcc_id.node())

    def name(self):
        return '%s%s%s' % (self.attr_parent(), cfg.ATTR_DELIMITER, self._dcc_id.partialName())

    def connect(self, destination_attribute_dag, **kwargs):
        rt.dcc.connections.connect_attr(self, destination_attribute_dag, **kwargs)

    def connections(self, **kwargs):
        return rt.dcc.connections.list_connections(self, **kwargs)

    def disconnect(self, **kwargs):
        return rt.dcc.connections.disconnect_attr(self, **kwargs)

    @classmethod
    def build(cls, *args, **kwargs):
        raise NotImplementedError('Cannot build type %s' % cls.__name__)

    def attr_dag(self):
        return self._api_class_instance.name()

    def attr_name(self):
        return self.attr_name().split(cfg.ATTR_DELIMITER)[-1]

    def node(self):
        return anvil.factory(self.name().split(cfg.ATTR_DELIMITER)[0])

    def children(self):
        return [self.__class__(attr) for attr in rt.dcc.connections.attr_query(listChildren=True)]

    def get(self, **kwargs):
        return rt.dcc.connections.get_attr(self, **kwargs)

    def get_alias(self, **kwargs):
        return rt.dcc.connections.alias_attr(self, **kwargs)

    def get_parent(self, **kwargs):
        return rt.dcc.connections.query_attr(self, listParent=True, **kwargs)

    def get_children(self, **kwargs):
        kwargs['listChildren'] = True
        return rt.dcc.connections.query_attr(self, **kwargs)

    def get_enums(self, **kwargs):
        return rt.dcc.connections.query_attr(self, listEnum=True, **kwargs)

    def get_soft_max(self):
        return self.query(self, softMax=True) if self.query(self, softMaxExists=True) else None

    def get_soft_min(self):
        return self.query(self, softMin=True) if self.query(self, softMinExists=True) else None

    def get_max(self):
        return self.query(self, maximum=True) if self.query(self, maxExists=True) else None

    def get_min(self):
        return self.query(self, minimum=True) if self.query(self, minExists=True) else None

    def get_num_elements(self):
        return rt.dcc.connections.query_attr(self, numberOfChildren=True)

    def get_range(self):
        return rt.dcc.connections.query_attr(self, node=self.node(), range=True)

    def get_siblings(self):
        return rt.dcc.connections.query_attr(self, listSiblings=True)

    def delete(self, **kwargs):
        rt.dcc.connections.delete_attr(self, **kwargs)

    def set(self, value, **kwargs):
        rt.dcc.connections.set_attr(self, value, **kwargs)

    def set_alias(self, alias, **kwargs):
        rt.dcc.connections.alias_attr(self, alias, **kwargs)

    def set_keyable(self, keyable=True, **kwargs):
        rt.dcc.connections.add_attr(self, keyable=keyable, edit=True, **kwargs)

    def set_locked(self, locked=True, **kwargs):
        rt.dcc.connections.set_attr(self, locked=locked, **kwargs)

    def set_min(self, value):
        rt.dcc.connections.add_attr(self, minValue=value, edit=True)

    def set_max(self, value):
        rt.dcc.connections.add_attr(self, maxValue=value, edit=True)

    def set_range(self, min, max):
        self.set_min(min)
        self.set_max(max)

    def set_soft_min(self, value):
        rt.dcc.connections.add_attr(self, softMinValue=value, edit=True)

    def set_soft_max(self, value):
        rt.dcc.connections.add_attr(self, softMaxValue=value, edit=True)

    def set_soft_range(self, min, max):
        self.set_soft_min(min)
        self.set_soft_max(max)

    def set_keyframe(self, **kwargs):
        return rt.dcc.animation.set_keyframe(self, **kwargs)

    def set_enums(self, enums, **kwargs):
        rt.dcc.connections.add_attr(self, edit=True, enumName=enums, **kwargs)

    def lock(self):
        self.set_locked(True)

    def unlock(self):
        self.set_locked(False)

    def mute(self, mute, **kwargs):
        rt.dcc.connections.mute(self, mute, **kwargs)

    def is_keyable(self):
        return rt.dcc.connections.add_attr(self, query=True, keyable=True)

    def is_muted(self):
        return rt.dcc.connections.mute(self, query=True)

    def isHidden(self):
        return rt.dcc.connections.query_attr(self, node=self.node(), hidden=True)

    def isConnectable(self):
        return rt.dcc.connections.query_attr(self, node=self.node(), connectable=True)

    def unmute(self, **kwargs):
        kwargs.setdefault('disable', True)
        kwargs.setdefault('force', True)
        return rt.dcc.connections.mute(self, **kwargs)

    def attribute_type(self):
        return rt.dcc.connections.add_attr(self, query=True, attributeType=True)

    def get_info(self, **kwargs):
        return rt.dcc.connections.info_attr(self, **kwargs)

    def is_destination(self, **kwargs):
        return rt.dcc.connections.connection_info(self, isDestination=True, **kwargs)

    def is_source(self, **kwargs):
        return rt.dcc.connections.connection_info(self, isSource=True, **kwargs)

    def is_connected(self, other=None, **kwargs):
        if other:
            return rt.dcc.connections.connected_attr(self, other, **kwargs)
        return rt.dcc.connections.connection_info(self, isDestination=True, **kwargs)

    def is_connected_to(self, other, **kwargs):
        other = self.__class__(other)
        if self.is_connected(other):
            return True

        if self.is_multi():
            return any([compound_attr.is_connected_to(other, **kwargs) for compound_attr in self])

        if other.is_multi():
            return any([self.is_connected_to(compound_attr, **kwargs) for compound_attr in other])

        return False

    def inputs(self, **kwargs):
        kwargs['source'] = True
        kwargs['destination'] = True
        return [self.__class__(plug) for plug in rt.dcc.connections.list_connections(self, **kwargs)]

    def outputs(self, **kwargs):
        kwargs['source'] = False
        kwargs['destination'] = False
        return [self.__class__(plug) for plug in rt.dcc.connections.list_connections(self, **kwargs)]

    def input_plugs(self, **kwargs):
        return [self.__class__(plug) for plug in
                rt.dcc.connections.list_connections(self, source=True, plugs=True, **kwargs)]

    def insert_input(self, node, in_attribute, out_attribute):
        inputs = self.inputs()
        if inputs:
            inputs[0].connect(node.attr(in_attribute))
        node.attr(out_attribute).connect(self, force=True)

    def is_dirty(self, **kwargs):
        return rt.dcc.connections.dirty_attr(**kwargs)

    def is_multi(self, **kwargs):
        return rt.dcc.connections.info_attr(self, multi=True, **kwargs)

    def is_channel_box(self, **kwargs):
        return rt.dcc.connections.set_attr(self, query=True, channelBox=True, **kwargs)

    def set_channel_box(self, value, **kwargs):
        return rt.dcc.connections.set_attr(self, value, channelBox=True, **kwargs)

    def __rshift__(self, other_attribute):
        self.connect(other_attribute)

    def __lshift__(self, other_attribute):
        other_attribute.connect(self)

    def __iter__(self):
        if self.isMulti():
            for i in self.get_num_children():
                yield self[i]
        else:
            raise TypeError("%s is not a multi-attribute" % self)

    def __getitem(self, item):
        return self._api_class_instance.elementByLogicalIndex[item]

    def __getattr__(self, item):
        """
        if item in rt.dcc.connections.list_attr(self):
            return self.__getattribute__('__class__')('%s.%s' % (self, item))
        else:
            return super(Attribute, self).__getattr__(item)
        """
        return super(Attribute, self).__getattr__(item)


DISPLAY_KWARGS = {cfg.ATTRIBUTE_TYPE: cfg.ENUM,
                  cfg.ENUM_NAME: cfg.DISPLAY_ENUM,
                  cfg.KEYABLE: True,
                  cfg.DEFAULT_VALUE: 0}

PM_1_KWARGS = {cfg.ATTRIBUTE_TYPE: cfg.FLOAT,
               cfg.KEYABLE: True,
               cfg.MIN_VALUE: -1,
               cfg.MAX_VALUE: 1,
               cfg.DEFAULT_VALUE: 0}

PM_10_KWARGS = {cfg.ATTRIBUTE_TYPE: cfg.FLOAT,
                cfg.KEYABLE: True,
                cfg.MIN_VALUE: -10,
                cfg.MAX_VALUE: 10,
                cfg.DEFAULT_VALUE: 0}

RANGE_10_KWARGS = {cfg.ATTRIBUTE_TYPE: cfg.FLOAT,
                   cfg.KEYABLE: True,
                   cfg.MIN_VALUE: 0,
                   cfg.MAX_VALUE: 10,
                   cfg.DEFAULT_VALUE: 0}

ZERO_TO_ONE_KWARGS = {cfg.ATTRIBUTE_TYPE: cfg.FLOAT,
                      cfg.MIN_VALUE: 0,
                      cfg.MAX_VALUE: 1,
                      cfg.DEFAULT_VALUE: 0,
                      cfg.KEYABLE: True}
