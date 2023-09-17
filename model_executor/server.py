"""
Start the Gunicorn Server
"""

import os
import shlex
import subprocess

from model_executor.config.config import get_settings

here = os.path.dirname(os.path.realpath(__file__))
gunicorn_config_filepath = os.path.join(here, "config", "gunicorn_config.py")
settings = get_settings()


def _create_prometheus_dir():
    """
    Creates prometheus_dir
    :return:
    """
    # Gets prometheus metrics from
    prometheus_dir = settings.PROMETHEUS_MULTIPROC_DIR

    # Creates a dir if not found
    if not os.path.exists(prometheus_dir):
        os.makedirs(prometheus_dir)


def execute():
    """
    Exec gunicorn with our wsgi app
    :return:
    """

    _create_prometheus_dir()

    address = f"{settings.FASTAPI_HOST}:{settings.FASTAPI_PORT_MODEL_MANAGEMENT}"

    if settings.ENVIRONMENT == "local":
        workers = 1
    else:
        workers = 2

    cmd = (f"gunicorn -b {address} -c {gunicorn_config_filepath} --workers {workers} --worker-class "
           f"uvicorn.workers.UvicornWorker model_executor.app:app")

    subprocess.run(shlex.split(cmd))


if __name__ == "__main__":
    execute()
