import api_proxy


def is_dcc_loaded():
    return True


def lazy_import():
    import connections
    import create
    import scene
    import dependencies
    return dependencies.API
