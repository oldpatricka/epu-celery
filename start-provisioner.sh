#use python uuid
export PYTHONPATH=.:$PYTHONPATH
export CELERY_HOST=`python -c 'import uuid; print uuid.uuid4()'`
celeryd  -l INFO --config=epu.celeryproc.provisionerconfig  --loader=epu.celeryproc.loader.TaskLoader -c 1 -n $CELERY_HOST -Q celery,$CELERY_HOST
