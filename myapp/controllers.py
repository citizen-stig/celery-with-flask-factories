from flask import Blueprint
from . import tasks
home = Blueprint('home_views', __name__)


@home.route('/')
def index():
    print('Executing task')
    task_id = tasks.simple_task.delay('FROM VIEW')
    print(task_id)
    return """
<!DOCTYPE html>
<html lang="en">
  <head><meta charset="utf-8">
    <title>Minimal Celery </title>
  </head>
  <body>'TASK {0} HAS BEEN RUN'</body>
</html>
""".format(task_id)


# @home.route('/result/<task_id>')
# def task_result(task_id):
#     result = celery.AsyncResult(task_id)
#     print(result.ready())
#     print(result.get())
#     return result
