import json

DEFAULT_LOGGER_FORMAT = {
    "module": "%(module)s",
    "func_name": "%(funcName)s",
    "caller": "%(name)s",
    "line": "%(lineno)s",
    "level": "%(levelname)s",
    "msg": "%(message)s",
    "pid": "%(process)d",
    "thread_id": "%(thread)d",
}

logging_config = dict(
        version=1,
        disable_existing_loggers=False,
        root={
            "level": "INFO",
            "handlers": ["default"]
        },
        formatters={
            "default": {
                "format": json.dumps(DEFAULT_LOGGER_FORMAT),
                "class": "logging.Formatter"
            }
        },
        handlers={
            "default": {
                "class": "logging.StreamHandler",
                "formatter": "default",
                "stream": "ext://sys.stdout"
            }
        },
        loggers={
            "": {
                "level": "INFO",
                "handlers": ["default"],
                "propagate": False,
            },
            "gunicorn": {
                "level": "INFO",
                "handlers": ["default"],
                "propagate": False,
            },
            "uvicorn": {
                "level": "INFO",
                "handlers": ["default"],
                "propagate": False,
            },
            "fastapi": {
                "level": "INFO",
                "handlers": ["default"],
                "propagate": False,
            },
        },
)