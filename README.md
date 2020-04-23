# Minimal Celery Configuration With Flask Factories #

## If you have docker and docker-compose

1. Run `docker-compose up`


## If you want to run locally

1. Set up redis on localhost, can be used from Docker: ```bin/start_redis_docker.sh``` 
1. Install requirements: ```pipenv install```
1. Run application server: ```pipenv run python app.py```
1. Run celery worker in another terminal: ```pipenv run celery worker -A myapp.worker.celery```
1. Make a request: ```curl http://127.0.0.1:5000/```
