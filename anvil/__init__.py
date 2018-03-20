from six import itervalues
import config
import utils
import colors
import meta_data
import log
import version
import plugins
import runtime
import objects
import grouping
import node_types
import sub_rig_templates
import rig_templates


class AnvilLog(log.LogMixin):
    LOG = log.obtain_logger(__name__)


LOG = AnvilLog
LOG.info('Auto-Loaded DCC %s', runtime.dcc)
LOG.info('Loaded logger config file %s successfully, writing to: %s',
         log.LogInitializer.CFG_FILE, log.LogInitializer.LOG_DIR)
LOG.info('Anvil environment has been set to %s', config.ENV)
LOG.info('Successfully initiated Anvil %s.', version.__version__)

EXISTING_ENCAPSULATIONS = {}


def check_for_encapsulation(dag_path):
    for node_encapsulation in itervalues(EXISTING_ENCAPSULATIONS):
        if dag_path == node_encapsulation._dcc_id:
            LOG.debug('Found previous encapsulation for %s: %r. Using instead.', dag_path, node_encapsulation)
            return node_encapsulation
    return None


def factory(dag_path, **kwargs):
    if dag_path is None:
        raise IOError('Tried to factory encapsulate None.')
    if is_anvil(dag_path):
        return dag_path

    existing = check_for_encapsulation(runtime.dcc.scene.get_persistent_id(str(dag_path)))
    if existing is not None:
        return existing

    node_type = runtime.dcc.scene.get_type(dag_path)

    if node_type in config.DCC_TYPES[config.TRANSFORM_TYPE]:
        encapsulation_class = objects.Transform

    elif node_type in config.DCC_TYPES[config.CURVE_TYPE]:
        encapsulation_class = objects.Curve

    elif node_type in config.DCC_TYPES[config.JOINT_TYPE]:
        encapsulation_class = objects.Joint

    else:
        encapsulation_class = objects.Transform

    encapsulation = encapsulation_class(dag_path, **kwargs)
    LOG.debug('Encapsulating %s with node type %s as %s', dag_path, encapsulation_class, encapsulation)
    register_encapsulation(encapsulation)
    return encapsulation


def factory_list(dag_nodes):
    return [factory(node) for node in dag_nodes]


def register_encapsulation(anvil_class_instance):
    EXISTING_ENCAPSULATIONS[len(EXISTING_ENCAPSULATIONS)] = anvil_class_instance


def is_anvil(node):
    try:
        if isinstance(node, node_types.REGISTERED_NODES.get(type(node).__name__)):
            return True
    except TypeError:
        pass
    return False


def is_aset(node):
    issubclass(type(node), node_types.BaseCollection)


def is_agrouping(node):
    return issubclass(type(node), node_types.AbstractGrouping)


def is_aobject(node):
    return issubclass(type(node), node_types.UnicodeDelegate)


__all__ = ['config',
           'meta_data',
           'plugins',
           'log',
           'version',
           'node_types',
           'runtime',
           'objects',
           'grouping',
           'sub_rig_templates',
           'rig_templates',
           'utils',
           'colors',
           'decorators.py']
