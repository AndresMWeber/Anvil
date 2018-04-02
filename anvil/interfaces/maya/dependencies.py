import maya.api.OpenMaya as om
import maya.cmds as mc
import atexit

# Initialize maya standalone if we are not in Maya
try:
    import maya.standalone as ms

    ms.initialize(name='anvil')
except TypeError:
    pass

import pymel.core as pm
import pymel.util as pmUtil
import pymel.core.datatypes as dt

APIs = {'pymel': pm,
        'openmaya': om,
        'cmds': mc,
        'standalone': ms}
DEFAULT_API = pm


@atexit.register
def exit_maya():
    import sys
    # If we are in standalone we need to make a new file and uninitialize then the virtual machines crash
    # if we do not use os._exit to properly exit Maya in CIRCLECI.
    # https://groups.google.com/forum/#!topic/python_inside_maya/chpuSyLbryI
    try:
        import maya.standalone as ms
        sys.stdout.write('Anvil is exiting Standalone Maya.')

        mc.file(new=True, force=True)
        sys.stdout.write('.')
        sys.stdout.flush()

        from pymel import versions
        if not str(versions.current()).startswith('2016'):
            ms.uninitialize()
            sys.stdout.write('.')
            sys.stdout.flush()
    except RuntimeError:
        pass

    finally:
        sys.stdout.write('Success...exiting.\n')
        sys.stdout.flush()
        import os
        if os.getenv('CIRCLECI'):
            os._exit(0)


__all__ = ['pmUtil', 'dt', 'om', 'mc', 'ms', 'DEFAULT_API', 'APIs', 'atexit']
