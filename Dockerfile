FROM python:3.9-slim

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1

#RUN PIPENV_VENV_IN_PROJECT=1

RUN apt-get update && apt-get upgrade -y \
 && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    musl-dev \
    libsm6 \
    libxext6 \
    libxrender-dev \
    dos2unix \
    libpq-dev \
    libmariadb-dev-compat \
    libmariadb-dev \
    libsm6 \
    libxext6 \
    ffmpeg \
    libfontconfig1 \
    libxrender1 \
    libgl1-mesa-glx \
    curl \
 && rm -rf /var/lib/apt/lists/*

ADD Pipfile .

RUN pip install -U pip \
 && pip install pipenv \
 && pipenv install gunicorn \
 && pipenv install --system --deploy --ignore-pipfile --skip-lock

# Create and switch to a new user
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser
RUN mkdir -p /home/appuser/static
RUN chmod 755 /home/appuser/static
#COPY docker-entrypoint.sh ./home/appuser


COPY . .

EXPOSE 8000

#RUN ["chmod", "+x", "./docker-entrypoint.sh"]
#ENTRYPOINT ["./docker-entrypoint.sh"]



#CMD ["python3", "manage.py", "migrate"]

#ENTRYPOINT ["./docker-entrypoint.sh"]

CMD ["gunicorn","--worker-class=gevent", "--workers=3","--worker-connections=1000" ,"config.wsgi:application", "--bind=0.0.0.0:8000","--log-level=DEBUG"]

