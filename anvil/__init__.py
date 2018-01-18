from six import iteritems
import config
import colors
import meta_data
import log
import version


class AnvilLog(log.LogMixin):
    LOG = log.obtainLogger(__name__)


LOG = AnvilLog

import runtime
import plugins
import utils
import objects
import grouping
import node_types
import sub_rig_templates
import rig_templates

LOG.info('Anvil environment has been set to %s', config.ENV)
LOG.info('Successfully initiated Anvil %s.', version.__version__)

EXISTING_ENCAPSULATIONS = {}


def check_for_encapsulation(dag_path):
    for node_index, node_encapsulation in iteritems(EXISTING_ENCAPSULATIONS):
        if dag_path == node_encapsulation._dcc_id:
            LOG.debug('Found previous encapsulation for %s: %r. Using instead.', dag_path, node_encapsulation)
            return node_encapsulation
    else:
        return None


def factory(dag_path):
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

    encapsulation = encapsulation_class(dag_path)
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
    except:
        pass
    return False


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
           'node_types',
           'objects',
           'grouping',
           'sub_rig_templates',
           'rig_templates',
           'utils',
           'colors']
