from celery.loaders.default import Loader
from celery.execute import send_task
from os import environ
class TaskLoader(Loader):
    """Loader Module that runs a list of tasks on startup

    To provide a list of tasks, set the CELERY_TASKS_ON_LOAD config
    option with the same syntax as CELERYBEAT_SCHEDULE
    """

    def on_worker_init(self):
        Loader.on_worker_init(self)
        
        celery_host = environ.get('CELERY_HOST')
        tasks_to_run = self.conf.get('CELERY_TASKS_ON_LOAD')
        for task_name, task_attrs in tasks_to_run.items():
            send_task(task_attrs['task'], args=task_attrs.get('args'), queue=celery_host)
