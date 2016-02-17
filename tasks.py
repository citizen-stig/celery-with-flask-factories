# -*- encoding: utf-8 -*-
from factories.celery import create_celery
from factories.application import create_application
celery = create_celery(create_application())


@celery.task(name="tasks.simple_task")
def simple_task(argument):
    print(argument)
