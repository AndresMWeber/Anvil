def is_dcc_loaded():
    try:
        import maya
        return True
    except ImportError:
        return False

def lazy_import():
    import create
    import scene
    import log_handler