from six import iteritems
import config
import log
import version

LOG = log.obtainLogger(__name__)

import runtime
import validation
import plugins
import objects
import grouping
import node_types

LOG.info('Anvil environment has been set to %s' % config.ENV)
LOG.info('Successfully initiated Anvil %s.' % version.__version__)

EXISTING_ENCAPSULATIONS = {}


def check_for_encapsulation(dag_path):
    for node_index, node_encapsulation in iteritems(EXISTING_ENCAPSULATIONS):
        if dag_path == node_encapsulation._dcc_id:
            return node_encapsulation
    else:
        return None


def factory(dag_path):
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
        encapsulation_class = objects.DagNode
    encapsulation = encapsulation_class(dag_path)
    EXISTING_ENCAPSULATIONS[len(EXISTING_ENCAPSULATIONS)] = encapsulation
    return encapsulation


__all__ = ['config',
           'validation',
           'plugins',
           'log',
           'version',
           'node_types',
           'runtime',
           'core',
           'node_types',
           'objects',
           'grouping',
           'dcc']
