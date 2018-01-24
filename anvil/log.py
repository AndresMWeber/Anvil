import logging
import structlog
import logging.config
import yaml
import os
import datetime
import config as cfg



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


class LogMixin(object):
    LOG = obtainLogger(__name__ + '.LogMixin')

    @classmethod
    def info(cls, msg, *args):
        cls.LOG.info(msg % args)

    @classmethod
    def debug(cls, msg, *args):
        cls.LOG.debug(msg % args)

    @classmethod
    def warning(cls, msg, *args):
        cls.LOG.warning(msg % args)

    @classmethod
    def critical(cls, msg, *args):
        cls.LOG.critical(msg % args)

    @classmethod
    def error(cls, msg, *args):
        cls.LOG.error(msg % args)


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


class LogInitializer(LogMixin):
    HANDLERS = 'handlers'
    LOGGERS = 'loggers'
    LOG = obtainLogger(__name__)
    DEFAULT_LEVEL = logging.DEBUG
    LOG_DIR = cfg.DEFAULT_LOG_DIR
    ENV_KEY = cfg.LOG_ENV_KEY
    CFG_FILE = cfg.DEFAULT_CONFIG_PATH
    CFG_DICT = {}
    STATE = True

    def __init__(self, log_directory, cfg_file=None):
        self.LOG_DIR = log_directory
        self.CFG_FILE = cfg_file or self.CFG_FILE

    @classmethod
    def load_from_current_state(cls):
        cls.set_config_file_path()
        cls.set_config_from_path()
        cls.set_log_directory()
        cls.set_from_dict()
        cls.info('Loaded logger config file %s successfully, writing to: %s', cls.CFG_FILE, cls.CFG_DICT)
        return cls.CFG_FILE, cls.CFG_DICT

    @classmethod
    def get_env_dir(cls):
        return os.getenv(cls.ENV_KEY, None)

    @classmethod
    def set_log_directory(cls, log_directory=None):
        cls.LOG_DIR = cls.LOG_DIR if log_directory is None else log_directory
        if not os.path.exists(cls.LOG_DIR):
            os.makedirs(cls.LOG_DIR)
        cls._format_log_filenames()

    @classmethod
    def set_config_file_path(cls, file_path=None):
        cls.CFG_FILE = file_path or cls.CFG_FILE or cls.get_env_dir() or {}
        cls.info('Set config file path as %s', cls.CFG_FILE)

    @classmethod
    def set_config_from_path(cls, file_path=None):
        cls.CFG_DICT = cls._read_yml_file(file_path or cls.CFG_FILE)
        cls.info('Set config data as %s', cls.CFG_DICT)

    @classmethod
    def set_from_dict(cls, config_dict=None):
        cls.CFG_DICT = config_dict or cls.CFG_DICT
        if cls.CFG_DICT:
            logging.config.dictConfig(cls.CFG_DICT)
        else:
            logging.basicConfig(level=cls.DEFAULT_LEVEL)

    @classmethod
    def override_all_handlers(cls, key, value):
        for handler in cls.CFG_DICT[cls.HANDLERS]:
            cls._override_dict_config_settings(handler, key, value)

    @classmethod
    def override_all_loggers(cls, key, value):
        for logger in cls.CFG_DICT[cls.LOGGERS]:
            cls._override_dict_config_settings(logger, key, value)

    @classmethod
    def toggle_loggers(cls, key, value):
        for logger in cls.CFG_DICT[cls.LOGGERS]:
            cls._override_dict_config_settings(logger, key, value)

    @classmethod
    def _format_log_filenames(cls):
        for handler in cls.CFG_DICT[cls.HANDLERS]:
            filename = cls.CFG_DICT[cls.HANDLERS][handler].get('filename')
            if filename:
                base, extension = os.path.splitext(filename)
                today = datetime.datetime.today()
                filename = 'anvil_{NAME}{DATE_TIME}_{MODE}{EXT}'.format(NAME=base,
                                                                        MODE=os.getenv(cfg.MODE_ENV_KEY),
                                                                        DATE_TIME=today.strftime('_%Y%m%d_%H%M%S'),
                                                                        EXT=extension)
                cls._override_dict_config_settings(handler, 'filename', os.path.join(cls.LOG_DIR, filename))

    @classmethod
    def _override_dict_config_settings(cls, handler, key, value):
        handler_entry = cls.CFG_DICT[cls.HANDLERS].get(handler, None) or cls.CFG_DICT[cls.LOGGERS][handler]
        initial = handler_entry.get(key, None)
        if initial:
            handler_entry[key] = value
            cls.info('Handler %s.%s overwritten %s -> %s', handler_entry, key, initial, value)

    @classmethod
    def _read_yml_file(cls, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'rt') as f:
                cls.info('Loading log config file %s.', file_path)
                return yaml.safe_load(f.read())
        else:
            cls.info('Default log config file %s could not be found.', file_path)
        return {}


LogInitializer.load_from_current_state()


def toggle_loggers():
    LogInitializer.STATE = not LogInitializer.STATE
    LogInitializer.override_all_loggers('disabled', LogInitializer.STATE)
    LogInitializer.set_from_dict()

def set_all_log_levels(level=logging.ERROR):
    LogInitializer.override_all_loggers('level', level)
    LogInitializer.set_from_dict()
