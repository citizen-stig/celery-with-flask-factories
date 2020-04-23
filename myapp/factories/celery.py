from celery import Celery
from celery.app.task import Task as CeleryTask
from flask import Flask

from myapp import extensions


def configure_celery(app: Flask) -> Celery:
    """Configures celery instance from app, using it's config"""
    TaskBase: CeleryTask = extensions.celery.Task

    class ContextTask(TaskBase):    # pylint: disable=too-few-public-methods
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    # https://docs.celeryproject.org/en/stable/userguide/configuration.html
    extensions.celery.conf.update(
        broker_url=app.config['CELERY_BROKER_URL'],
        result_backend=app.config['CELERY_RESULT_BACKEND'],
        accept_content=app.config['CELERY_ACCEPT_CONTENT'],
        task_serializer=app.config['CELERY_TASK_SERIALIZER'],
        result_serializer=app.config['CELERY_TASK_SERIALIZER'],
        worker_hijack_root_logger=False,
        beat_schedule=app.config.get('CELERYBEAT_SCHEDULE', {}),
        worker_redirect_stdouts_level='ERROR',
        task_always_eager=app.config.get('CELERY_ALWAYS_EAGER', False)
    )
    extensions.celery.Task = ContextTask
    return extensions.celery
