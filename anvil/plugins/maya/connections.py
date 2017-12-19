from anvil.plugins.maya.dependencies import *
import anvil.plugins.base.api_proxy as api_proxy
import anvil.config as cfg

default_properties = {
    "layer": api_proxy.STR_TYPE,
    "name": api_proxy.STR_TYPE,
    "remove": api_proxy.BOOL_TYPE,
    "targetList": api_proxy.BOOL_TYPE,
    "weight": api_proxy.NUM_TYPE,
    "weightAliasList": api_proxy.BOOL_TYPE,
}

cacheable_schema = {
    "createCache": api_proxy.LINEAR_ANGLE_TYPE,
    "deleteCache": api_proxy.BOOL_TYPE,
}

offset_schema = {
    "maintainOffset": {api_proxy.BOOL_TYPE, cfg.DEFAULT,
    "offset": api_proxy.POSITION_TYPE,
    "skip": api_proxy.STR_TYPE,
}

aim_schema = {
    "aimVector": api_proxy.POSITION_TYPE,
    "upVector": api_proxy.POSITION_TYPE,
    "worldUpObject": api_proxy.STR_TYPE,
    "worldUpType": api_proxy.STR_TYPE,
    "worldUpVector": api_proxy.POSITION_TYPE,
}


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA, {'properties': {'ignoreUnitConversion': api_proxy.BOOL_TYPE}}),
    API, 'mute')
def connected_attr(attribute_dag_path_1, attribute_dag_path_2, **kwargs):
    pass


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA,
                          {'properties':
                               {'disable': api_proxy.BOOL_TYPE,
                                'force': api_proxy.BOOL_TYPE}}),
    API, 'mute')
def mute(attribute_dag_path, **kwargs):
    pass


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA,
                          {'properties':
                               {'connection': api_proxy.BOOL_TYPE,
                                'datablock': api_proxy.BOOL_TYPE}}),
    API, 'isDirty')
def dirty_attr(attribute_dag_path, **kwargs):
    pass


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA,
                          {'properties':
                               {'destinationFromSource': api_proxy.BOOL_TYPE,
                                'getExactDestination': api_proxy.BOOL_TYPE, 'getExactSource': api_proxy.BOOL_TYPE,
                                'getLockedAncestor': api_proxy.BOOL_TYPE, 'isDestination': api_proxy.BOOL_TYPE,
                                'isExactDestination': api_proxy.BOOL_TYPE, 'isExactSource': api_proxy.BOOL_TYPE,
                                'isLocked': api_proxy.BOOL_TYPE, 'isSource': api_proxy.BOOL_TYPE,
                                'sourceFromDestination': api_proxy.BOOL_TYPE}}),
    API, 'connectionInfo')
def connection_info(attribute_dag_path, **kwargs):
    pass


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA,
                          {'properties':
                               {'allAttributes': api_proxy.BOOL_TYPE, 'bool': api_proxy.BOOL_TYPE,
                                'enumerated': api_proxy.BOOL_TYPE, 'hidden': api_proxy.BOOL_TYPE,
                                'internal': api_proxy.BOOL_TYPE, 'leaf': api_proxy.BOOL_TYPE,
                                'logicalAnd': api_proxy.BOOL_TYPE, 'multi': api_proxy.BOOL_TYPE,
                                'short': api_proxy.BOOL_TYPE, 'type': api_proxy.STR_TYPE,
                                'userInterface': api_proxy.BOOL_TYPE, 'writable': api_proxy.BOOL_TYPE}}),
    API, 'attributeInfo')
def info_attr(attribute_dag_path, **kwargs):
    pass


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA,
                          {'properties':
                               {'allFuture': api_proxy.BOOL_TYPE, 'allGraphs': api_proxy.BOOL_TYPE,
                                'breadthFirst': api_proxy.BOOL_TYPE, 'future': api_proxy.BOOL_TYPE,
                                'futureLocalAttr': api_proxy.BOOL_TYPE, 'futureWorldAttr': api_proxy.BOOL_TYPE,
                                'groupLevels': api_proxy.BOOL_TYPE, 'historyAttr': api_proxy.BOOL_TYPE,
                                'interestLevel': api_proxy.INT_TYPE, 'leaf': api_proxy.BOOL_TYPE,
                                'levels': api_proxy.INT_TYPE, 'pruneDagObjects': api_proxy.BOOL_TYPE}}),
    API, 'listHistory')
