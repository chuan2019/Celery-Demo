import os
from celery import Celery
import time

broker_url  = os.environ.get("CELERY_BROKER_URL",
                             "redis://localhost:6378/0"),
res_backend = os.environ.get("CELERY_RESULT_BACKEND",
                             "db+postgresql://dbc:dbc@localhost:5434/celery")

celery_app = Celery(name           = 'tasks',
                    broker         = broker_url,
                    result_backend = res_backend)

@celery_app.task
def add(x, y):
    for i in range(5):
        time.sleep(1)
        print(i)
    return x+y

