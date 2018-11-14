from myapp.extenstions import celery


@celery.task(name="tasks.simple_task")
def simple_task(argument):
    hello = 'Hello {}'.format(str(argument))
    print(hello)
    return hello
