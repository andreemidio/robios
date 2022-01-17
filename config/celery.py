import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery("core")
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r} =================================')
app.conf.beat_schedule = {
    'robios-callback-message': {
        'task': 'apps.producao.tasks.get_message_robios',
        'schedule': crontab(minute="*/1"),
    }
}
app.conf.timezone = 'America/Sao_Paulo'
