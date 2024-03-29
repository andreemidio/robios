FROM python:3.9-slim

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
#ENV PYTHONDONTWRITEBYTECODE=1
#ENV PYTHONUNBUFFERED=1
#ENV PYTHONFAULTHANDLER=1

RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser
RUN mkdir -p /home/appuser/static
RUN chmod -R 777 /home/appuser/static

ADD requirements.txt /home/appuser
ADD robios_api-1.0.0-py3-none-any.whl /home/appuser
ADD communication-2.1.1-py3-none-any.whl /home/appuser
ADD messaging-2.5.0-py3-none-any.whl /home/appuser

RUN pip install -U pip \
    && pip install gunicorn \
    && pip install celery==4.2.1 \
    && pip install django-celery-beat==1.1.1 \
    && pip install flower \
    && pip install -r /home/appuser/requirements.txt \
    && pip install /home/appuser/robios_api-1.0.0-py3-none-any.whl \
    && pip install /home/appuser/communication-2.1.1-py3-none-any.whl \
    && pip install /home/appuser/messaging-2.5.0-py3-none-any.whl

COPY . /home/appuser

EXPOSE 8000




