import os
import anvil
import colors

# BASIC TYPES
MODEL_TYPE = 'model'
JOINT_TYPE = 'joint'
CURVE_TYPE = 'curve'
NURBS_TYPE = 'nurbs'
NODE_TYPE = 'node'
SURFACE_TYPE = 'surface'
POLY_TYPE = 'poly'
GROUP_TYPE = 'group'
TRANSFORM_TYPE = 'transform'
ADD_SUB_TYPE = 'plusMinusAverage'

# NAME METADATA
LEFT = 'left'
RIGHT = 'right'
CENTER = 'center'
CHARACTER = 'character'
NAME = 'name'
SIDE = 'side'
VARIATION = 'var'
CHILD_TYPE = 'childtype'
UPPER = 'upper'
LOWER = 'lower'

# NAME FORMATS
RIG_FORMAT = 'character_rig_side_location_nameDecoratorVar_childtype_purpose_type'
DISPLAY_ENUM = 'off:on:template:reference'

# COMPLEX TYPES
RIG_TYPE = 'rig'
SUB_RIG_TYPE = 'sub_rig'
CONTROL_TYPE = 'control'
HIERARCHY_TYPE = 'hierarchy'

# RIG CONCEPTS
SUB_RIG_TOKEN = 'sub'
NAME_TOKENS = 'name_tokens'
META_DATA= 'meta_data'
UNIVERSAL = 'universal'
TOP_GROUP = 'group_top'
UNIVERSAL_CONTROL = '%s_%s' % (CONTROL_TYPE, UNIVERSAL)
ARM = 'arm'
LEG = 'leg'
HAND = 'hand'
FOOT = 'foot'
SPINE = 'spine'
NECK = 'neck'
HEAD = 'head'
DIGITS = 'digits'
FINGER = 'finger'
LAYOUT = 'layout_joints'
LOD = 'lod'
DEFAULT = 'default'
REFERENCE_OBJECT = 'reference_object'
OFFSET_GROUP = 'offset_group'
CONNECTION_GROUP = 'connection_group'
QUERY = 'query'


# DATA TYPES
ATTRIBUTE_TYPE = 'attributeType'
DEFAULT_VALUE = 'defaultValue'
FLOAT = 'double'
INTEGER = 'integer'
NUMBER = 'number'
STRING = 'string'
BOOLEAN = 'boolean'
ENUM = 'enum'
INT = 'int'
ARRAY = 'array'
POINT = 'point'
DEGREE = 'degree'
RADIAN = 'radian'

# ATTRIBUTES
ATTR_DELIMITER = '.'
MINIMUM = 'minimum'
MIN = 'min'
MIN_VALUE = 'minValue'
MAX = 'max'
MAXIMUM = 'maximum'
MAX_VALUE = 'maxValue'
KEYABLE = 'keyable'
ENUM_NAME = 'enumName'
OVERRIDE_ENABLED = 'overrideEnabled'
OVERRIDE_RGB = 'overrideRGBColors'
OVERRIDE_COLOR_INDEX = 'overrideColorRGB'
OVERRIDE_COLOR_RGB = 'overrideColorRGB'

# 3D CONCEPTS
PARENT = 'parent'
IK = 'ik'
IK_RP_SOLVER = 'ikRPsolver'
IK_SC_SOLVER = 'ikSCsolver'
IK_HANDLE = 'ik_handle'
IK_EFFECTOR = 'ik_effector'
FK = 'fk'
IKFK_BLEND = 'ikfk_blend'
BLENDER = 'blendColors'
POLE_VECTOR = 'pole_vector'
BLEND = 'blend'
WORLD_SPACE = 'worldSpace'
WORLD_SPACE_DISTANCE = 'worldSpaceDistance'
OBJECT_SPACE = 'objectSpace'

# 3D SPACE
TRANSLATE = 'translate'
TRANSLATION = 'translation'
TRANSFORM = 'transform'
ROTATE = 'rotate'
ROTATION = 'rotation'
SCALE = 'scale'
X = 'x'
Y = 'y'
Z = 'Z'
AXES = [X, Y, Z]
TRANSFORMATION = [TRANSLATE, ROTATE, SCALE]
PIVOTS = 'pivots'
ABSOLUTE = 'absolute'
RELATIVE = 'relative'
WORLD = 'world'
LOCAL = 'local'
AIM = 'aim'

# SHAPES
CUBE = 'cube'
SHAPE = 'shape'
SPHERE = 'sphere'
TRIANGLE = 'triangle'
PYRAMID_PIN = 'pyramid_pin'
CIRCLE = 'circle'
PENTAGON_CROSS = 'pentagon_cross'

# NAMING TOKENS
TYPE = 'type'
PURPOSE = 'purpose'

# DCC LIST
BASE = 'standalone'
MAYA = 'maya'
NUKE = 'nuke'
HOUDINI = 'houdini'

# ANVIL VARS
DEFAULT_TAG_ATTR = 'anvil'
MODE = MAYA
TEST = 'test'
PROD = 'prod'
DEV = 'dev'
MODE_ENV_KEY = 'ANVIL_MODE'
LOG_ENV_KEY = 'ANVIL_LOG_CFG'
DEFAULT_UNIVERSAL_SHAPE = DEFAULT_TAG_ATTR
DEFAULT_IK_SHAPE = SPHERE
DEFAULT_FK_SHAPE = CUBE
DEFAULT_DIGIT_FK_SHAPE = PYRAMID_PIN
DEFAULT_PV_SHAPE = TRIANGLE

# PATHS
BASE_DIR = os.path.dirname(os.path.abspath(anvil.__file__))
SHAPES_FILE = os.path.join(BASE_DIR, 'objects', 'curve_shapes.yml')
DEFAULT_CONFIG_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), '.log.yml')
DEFAULT_LOG_DIR = os.path.join(os.path.expanduser('~'), '.anvil')

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

RIG_COLORS = {
    CENTER: colors.YELLOW,
    LEFT: colors.RED,
    RIGHT: colors.BLUE,
    DEFAULT: colors.DARKSALMON,
}
