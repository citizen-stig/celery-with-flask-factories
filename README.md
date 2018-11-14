# Minimal Celery Configuration With Flask Factories #

## If you have docker and docker-compose

1. Run `docker-compose up`


## If you want to run locally

1. Set up redis
1. Install requirements: ```pip install -r requirements.txt```
1. Run application server: ```python app.py```
1. Run celery worker: ```bin/start_worker.sh```
1. Make a request: ```curl http://127.0.0.1:5000/```
