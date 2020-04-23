FROM python:3.7

MAINTAINER nikolay.v.golub@gmail.com

ENV PIP_NO_CACHE_DIR=on

COPY . /app
WORKDIR /app

RUN pipenv install --system --deploy

CMD ["pipenv", "run", "python",  "app.py"]
