import log
import config
import version

LOG = log.obtainLogger('anvil')
LOG.info('Successfully initiated Anvil %s.' % version.__version__)

import plugins
import runtime
import objects
import grouping
import node_types

__all__ = ['config', 'plugins', 'log', 'version', 'node_types', 'runtime', 'core', 'node_types', 'objects', 'grouping']
