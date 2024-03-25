from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'habits.settings')

app = Celery('habits', include=['habits.tasks'])

app.config_from_object('django.conf:settings', namespace='CELERY')

