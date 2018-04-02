from anvil.interfaces.maya.dependencies import DEFAULT_API
import anvil.interfaces.api_proxy as api_proxy


@api_proxy.APIProxy.validate({"type": ["object", "null"],
                              "properties": {
                                  "autoPriority": api_proxy.BOOL_TYPE,
                                  "connectEffector": api_proxy.BOOL_TYPE,
                                  "createCurve": api_proxy.BOOL_TYPE,
                                  "createRootAxis": api_proxy.BOOL_TYPE,
                                  "curve": api_proxy.STR_TYPE,
                                  "disableHandles": api_proxy.BOOL_TYPE,
                                  "enableHandles": api_proxy.BOOL_TYPE,
                                  "endEffector": api_proxy.STR_TYPE,
                                  "exists": api_proxy.STR_TYPE,
                                  "forceSolver": api_proxy.BOOL_TYPE,
                                  "freezeJoints": api_proxy.BOOL_TYPE,
                                  "jointList": api_proxy.BOOL_TYPE,
                                  "name": api_proxy.STR_TYPE,
                                  "numSpans": api_proxy.INT_TYPE,
                                  "parentCurve": api_proxy.BOOL_TYPE,
                                  "positionWeight": api_proxy.NUM_TYPE,
                                  "priority": api_proxy.INT_TYPE,
                                  "rootOnCurve": api_proxy.BOOL_TYPE,
                                  "rootTwistMode": api_proxy.BOOL_TYPE,
                                  "setupForRPsolver": api_proxy.BOOL_TYPE,
                                  "simplifyCurve": api_proxy.BOOL_TYPE,
                                  "snapCurve": api_proxy.BOOL_TYPE,
                                  "snapHandleFlagToggle": api_proxy.BOOL_TYPE,
                                  "solver": api_proxy.STR_TYPE,
                                  "startJoint": api_proxy.STR_TYPE,
                                  "sticky": api_proxy.STR_TYPE,
                                  "twistType": api_proxy.STR_TYPE,
                                  "weight": api_proxy.NUM_TYPE}},
                             DEFAULT_API, 'ikHandle')
def ik_handle(node, **kwargs):
    pass


@api_proxy.APIProxy.validate({"type": ["object", "null"],
                              "properties": {
                                  "destinationSkin": api_proxy.STR_TYPE,
                                  "influenceAssociation": api_proxy.STR_TYPE,
                                  "mirrorInverse": api_proxy.BOOL_TYPE,
                                  "mirrorMode": api_proxy.STR_TYPE,
                                  "noBlendWeight": api_proxy.BOOL_TYPE,
                                  "noMirror": api_proxy.BOOL_TYPE,
                                  "normalize": api_proxy.BOOL_TYPE,
                                  "sampleSpace": api_proxy.INT_TYPE,
                                  "smooth": api_proxy.BOOL_TYPE,
                                  "sourceSkin": api_proxy.STR_TYPE,
                                  "surfaceAssociation": api_proxy.STR_TYPE,
                                  "uvSpace": api_proxy.LINEAR_STRING_TYPE}},
                             DEFAULT_API, 'copySkinWeights')
def copy_skin_weights(source, destination, **kwargs):
    pass


