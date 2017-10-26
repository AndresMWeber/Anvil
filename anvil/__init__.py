import log
import config
import version

setup_info = log.setup_logging(log.DEFAULT_LOG_DIR)

LOG = log.obtainLogger(__name__)
if setup_info:
    LOG.info('Loaded logger config file %s successfully, log files writing to directory:\n\t%s' % (setup_info[0],
                                                                                                   log.DEFAULT_LOG_DIR))

import plugins
import objects
import grouping

LOG.info('Populating node types...')

import node_types

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
