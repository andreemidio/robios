FROM python:3.9-slim

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1

#RUN PIPENV_VENV_IN_PROJECT=1

ADD requirements.txt .
ADD robios .

RUN pip install -U pip \
    && pip install gunicorn \
    && pip install .\robios\robios_api-1.0.0-py3-none-any.whl \
    && pip install .\robios\communication-2.1.1-py3-none-any.whl\
    && pip install .\robios\messaging-2.5.0-py3-none-any.whl \
    && pip install -r .\requirements.txt

# Create and switch to a new user
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser
RUN mkdir -p /home/appuser/static
RUN chmod -R 777 /home/appuser/static
#COPY docker-entrypoint.sh ./home/appuser


COPY . .

EXPOSE 8000

#RUN ["chmod", "+x", "./docker-entrypoint.sh"]
#ENTRYPOINT ["./docker-entrypoint.sh"]



#CMD ["python3", "manage.py", "migrate"]

#ENTRYPOINT ["./docker-entrypoint.sh"]

#CMD ["gunicorn","--worker-class=gevent", "--workers=3","--worker-connections=1000" ,"config.wsgi:application", "--bind=0.0.0.0:8000","--log-level=DEBUG"]

