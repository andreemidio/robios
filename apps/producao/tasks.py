from config.celery import app


@app.task
def add():
    z = 16 + 1
    print(z)
