from logging.config import dictConfig

from commons.logging import logging_config


def on_starting(server):
    dictConfig(logging_config)


def when_ready(server):
    pass


def child_exit(server, worker):
    pass


timeout = 330
