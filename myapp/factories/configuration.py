import os


class Config:
    MODULE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    PROJECT_DIR = os.path.dirname(MODULE_DIR)
    DEBUG = False
    TESTING = False
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL',
                                       'redis://localhost:6379/0')
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_BACKEND',
                                           'redis://localhost:6379/1')
    CELERY_ACCEPT_CONTENT = ['json', 'yaml']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_IMPORTS = ('myapp.tasks',)
    CELERY_WORKER_HIJACK_ROOT_LOGGER = False
