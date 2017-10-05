import logging
from anvil.plugins.dcc_plugin import get_log_handler


def getLogger(name):
    """Get's a logger and attaches the correct DCC compatible Handler.
    Args:
        name (str): Name of the logger to get / create.
    Returns:
        Logger: Logger.
    """

    logger = logging.getLogger(name)

    handlerNames = [type(x).__name__ for x in logger.handlers]

    if 'DCCHandler' not in handlerNames:
        dccHandler = get_log_handler()
        if dccHandler is not None:
            logger.addHandler(dccHandler)

    return logger
