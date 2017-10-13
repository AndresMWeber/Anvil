import config
import plugins
import log
import core
import templates
import runtime
import core.collections
import version
import core.objects.node_types

node_types = core.objects.node_types

LOG = log.obtainLogger('anvil')
LOG.info('Successfully initiated Anvil %s.' % version.__version__)