@api_proxy.APIProxy.validate({"type": ["object", "null"],
                              "properties": {
                                  "addInfluence": api_proxy.STR_TYPE,
                                  "addToSelection": api_proxy.BOOL_TYPE,
                                  "after": api_proxy.BOOL_TYPE,
                                  "afterReference": api_proxy.BOOL_TYPE,
                                  "baseShape": api_proxy.STR_TYPE,
                                  "before": api_proxy.BOOL_TYPE,
                                  "bindMethod": api_proxy.INT_TYPE,
                                  "deformerTools": api_proxy.BOOL_TYPE,
                                  "dropoffRate": api_proxy.FLOAT_TYPE,
                                  "exclusive": api_proxy.STR_TYPE,
                                  "forceNormalizeWeights": api_proxy.BOOL_TYPE,
                                  "frontOfChain": api_proxy.BOOL_TYPE,
                                  "geometry": api_proxy.STR_TYPE,
                                  "geometryIndices": api_proxy.BOOL_TYPE,
                                  "heatmapFalloff": api_proxy.FLOAT_TYPE,
                                  "ignoreBindPose": api_proxy.BOOL_TYPE,
                                  "ignoreHierarchy": api_proxy.BOOL_TYPE,
                                  "ignoreSelected": api_proxy.BOOL_TYPE,
                                  "includeHiddenSelections": api_proxy.BOOL_TYPE,
                                  "influence": api_proxy.STR_TYPE,
                                  "lockWeights": api_proxy.BOOL_TYPE,
                                  "maximumInfluences": api_proxy.INT_TYPE,
                                  "moveJointsMode": api_proxy.BOOL_TYPE,
                                  "name": api_proxy.STR_TYPE,
                                  "normalizeWeights": api_proxy.INT_TYPE,
                                  "nurbsSamples": api_proxy.INT_TYPE,
                                  "obeyMaxInfluences": api_proxy.BOOL_TYPE,
                                  "parallel": api_proxy.BOOL_TYPE,
                                  "polySmoothness": api_proxy.FLOAT_TYPE,
                                  "prune": api_proxy.BOOL_TYPE,
                                  "recacheBindMatrices": api_proxy.BOOL_TYPE,
                                  "remove": api_proxy.BOOL_TYPE,
                                  "removeFromSelection": api_proxy.BOOL_TYPE,
                                  "removeInfluence": api_proxy.STR_TYPE,
                                  "removeUnusedInfluence": api_proxy.BOOL_TYPE,
                                  "selectInfluenceVerts": api_proxy.STR_TYPE,
                                  "skinMethod": api_proxy.INT_TYPE,
                                  "smoothWeights": api_proxy.FLOAT_TYPE,
                                  "smoothWeightsMaxIterations": api_proxy.INT_TYPE,
                                  "split": api_proxy.BOOL_TYPE,
                                  "toSelectedBones": api_proxy.BOOL_TYPE,
                                  "toSkeletonAndTransforms": api_proxy.BOOL_TYPE,
                                  "unbind": api_proxy.BOOL_TYPE,
                                  "unbindKeepHistory": api_proxy.BOOL_TYPE,
                                  "useGeometry": api_proxy.BOOL_TYPE,
                                  "volumeBind": api_proxy.FLOAT_TYPE,
                                  "volumeType": api_proxy.INT_TYPE,
                                  "weight": api_proxy.FLOAT_TYPE,
                                  "weightDistribution": api_proxy.INT_TYPE,
                                  "weightedInfluence": api_proxy.BOOL_TYPE}},
                             DEFAULT_API, 'skinCluster')
def skin_cluster(objects):
    pass


@api_proxy.APIProxy.validate({"type": ["object", "null"],
                              "properties": {'after': api_proxy.BOOL_TYPE, 'before': api_proxy.BOOL_TYPE,
                                             'bindState': api_proxy.BOOL_TYPE,
                                             'deformerTools': api_proxy.BOOL_TYPE,
                                             'envelope': api_proxy.FLOAT_TYPE,
                                             'exclusive': api_proxy.STR_TYPE,
                                             'frontOfChain': api_proxy.BOOL_TYPE,
                                             'geometry': api_proxy.STR_TYPE,
                                             'ignoreSelected': api_proxy.BOOL_TYPE,
                                             'name': api_proxy.STR_TYPE, 'parallel': api_proxy.BOOL_TYPE,
                                             'prune': api_proxy.BOOL_TYPE, 'relative': api_proxy.BOOL_TYPE,
                                             'remove': api_proxy.BOOL_TYPE,
                                             'resetGeometry': api_proxy.BOOL_TYPE,
                                             'split': api_proxy.BOOL_TYPE,
                                             'weightedNode': api_proxy.LINEAR_STRING_TYPE}},
                             DEFAULT_API, 'cluster')
def cluster(objects, **kwargs):
    pass