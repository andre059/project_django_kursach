import time

import schedule
from django.conf import settings
from django.core.mail import send_mail

from order.models import Order


def send_order_email(order_item: Order):
    # Формирование текста письма
    send_mail(
        'Заявка на покупку автомобиля',
        f'Здравствуйте, меня зовут: {order_item.name} \n'
        f'Мой адрес электронной почты: ({order_item.email}) \n'
        f'Хочу купить вашу машину: {order_item.car.name}. \n'
        f'Сообщение:{order_item.message} \n',
        settings.EMAIL_HOST_USER,
        [order_item.car.owner.email],
    )


def schedule_email(order):
    send_order_email(order)


def start_scheduling():
    while True:
        schedule.run_pending()
        time.sleep(1)
