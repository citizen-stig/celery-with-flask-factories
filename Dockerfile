FROM python:3

MAINTAINER nikolay.v.golub@gmail.com

COPY . /app
WORKDIR /app

#RUN pip install pipenv
#
#RUN pipenv install --system --deploy

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python",  "app.py"]
