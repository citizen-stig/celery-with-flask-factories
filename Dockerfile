FROM python:3.7

MAINTAINER nikolay.v.golub@gmail.com

ENV PIP_NO_CACHE_DIR=on

COPY . /app
WORKDIR /app

RUN pip3 install pipenv && \
    pipenv install --system --deploy

CMD ["python", "app.py"]
