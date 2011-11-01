from celery.execute import send_task



op = "start"
args = {"op":op, "data":"datax"}
result = send_task("provisioner", kwargs=args)

print result
result.get()

