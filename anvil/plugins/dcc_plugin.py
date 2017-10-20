import logging
import sys
from importlib import import_module


class DCCPlugin(object):
    SUPPORTED = ['standalone', 'maya']
    ENGINE = None

    def __init__(self, dcc_module):
        self.ENGINE_API = dcc_module.lazy_import() or {}
        self.scene = dcc_module.scene.Scene()
        self.create = dcc_module.create.Create()
        self.constrain = dcc_module.connections.Constraint()
        self.ENGINE = dcc_module.__name__

    def __str__(self):
        return '%s(%s, API=%s)' % (self.__class__.__name__, self.ENGINE, self.ENGINE_API)


def get_current_dcc(return_module=True):
    handler = None
    for plugin in DCCPlugin.SUPPORTED:
        handler = get_dcc(plugin, return_module=return_module) or handler
    return handler


def get_dcc(dcc_name_query, return_module=False):
    mod = import_module("anvil.plugins.{PLUGIN}".format(PLUGIN=dcc_name_query))
    reload(mod)
    if mod.is_dcc_loaded():
        return mod if return_module else dcc_name_query
