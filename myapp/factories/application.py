from celery.app.task import Task as CeleryTask
from celery import Celery
from flask import Flask
from myapp.factories.configuration import Config
from myapp.controllers import home
from myapp import extensions    # Module import for prevent name clashes


def create_application() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(home)
    return app


def configure_celery(app: Flask) -> Celery:
    """Configures celery instance from app, using it's config"""
    TaskBase: CeleryTask = extensions.celery.Task

    class ContextTask(TaskBase):    # pylint: disable=too-few-public-methods
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    extensions.celery.conf.update(
        broker_url=app.config['CELERY_BROKER_URL'],
        accept_content=app.config['CELERY_ACCEPT_CONTENT'],
        task_serializer=app.config['CELERY_TASK_SERIALIZER'],
        result_serializer=app.config['CELERY_TASK_SERIALIZER'],
        worker_hijack_root_logger=False,
        beat_schedule=app.config.get('CELERYBEAT_SCHEDULE', {}),
        worker_redirect_stdouts_level='DEBUG',
        task_always_eager=app.config.get('CELERY_ALWAYS_EAGER', False)
    )
    extensions.celery.Task = ContextTask
    return extensions.celery
