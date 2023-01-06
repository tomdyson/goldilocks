ARG PYTHON_VERSION=3.10-slim-buster

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt

RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    pip install gunicorn && \
    rm -rf /root/.cache/

COPY . /code/

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD set -xe; python manage.py migrate --noinput; gunicorn tomd.wsgi:application