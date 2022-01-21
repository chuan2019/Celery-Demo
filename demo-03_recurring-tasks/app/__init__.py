import os
import yaml
from celery import Celery

base_dir = os.path.dirname(os.path.realpath(__file__))
config_file = os.path.join(base_dir, 'config.yml')

with open(config_file, 'r') as fp:
    try:
        config = yaml.safe_load(fp)
    except yaml.YAMLError as err:
        raise yaml.YAMLError(str(err))

broker = os.environ.get('CELERY_BROKER_URL', config.get('demo_broker'))
backend = os.environ.get('CELERY_RESULT_BACKEND', config.get('demo_backend'))
API_KEY = config.get('api_key')

def make_celery(app=None):
    if app is None:
        celery = Celery(__name__, backend=backend, broker=broker)
    else:
        celery = Celery(
            app.import_name,
            broker=app.config['CELERY_BROKER_URL'],
            backend=app.config['CELERY_RESULT_BACKEND']
        )
        celery.conf.update(app.config)
        TaskBase = celery.Task

        class ContextTask(TaskBase):
            abstract = True

            def __call__(self, *args, **kwargs):
                with app.app_context():
                    return TaskBase.__call__(self, *args, **kwargs)

        celery.Task = ContextTask

    return celery
