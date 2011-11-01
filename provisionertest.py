from celery.execute import send_task

result = send_task("provisioner", ("provision",))
print result.get()
