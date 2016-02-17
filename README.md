# Minimal Celery Configuration With Flask Factories #

1. Set up redis
1. Install requirements: ```pip install -r requirements.txt```
1. Run application server: ```python myapp.py```
1. Run celery worker: ```./run_worker.sh```
1. Make a request: ```curl http://127.0.0.1:5000/```