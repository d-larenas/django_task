from config import celery_app
from celery import shared_task


@celery_app.task(name='saludo')
def add():
    print("esta es una tarea")
    return "hola"
