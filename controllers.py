# -*- encoding: utf-8 -*-
from flask import Blueprint, current_app
from factories.celery import create_celery
home = Blueprint('home_views', __name__)


@home.route('/')
def index():
    celery = create_celery(current_app)
    res = celery.send_task('simple_task', args=('-=-= TEST FROM VIEW =-=-',))
    print(res)
    return """
<!DOCTYPE html>
<html lang="en">
  <head><meta charset="utf-8">
    <title>Minimal Celery </title>
  </head>
  <body>'TASK {0} HAS BEEN RUN'</body>
</html>
""".format(res)
