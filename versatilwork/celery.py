from __future__ import absolute_import, unicode_literals
import os, environ
from celery import Celery
import activity, notifications

env = environ.Env()
environ.Env.read_env()
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('C_FORCE_ROOT', 'true')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('backend', backend='rpc://', broker=env('broker'))

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Por alguna razón el autodiscover no está funcionando
#app.autodiscover_tasks()



# encender worker
# celery -A proj worker -l info

# encender celery beat
# celery -A charter beat -l info -S django

# Cerrar worker
# pkill -9 -f 'celery worker'


# sudo rabbitmqctl add_user myuser mypassword
# sudo rabbitmqctl add_vhost myvhost
# sudo rabbitmqctl set_user_tags myuser mytag
# sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"
