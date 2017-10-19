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
DEFAULT_TAG_ATTR = 'metaforge'
BASE_DIR = os.path.dirname(os.path.abspath(anvil.__file__))
SHAPES_FILE = os.path.join(BASE_DIR, 'objects', 'curve_shapes.yml')
