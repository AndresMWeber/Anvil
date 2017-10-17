import logging
import sys
from importlib import import_module


class DCCPlugin(object):
    SUPPORTED = ['abstract', 'maya']
    ENGINE = None

    def __init__(self, dcc_module):
        self.ENGINE_API = dcc_module.lazy_import() or {}
        self.scene = dcc_module.scene.Scene()
        self.create = dcc_module.create.Create()
        self.ENGINE = dcc_module.__name__

    def __str__(self):
        return '%s(%s, API=%s)' % (self.__class__.__name__, self.ENGINE, self.ENGINE_API)


def get_log_handler():
    """Returns the appropriate logging handler for the DCC.
    Returns:
        class: Instance of the log handler or None if not found.
    """
    plugin = get_current_dcc(return_module=False)
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


def get_current_dcc(return_module=True):
    handler = None
    for plugin in DCCPlugin.SUPPORTED:
        handler = get_dcc(plugin, return_module=return_module)
    return handler


def get_dcc(dcc_name_query, return_module=False):
    mod = import_module("anvil.plugins.{PLUGIN}".format(PLUGIN=dcc_name_query))
    reload(mod)
    if mod.is_dcc_loaded():
        return mod if return_module else dcc_name_query
