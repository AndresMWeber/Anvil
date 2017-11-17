import maya.api.OpenMaya as om
import maya.cmds as mc

# Initialize maya standalone if we are not in Maya
try:
    import maya.standalone as ms

    ms.initialize(name='anvil')
except TypeError:
    pass

import pymel.core as pm
import pymel.util as pmUtil
import pymel.core.datatypes as dt

API = pm
