BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_USER = "myuser"
BROKER_PASSWORD = "mypassword"
BROKER_VHOST = "myvhost"
CELERY_RESULT_BACKEND = "amqp"
CELERY_AMQP_TASK_RESULT_EXPIRES = 300
CELERY_IMPORTS = ("epu.celeryproc.provisioner", )
CELERY_TASKS_ON_LOAD = {
    "Start provisioner": {
        "task": "provisioner",
        "args": ("start",)
        }
    }
