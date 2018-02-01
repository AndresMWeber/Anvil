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

import atexit

@atexit.register
def exit_maya():
    # If we are in standalone we need to make a new file and uninitialize then os._exit to properly exit Maya.
    # https://groups.google.com/forum/#!topic/python_inside_maya/chpuSyLbryI
    try:
        import maya.standalone as ms
        import os
        import sys
        sys.stdout.write('Anvil is exiting Standalone Maya.')
        sys.stdout.write('.')
        mc.file(new=True, force=True)
        sys.stdout.write('.')
        ms.uninitialize()
        sys.stdout.write('.')
        os._exit(0)
        sys.stdout.write('Success')

    except:
        pass