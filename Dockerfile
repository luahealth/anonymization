FROM python:3.9

ADD . /app


WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT gunicorn api.main:app --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
