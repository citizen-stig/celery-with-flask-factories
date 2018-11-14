import os
from myapp.factories.application import create_application
from myapp.factories.celery import create_celery


def run():
    app = create_application()
    create_celery(app)
    flask_host = os.environ.get('FLASK_HOST', '127.0.0.1')
    app.run(host=flask_host, debug=True)


if __name__ == '__main__':
    run()
