from celery import Celery
from myapp.factories.celery import create_celery
from myapp.factories.application import create_application

celery: Celery = create_celery(create_application())
