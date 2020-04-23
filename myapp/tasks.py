from myapp.extensions import celery


@celery.task(name="tasks.simple_task")
def simple_task(argument) -> str:
    hello = "Hello {} from task!".format(str(argument))
    print(hello)
    return hello
