import logging
import sys
from importlib import import_module


class DCCPlugin(object):
    SUPPORTED = ['abstract', 'maya']
    ENGINE = None

    def __init__(self, dcc_module):
        dcc_module.lazy_import()
        self.scene = dcc_module.scene.Scene()
        self.create = dcc_module.create.Create()
        self.ENGINE = dcc_module.__name__


def get_log_handler():
    """Returns the appropriate logging handler for the DCC.
    Returns:
        class: Instance of the log handler or None if not found.
    """
    plugin = get_current_dcc()

    loaded_mod = __import__("anvil.plugins.{PLUGIN}.log_handler".format(PLUGIN=plugin), fromlist=['handler'])
    reload(loaded_mod)
    loaded_class = getattr(loaded_mod, 'DCCHandler')

    handler = loaded_class()

    if handler is None:
        class DCCHandler(logging.StreamHandler):
            """Generic DCC Handler instance"""

            def __init__(self, stream=None):
                super(DCCHandler, self).__init__(stream)

        handler = DCCHandler(sys.stdout)

    return handler


def get_current_dcc(return_module=False):
    handler = None

    for plugin in DCCPlugin.SUPPORTED:
        mod = import_module("anvil.plugins.{PLUGIN}".format(PLUGIN=plugin))
        reload(mod)
        if mod.is_dcc_loaded():
            handler = mod if return_module else plugin

    return handler