def list_history(dag_path, **kwargs):
    pass


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA,
                          {'properties': {'connections': api_proxy.BOOL_TYPE, 'destination': api_proxy.BOOL_TYPE,
                                          'exactType': api_proxy.BOOL_TYPE, 'plugs': api_proxy.BOOL_TYPE,
                                          'shapes': api_proxy.BOOL_TYPE, 'skipConversionNodes': api_proxy.BOOL_TYPE,
                                          'source': api_proxy.BOOL_TYPE, 'type': api_proxy.STR_TYPE}
                           }),
    API, 'listConnections')
def list_connections(attribute_dag_path, **kwargs):
    pass


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA,
                          {'properties': {
                              'remove': api_proxy.BOOL_TYPE,
                              'query': api_proxy.BOOL_TYPE}}),
    API, 'aliasAttr')
def alias_attr(attribute_dag_path, **kwargs):
    pass


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA,
                          {'properties': {
                              'affectsAppearance': api_proxy.BOOL_TYPE, 'affectsWorldspace': api_proxy.BOOL_TYPE,
                              'attributeType': api_proxy.BOOL_TYPE, 'cachedInternally': api_proxy.BOOL_TYPE,
                              'categories': api_proxy.BOOL_TYPE, 'channelBox': api_proxy.BOOL_TYPE,
                              'connectable': api_proxy.BOOL_TYPE, 'enum': api_proxy.BOOL_TYPE,
                              'exists': api_proxy.BOOL_TYPE, 'hidden': api_proxy.BOOL_TYPE,
                              'indeterminant': api_proxy.BOOL_TYPE, 'indexMatters': api_proxy.BOOL_TYPE,
                              'internal': api_proxy.BOOL_TYPE, 'internalGet': api_proxy.BOOL_TYPE,
                              'internalSet': api_proxy.BOOL_TYPE, 'keyable': api_proxy.BOOL_TYPE,
                              'listChildren': api_proxy.BOOL_TYPE, 'listDefault': api_proxy.BOOL_TYPE,
                              'listEnum': api_proxy.BOOL_TYPE, 'listParent': api_proxy.BOOL_TYPE,
                              'listSiblings': api_proxy.BOOL_TYPE, 'longName': api_proxy.BOOL_TYPE,
                              'maxExists': api_proxy.BOOL_TYPE, 'maximum': api_proxy.BOOL_TYPE,
                              'message': api_proxy.BOOL_TYPE, 'minExists': api_proxy.BOOL_TYPE,
                              'minimum': api_proxy.BOOL_TYPE, 'multi': api_proxy.BOOL_TYPE,
                              'niceName': api_proxy.BOOL_TYPE, 'node': api_proxy.STR_TYPE,
                              'numberOfChildren': api_proxy.BOOL_TYPE, 'range': api_proxy.BOOL_TYPE,
                              'rangeExists': api_proxy.BOOL_TYPE, 'readable': api_proxy.BOOL_TYPE,
                              'renderSource': api_proxy.BOOL_TYPE, 'shortName': api_proxy.BOOL_TYPE,
                              'softMax': api_proxy.BOOL_TYPE, 'softMaxExists': api_proxy.BOOL_TYPE,
                              'softMin': api_proxy.BOOL_TYPE, 'softMinExists': api_proxy.BOOL_TYPE,
                              'softRange': api_proxy.BOOL_TYPE, 'softRangeExists': api_proxy.BOOL_TYPE,
                              'storable': api_proxy.BOOL_TYPE, 'type': api_proxy.STR_TYPE,
                              'typeExact': api_proxy.STR_TYPE, 'usedAsColor': api_proxy.BOOL_TYPE,
                              'usedAsFilename': api_proxy.BOOL_TYPE, 'usesMultiBuilder': api_proxy.BOOL_TYPE,
                              'worldspace': api_proxy.BOOL_TYPE, 'writable': api_proxy.BOOL_TYPE}}),
    API, 'attributeQuery')
