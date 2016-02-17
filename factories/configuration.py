# -*- encoding: utf-8 -*-


def get_config():
    class Config:
        CELERY_BROKER_URL = 'redis://localhost:6379/0'
        CELERY_ACCEPT_CONTENT = ['json', 'yaml']
        CELERY_TASK_SERIALIZER = 'json'
        CELERY_RESULT_SERIALIZER = 'json'
        CELERY_IMPORTS = ('tasks',)
    return Config

