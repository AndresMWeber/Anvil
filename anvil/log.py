import logging
import structlog
import logging.config
import yaml
import os
import datetime
import config


def setup_logging(log_path=config.DEFAULT_CONFIG_PATH,
                  default_level=logging.INFO,
                  env_key=config.LOG_ENV_KEY,
                  log_directory=''):
    """Setup logging configuration

    """
    env_path = os.getenv(env_key, None)

    config_dict = read_yml_file(env_path if env_path else log_path)
    if config_dict:
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

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
            base, extension = os.path.splitext(filename)
            today = datetime.datetime.today()
            filename = 'anvil_{NAME}{DATE_TIME}_{MODE}{EXT}'.format(NAME=base,
                                                                    MODE=os.getenv(config.MODE_ENV_KEY),
                                                                    DATE_TIME=today.strftime('_%Y%m%d_%H%M%S'),
                                                                    EXT=extension)
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
    logger = structlog.get_logger(name)

    if json_output:
        format_str = '%(message)%(levelname)%(name)%(asctime)'
        # formatter = jslog.JsonFormatter(format_str)
        # for handler in logger.handlers:
        #    handler.setFormatter(formatter)
        pass

    return logger


LOG = obtainLogger(__name__)
setup_info = setup_logging(log_directory=config.DEFAULT_LOG_DIR)

if setup_info:
    LOG.info('Loaded logger config file %s successfully, writing to: %s' % (setup_info[0], config.DEFAULT_LOG_DIR))

structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer(),
        # structlog.processors.KeyValueRenderer(
        #    key_order=["event", "logger", "level", "timestamp"],
        # ),
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)
