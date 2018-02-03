from anvil.plugins.maya.dependencies import *
import anvil.plugins.base.api_proxy as api_proxy


@api_proxy.APIProxy._validate_function(
    api_proxy.merge_dicts(api_proxy.DEFAULT_SCHEMA,
                          {'properties':
                               {'animLayer': api_proxy.STR_TYPE, 'attribute': api_proxy.STR_TYPE,
                                'breakdown': api_proxy.BOOL_TYPE, 'clip': api_proxy.STR_TYPE,
                                'controlPoints': api_proxy.BOOL_TYPE, 'float': api_proxy.NUM_TYPE,
                                'hierarchy': api_proxy.STR_TYPE, 'identity': api_proxy.BOOL_TYPE,
                                'inTangentType': api_proxy.STR_TYPE, 'insert': api_proxy.BOOL_TYPE,
                                'insertBlend': api_proxy.BOOL_TYPE, 'minimizeRotation': api_proxy.BOOL_TYPE,
                                'outTangentType': api_proxy.STR_TYPE, 'shape': api_proxy.BOOL_TYPE,
                                'time': api_proxy.NUM_TYPE, 'value': api_proxy.NUM_TYPE}}),
    DEFAULT_API, 'setKeyframe')
def set_keyframe(*objects, **kwargs):
    pass
