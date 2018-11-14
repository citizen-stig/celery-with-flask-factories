import os


def get_config():
    class Config:
        CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
        # CELERY_RESULT_BACKEND = os.environ.get('CELERY_BACKEND', 'redis://localhost:6379/1')
        # CELERY_RESULT_BACKEND = 'redis'
        CELERY_ACCEPT_CONTENT = ['json', 'yaml']
        CELERY_TASK_SERIALIZER = 'json'
        CELERY_RESULT_SERIALIZER = 'json'
        CELERY_IMPORTS = ('myapp.tasks',)
        CELERY_WORKER_HIJACK_ROOT_LOGGER = False
    return Config

