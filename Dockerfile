FROM python:3.9-slim

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1

#RUN PIPENV_VENV_IN_PROJECT=1


RUN pip install -U pip --user \
    && pip install gunicorn --user \
    && pip install .\robios_api-1.0.0-py3-none-any.whl --user \
    && pip install .\communication-2.1.1-py3-none-any.whl --user\
    && pip install .\messaging-2.5.0-py3-none-any.whl --user \

RUN pip install -r .\requirements.txt --user

# Create and switch to a new user
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser
RUN mkdir -p /home/appuser/static
RUN chmod -R 777 /home/appuser/static


COPY . .

EXPOSE 8000


