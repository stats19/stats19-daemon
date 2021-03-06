import logging
import logging.config


def setup_logging_configuration(log_level: str, process_name: str) -> None:
    path = './logs'
    filename_path = f'{path}/stats19-server_{process_name}.log'

    config_logger = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '%(asctime)s | %(levelname)s | %(module)s | %(funcName)s | %(message)s'
            }
        },
        'handlers': {
            'log_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'level': log_level,
                'formatter': 'simple',
                'filename': filename_path,
                'maxBytes': 50000000,
                'backupCount': 1,
                'encoding': 'utf8'
            },
            'log_console': {
                'class': 'logging.StreamHandler',
                'level': log_level,
                'formatter': 'simple'
            }
        },
        'root': {
            'level': log_level,
            'handlers': ['log_file', 'log_console']
        }
    }

    logging.config.dictConfig(config_logger)
