from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JunDemo.settings')

app = Celery('project', CELERY_RESULT_BACKEND='amqp://')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task
def add(x, y):
    return x + y

@app.task
def div(x, y):
    return x / y
