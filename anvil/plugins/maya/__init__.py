def is_dcc_loaded():
    try:
        import maya
        return True
    except ImportError:
        return False


import create
import scene
import connections
import dependencies
