import logging

from config.celery import app


@app.task
def add():
    z = 16 + 1
    print(z)


@app.task
def get_message_robios():
    logging.INFO('To começando meu bom')
