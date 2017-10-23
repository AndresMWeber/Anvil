import logging
import logging.config
import yaml
import os
import pythonjsonlogger.jsonlogger as jslog

default_log = os.path.join(os.path.abspath(os.path.dirname(__file__)), '.log.yml')


def setup_logging(log_path=None, default_level=logging.INFO, env_key='LOG_CFG'):
    """Setup logging configuration

    """
    path = log_path or default_log
    value = os.getenv(env_key, None)
    if value:
        path = value

    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
        return path, config
    else:
        logging.basicConfig(level=default_level)
        return None

def obtainLogger(name, json_output=False):
    """Get's a logger and attaches the correct DCC compatible Handler.
    Args:
        name (str): Name of the logger to get / create.
    Returns:
        Logger: Logger.
    """
    logger = logging.getLogger(name)

    if json_output:
        format_str = '%(message)%(levelname)%(name)%(asctime)'
        formatter = jslog.JsonFormatter(format_str)
        for handler in logger.handlers:
            handler.setFormatter(formatter)

    return logger
