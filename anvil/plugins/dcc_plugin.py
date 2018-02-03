from importlib import import_module


class DCCPlugin(object):
    SUPPORTED = ['standalone', 'maya']
    ENGINE = None

    def __init__(self, dcc_module):
        self.ENGINE = dcc_module.__name__
        self.APIs = dcc_module.dependencies.APIs or {}
        self.ENGINE_API = dcc_module.dependencies.DEFAULT_API

        self.scene = dcc_module.scene
        self.create = dcc_module.create
        self.connections = dcc_module.connections
        self.rigging = dcc_module.rigging
        self.animation = dcc_module.animation

    def copy_weights(self, source, targets):
        if not isinstance(targets, list):
            targets = [targets]

        for target in targets:
            self.rigging.copy_skin_weights(source, target, noMirror=True, surfaceAssociation='closestPoint',
                                           influenceAssociation='closestJoint')

    def __str__(self):
        return '%s(%s, API=%s)' % (self.__class__.__name__, self.ENGINE, self.ENGINE_API)


def get_current_dcc(return_module=True):
    handler = None
    for plugin in DCCPlugin.SUPPORTED:
        handler = get_dcc(plugin, return_module=return_module) or handler
    return handler


def get_dcc(dcc_name_query, return_module=False):
    mod = None
    try:
        mod = import_module("anvil.plugins.{PLUGIN}".format(PLUGIN=dcc_name_query))
    except ImportError:
        pass

    return mod if return_module else dcc_name_query
