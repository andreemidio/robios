FROM python:3.9-slim

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONFAULTHANDLER=1

# Create and switch to a new user
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser
RUN mkdir -p /home/appuser/static
RUN chmod -R 777 /home/appuser/static

ADD requirements.txt /home/appuser

RUN pip install -U pip \
#    && pip install gunicorn --user \
#    && pip install .\robios_api-1.0.0-py3-none-any.whl --user \
#    && pip install .\communication-2.1.1-py3-none-any.whl --user\
#    && pip install .\messaging-2.5.0-py3-none-any.whl --user \

RUN pip install -r /home/appuser/requirements.txt



COPY . /home/appuser

EXPOSE 8000


