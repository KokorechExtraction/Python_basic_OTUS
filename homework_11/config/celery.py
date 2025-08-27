import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
os.environ["FORKED_BY_MULTIPROCESSING"] = "1"

app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


app.conf.beat_scheduler = "django_celery_beat.schedulers.DatabaseScheduler"
