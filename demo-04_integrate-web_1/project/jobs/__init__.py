"""__init__.py"""
import os
import logging
from celery import Celery

# Logging configuration
logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

backend = os.environ.get("CELERY_RESULT_BACKEND",
                         "db+postgresql://dbc:dbc@localhost:15432/schedule")
broker = os.environ.get("CELERY_BROKER_URL",
                        "redis://:redis123@localhost:16379/0")

celery_app = Celery("tasks", backend=backend, broker=broker)
celery_app.conf.update(
    timezone='America/Los_Angeles',
)
