import logging
import logging.config
import yaml
import os


def setup_logging(default_path='.log.yml', default_level=logging.INFO, env_key='LOG_CFG'):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value

    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)

    else:
        logging.basicConfig(level=default_level)


def obtainLogger(name):
    """Get's a logger and attaches the correct DCC compatible Handler.
    Args:
        name (str): Name of the logger to get / create.
    Returns:
        Logger: Logger.
    """
    logger = logging.getLogger(name)
    return logger

setup_logging()