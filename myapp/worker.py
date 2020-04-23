from celery import Celery

from myapp.factories.application import create_application
from myapp.factories.celery import configure_celery

celery: Celery = configure_celery(create_application())
