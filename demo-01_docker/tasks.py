"""tasks.py"""
# pylint: disable=C0103
import os
import time
from celery import Celery

broker_url  = os.environ.get("CELERY_BROKER_URL",
                             "redis://localhost:6378/0")
res_backend = os.environ.get("CELERY_RESULT_BACKEND",
                             "db+postgresql://dbc:dbc@localhost:5434/celery")

celery_app = Celery(name           = 'tasks',
                    broker         = broker_url,
                    result_backend = res_backend)

@celery_app.task
def add(x, y):
    '''
    mimic time consuming task:
        return sum of the two integers after sleeping for 5 seconds
    '''
    for i in range(5):
        time.sleep(1)
        print(i)
    return x+y
