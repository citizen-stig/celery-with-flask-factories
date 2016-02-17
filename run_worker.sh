#!/usr/bin/env bash
celery worker -A celery_worker.celery --loglevel=DEBUG