def query_attr(attribute, **kwargs):
    pass


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA,
                          {'properties': {
                              'caching': api_proxy.BOOL_TYPE,
                              'category': api_proxy.STR_TYPE,
                              'changedSinceFileOpen': api_proxy.BOOL_TYPE,
                              'channelBox': api_proxy.BOOL_TYPE,
                              'connectable': api_proxy.BOOL_TYPE,
                              'extension': api_proxy.BOOL_TYPE,
                              'fromPlugin': api_proxy.BOOL_TYPE,
                              'hasData': api_proxy.BOOL_TYPE,
                              'hasNullData': api_proxy.BOOL_TYPE,
                              'inUse': api_proxy.BOOL_TYPE,
                              'keyable': api_proxy.BOOL_TYPE,
                              'leaf': api_proxy.BOOL_TYPE,
                              'locked': api_proxy.BOOL_TYPE,
                              'multi': api_proxy.BOOL_TYPE,
                              'output': api_proxy.BOOL_TYPE,
                              'ramp': api_proxy.BOOL_TYPE,
                              'read': api_proxy.BOOL_TYPE,
                              'readOnly': api_proxy.BOOL_TYPE,
                              'scalar': api_proxy.BOOL_TYPE,
                              'scalarAndArray': api_proxy.BOOL_TYPE,
                              'settable': api_proxy.BOOL_TYPE,
                              'shortNames': api_proxy.BOOL_TYPE,
                              'string': api_proxy.STR_TYPE,
                              'unlocked': api_proxy.BOOL_TYPE,
                              'usedAsFilename': api_proxy.BOOL_TYPE,
                              'userDefined': api_proxy.BOOL_TYPE,
                              'visible': api_proxy.BOOL_TYPE,
                              'write': api_proxy.BOOL_TYPE}}),
    API, 'listAttr')
def list_attr(node, *args, **kwargs):
    pass


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA,
                          {'properties': {
                              'attribute': api_proxy.STR_TYPE,
                              'name': api_proxy.STR_TYPE}}),
    API, 'deleteAttr')
def delete_attr(attribute_dag_path_or_node, **kwargs):
    pass


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA,
                          {'properties': {
                              'asString': api_proxy.BOOL_TYPE,
                              'caching': api_proxy.BOOL_TYPE,
                              'channelBox': api_proxy.BOOL_TYPE,
                              'expandEnvironmentVariables': api_proxy.BOOL_TYPE,
                              'keyable': api_proxy.BOOL_TYPE,
                              'lock': api_proxy.BOOL_TYPE,
                              'multiIndices': api_proxy.BOOL_TYPE,
                              'settable': api_proxy.BOOL_TYPE,
                              'silent': api_proxy.BOOL_TYPE,
                              'size': api_proxy.BOOL_TYPE,
                              'time': api_proxy.NUM_TYPE,
                              'type': api_proxy.BOOL_TYPE}}),
    API, 'getAttr')
def get_attr(attribute_dag_path, *args, **kwargs):
    pass


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA,
                          {'properties': {
                              'alteredValue': api_proxy.BOOL_TYPE,
                              'caching': api_proxy.BOOL_TYPE,
                              'capacityHint': api_proxy.NUM_TYPE,
                              'channelBox': api_proxy.BOOL_TYPE,
                              'clamp': api_proxy.BOOL_TYPE,
                              'keyable': api_proxy.BOOL_TYPE,
                              'lock': api_proxy.BOOL_TYPE,
                              'size': api_proxy.NUM_TYPE,
                              'type': api_proxy.STR_TYPE}}),
    API, 'setAttr')
