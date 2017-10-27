import os
import anvil

MODEL_TYPE = 'model'
JOINT_TYPE = 'joint'
CONTROL_TYPE = 'control'
HIERARCHY_TYPE = 'hierarchy'
meta_data_TYPE = 'meta_data'

BASE = 'standalone'
MAYA = 'maya'
NUKE = 'nuke'
HOUDINI = 'houdini'

MODE = MAYA
DEFAULT_TAG_ATTR = 'anvil'
BASE_DIR = os.path.dirname(os.path.abspath(anvil.__file__))
SHAPES_FILE = os.path.join(BASE_DIR, 'objects', 'curve_shapes.yml')

TEST = 'test'
PROD = 'prod'
DEV = 'dev'
MODE_ENV_KEY = 'ANVIL_MODE'
LOG_ENV_KEY = 'ANVIL_LOG_CFG'

DEFAULT_CONFIG_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), '.log.yml')
DEFAULT_LOG_DIR = os.path.join(os.path.expanduser('~'), 'anvil')

ENV = {MODE_ENV_KEY: DEV}

os.environ.update(ENV)
