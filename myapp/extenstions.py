"""
Module for importing non-configured flask extensions
"""
from celery import Celery

celery = Celery('celery_example', include=['myapp.tasks'])
