from datetime import timedelta
from celery import Celery


def init_app(app: Celery):
    app.conf.beat_schedule = {
        "my-periodic-task": {
            "task": "scheduler.my_task",
            "schedule": timedelta(seconds=2),
            "args": ("arg1_value", "arg2_value"),
        },
    }
