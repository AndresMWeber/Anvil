import os
import anvil

# BASIC TYPES
MODEL_TYPE = 'model'
JOINT_TYPE = 'joint'
CURVE_TYPE = 'curve'
NURBS_TYPE = 'nurbs'
POLY_TYPE = 'poly'
TRANSFORM_TYPE = 'transform'

# COMPLEX TYPES
CONTROL_TYPE = 'control'
HIERARCHY_TYPE = 'hierarchy'
meta_data_TYPE = 'meta_data'

# DCC LIST
BASE = 'standalone'
MAYA = 'maya'
NUKE = 'nuke'
HOUDINI = 'houdini'

# BASIC VARS
DEFAULT_TAG_ATTR = 'anvil'
MODE = MAYA
TEST = 'test'
PROD = 'prod'
DEV = 'dev'
MODE_ENV_KEY = 'ANVIL_MODE'
LOG_ENV_KEY = 'ANVIL_LOG_CFG'

# PATHS
BASE_DIR = os.path.dirname(os.path.abspath(anvil.__file__))
SHAPES_FILE = os.path.join(BASE_DIR, 'objects', 'curve_shapes.yml')
DEFAULT_CONFIG_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), '.log.yml')
DEFAULT_LOG_DIR = os.path.join(os.path.expanduser('~'), 'anvil')

# ENV PATCHING
ENV = {MODE_ENV_KEY: DEV}
os.environ.update(ENV)

# DCC TYPE LOOKUP
DCC_TYPES = {
    TRANSFORM_TYPE: ['transform'],
    JOINT_TYPE: ['joint'],
    CURVE_TYPE: ['nurbsCurve'],
    NURBS_TYPE: ['nurbsSurface'],
    POLY_TYPE: ['mesh'],
}
