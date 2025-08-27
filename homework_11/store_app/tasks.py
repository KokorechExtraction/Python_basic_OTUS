from celery import shared_task
from django.core.mail import send_mail
from .models import Product


@shared_task
def logging_new_product(recipient_email):
    return f"Товар добавлен {recipient_email}"
