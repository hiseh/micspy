'''
sanic 日志
'''
import logging

log = logging.getLogger(__name__)

LOG_SETTINGS = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            # 'class': 'logging.handlers.RotatingFileHandler',
            # 'filename': './log/error.log',
            'level': 'DEBUG',
            'formatter': 'default',
            # 'encoding': 'utf-8'
        },
        'error': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'formatter': 'debug',
            'filename': './log/error.log',
            'maxBytes': 1024 * 1024 * 200,
            'backupCount': 5,
            'encoding': 'utf-8'
        },
    },
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s %(name)s:%(lineno)d | %(message)s',
        },
        'debug': {
            'format': '%(asctime)s - %(levelname)s - %(name)s:%(lineno)d | %(message)s',
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'error'],
            'propagate': True
        },
    }
}