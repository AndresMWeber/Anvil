import config
import plugins
import log
import core
import templates
import runtime
import core.collections
import version

LOG = log.obtainLogger('anvil')
LOG.info('Successfully initiated Anvil %s.' % version.__version__)
