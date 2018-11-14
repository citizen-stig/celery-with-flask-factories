from ..extenstions import celery


def config_to_celery_kwargs(config):
    return {
        k.replace('CELERY_', '').lower(): v
        for k, v in dict(config).items()
        if k.startswith('CELERY')
    }


def create_celery(app):
    """
    Configures celery instance from application, using it's config
    :param app: Flask application instance
    :return: Celery instance
    """

    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery_config = config_to_celery_kwargs(app.config)
    print('Celery config: ', celery_config)
    celery.conf.update(**celery_config)
    print('Celery broker: ' + str(celery.conf.get('broker_url')))
    celery.Task = ContextTask
    return celery
