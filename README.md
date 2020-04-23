# Minimal Celery Configuration With Flask Factories #

## If you have docker and docker-compose

1. Run `docker-compose up`
1. Open browser [127.0.0.1:5000](http://127.0.0.1:5000/). There new task can be sent and result checked

## If you want to run locally

Python 3.7 and [pipenv](https://pipenv.pypa.io/en/latest/) is required

1. Set up redis on localhost, can be used from Docker: ```bin/start_redis_docker.sh```. If another instance of redis is used, please configure `CELERY_BROKER_URL` and `CELERY_BACKEND` environment variables.
1. Install requirements: ```pipenv install```
1. Run application server: ```pipenv run python app.py```
1. Run celery worker in another terminal: ```pipenv run celery worker -A myapp.worker.celery```
1. Open browser [127.0.0.1:5000](http://127.0.0.1:5000/). There new task can be sent and result checked
