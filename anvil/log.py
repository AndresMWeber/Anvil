import logging
import logging.config
import yaml
import os
import pythonjsonlogger.jsonlogger as jslog

DEFAULT_CONFIG_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), '.log.yml')
DEFAULT_ENV_KEY = 'ANVIL_LOG_CFG'
DEFAULT_LOG_DIR = os.path.join(os.path.expanduser('~'), 'anvil')


def setup_logging(log_path=DEFAULT_CONFIG_PATH, default_level=logging.INFO, env_key=DEFAULT_ENV_KEY, log_directory=''):
    """Setup logging configuration

    """
    env_path = os.getenv(env_key, None)

    config_dict = read_yml_file(env_path if env_path else log_path)
    if config_dict:
        prepend_log_filename(config_dict, log_directory)
        logging.config.dictConfig(config_dict)
        return log_path, config_dict
    else:
        logging.basicConfig(level=default_level)
        return None


def prepend_log_filename(config_dict, log_directory):
    for handler in config_dict['handlers']:
        filename = config_dict['handlers'][handler].get('filename', None)
        if filename:
            config_dict['handlers'][handler]['filename'] = os.path.join(log_directory, filename)
            LOG.info('Handler %s writing to %s' % (handler, config_dict['handlers'][handler]['filename']))

def read_yml_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'rt') as f:
            LOG.info('Loading log config file %s.' % (file_path))
            return yaml.safe_load(f.read())
    else:
        LOG.info('Default log config file %s could not be found.' % (file_path))
        return {}


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


LOG = obtainLogger(__file__)
