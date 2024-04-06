from src.services.email_service import EmailService
from celery import Celery  # type: ignore  # noqa
from celery.app.task import Task  # type: ignore  # noqa
from mailersend import emails  # type: ignore  # noqa
from config import settings as s  # type: ignore  # noqa


celery_app = Celery(__name__, broker=s.WORKER_BROKER)


celery_app.conf.update(
    accept_content=[
        'pickle',
        'application/json',
        'application/x-python-serialize'
    ],
    result_accept_content=[
        'pickle',
        'application/json',
        'application/x-python-serialize'
    ],
    task_create_missing_queues=True,
    celery_store_errors_even_if_ignored=True,
    task_store_errors_even_if_ignored=True,
    task_ignore_results=False,
    task_serializer='pickle',
    result_serializer='pickle',
    event_serializer='json',
    timezone='America/Sao_Paulo',
    enable_utc=False
)


@celery_app.task(
    bind=True,
    max_retry=5,
    default_delay_retry=20,
    retry_backoff=2
)
def send_email(self, context: dict):

    html = f"""
        html message: <b>Greetings</b><br /> from the {context['from']}
        text plain: you got this message through MailerSend.
    """

    result = EmailService.send_email(
        to="antoniofernandodj@outlook.com",
        to_name="Antonio",
        subject=f"{context['subject']}",
        html=html
    )

    return result
