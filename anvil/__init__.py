import config
import log
import version

LOG = log.obtainLogger(__name__)

import plugins
import objects
import grouping
import node_types

LOG.info('Anvil environment has been set to %s' % config.ENV)
LOG.info('Successfully initiated Anvil %s.' % version.__version__)

__all__ = ['config',
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
