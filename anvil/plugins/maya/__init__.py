def is_dcc_loaded():
    try:
        import maya
        return True
    except ImportError:
        return False

def lazy_import():
    import create
    import scene
    import connections
    import log_handler
    import dependencies
    return dependencies.API