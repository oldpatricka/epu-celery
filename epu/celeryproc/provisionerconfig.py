from epu.celeryproc.celeryconfig import *
from epu.celeryproc.epuconfig import *

CELERY_IMPORTS = ("epu.celeryproc.provisioner", )
CELERY_TASKS_ON_LOAD = {
    "Start provisioner": {
        "task": "provisioner",
        "args": ("start",)
        }
    }
PROVISIONER_CONFIG = {
    "store": "store.class",
    "notifier": "notifier.class",
    "dtrs": "dtrs.class",
    "core": "core.class"
    }
