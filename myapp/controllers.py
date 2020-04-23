from flask import Blueprint, render_template, Response, request
from myapp import tasks
from myapp.extensions import celery
home = Blueprint('home_views', __name__)


@home.route('/', methods=['GET', 'POST'])
def index() -> Response:
    task_id = None
    if request.method == 'POST':
        task_id = tasks.simple_task.delay(request.form.get('message'))
    return render_template('index.html', task_id=task_id)


@home.route('/result/<task_id>')
def task_result(task_id):
    result = celery.AsyncResult(task_id)
    return render_template('task_result.html', task_id=task_id, result=result)