def set_attr(attribute, **kwargs):
    pass


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA,
                          {'properties': {
                              'attributeType': api_proxy.STR_TYPE, 'binaryTag': api_proxy.STR_TYPE,
                              'cachedInternally': api_proxy.BOOL_TYPE, 'category': api_proxy.STR_TYPE,
                              'dataType': api_proxy.STR_TYPE, 'defaultValue': api_proxy.NUM_TYPE,
                              'disconnectBehaviour': api_proxy.INT_TYPE, 'enumName': api_proxy.STR_TYPE,
                              'exists': api_proxy.BOOL_TYPE, 'fromPlugin': api_proxy.BOOL_TYPE,
                              'hasMaxValue': api_proxy.BOOL_TYPE, 'hasMinValue': api_proxy.BOOL_TYPE,
                              'hasSoftMaxValue': api_proxy.BOOL_TYPE, 'hasSoftMinValue': api_proxy.BOOL_TYPE,
                              'hidden': api_proxy.BOOL_TYPE, 'indexMatters': api_proxy.BOOL_TYPE,
                              'api_proxy.INT_TYPEernalSet': api_proxy.BOOL_TYPE, 'keyable': api_proxy.BOOL_TYPE,
                              'longName': api_proxy.STR_TYPE, 'maxValue': api_proxy.NUM_TYPE,
                              'minValue': api_proxy.NUM_TYPE, 'multi': api_proxy.BOOL_TYPE,
                              'niceName': api_proxy.STR_TYPE, 'numberOfChildren': api_proxy.INT_TYPE,
                              'parent': api_proxy.STR_TYPE, 'proxy': api_proxy.STR_TYPE,
                              'readable': api_proxy.BOOL_TYPE, 'shortName': api_proxy.STR_TYPE,
                              'softMaxValue': api_proxy.NUM_TYPE, 'softMinValue': api_proxy.NUM_TYPE,
                              'storable': api_proxy.BOOL_TYPE, 'usedAsColor': api_proxy.BOOL_TYPE,
                              'usedAsFilename': api_proxy.BOOL_TYPE, 'usedAsProxy': api_proxy.BOOL_TYPE,
                              'writable': api_proxy.BOOL_TYPE
                          }}),
    API, 'addAttr')
def add_attr(attribute, **kwargs):
    pass


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA,
                          {'properties': {
                              'force': api_proxy.BOOL_TYPE,
                              'lock': api_proxy.BOOL_TYPE,
                              'nextAvailable': api_proxy.STR_TYPE,
                              'referenceDest': api_proxy.STR_TYPE}}),
    API, 'connectAttr')
def connect_attr(source_attribute, destination_attribute, **kwargs):
    pass


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA, {'properties': {'nextAvailable': api_proxy.BOOL_TYPE}}),
    API, 'disconnectAttr')
def disconnect_attr(*attributes, **kwargs):
    pass


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA,
                          {'properties': api_proxy.merge_dicts(default_properties, offset_schema)}),
    API, 'pointConstraint')
def translate(source, targets, **flags):
    pass


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA,
                          {'properties': api_proxy.merge_dicts(default_properties, offset_schema, cacheable_schema)}),
    API, 'orientConstraint')
def rotate(source, targets, **flags):
    pass


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA,
                          {'properties': api_proxy.merge_dicts(default_properties, offset_schema, aim_schema)}),
    API, 'aimConstraint')
def aim(source, targets, **flags):
    pass


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA,
                          {'properties': api_proxy.merge_dicts(default_properties,
                                                               {"scaleCompensate": api_proxy.BOOL_TYPE,
                                                                "targetList": api_proxy.BOOL_TYPE},
                                                               offset_schema)}),
    API, 'scaleConstraint')
def scale(source, targets, **flags):
    pass


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA,
                          {'properties': api_proxy.merge_dicts(default_properties,
                                                               {"decompRotationToChild": api_proxy.BOOL_TYPE,
                                                                "skipRotate": api_proxy.STR_TYPE,
                                                                "skipTranslate": api_proxy.STR_TYPE,
                                                                },
                                                               offset_schema,
                                                               cacheable_schema)}),
    API, 'parentConstraint')
def parent(source, targets, **flags):
    pass


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA,
                          {'properties': api_proxy.merge_dicts(default_properties, aim_schema)}),
    API, 'tangentConstraint')
def tangent(source, targets, **flags):
    pass


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA, {'properties': api_proxy.merge_dicts(default_properties)}),
    API, 'geometryConstraint')
def geometry_point(source, targets, **flags):
    pass


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA,
                          {'properties': api_proxy.merge_dicts(default_properties, aim_schema)}),
    API, 'normalConstraint')
def geometry_normal(source, targets, **flags):
    pass


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA, {'properties': api_proxy.merge_dicts(default_properties)}),
    API, 'poleVectorConstraint')
def pole_vector(source, targets, **flags):
    pass
