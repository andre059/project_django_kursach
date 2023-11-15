from django.db import models
from django.utils import timezone

from car.models import NULLABLE
from config import settings


class Mailing(models.Model):
    """Рассылка."""

    PERIOD = (
        ('DAILY', 'Каждый день'),
        ('WEEKLY', 'Каждую неделю'),
        ('MONTHLY', 'Каждый месяц'),
    )

    time_start = models.TimeField(default=timezone.now, verbose_name='Время запуска рассылки')
    # если по каким-то причинам не успели разослать все сообщения, то
    # никакие сообщения клиентам после этого времени доставляться не должны
    time_end = models.TimeField(default=timezone.now, verbose_name='Время окончания рассылки')
    periodicity = models.CharField(max_length=50, verbose_name='Периодичность', choices=PERIOD)
    is_active = models.BooleanField(max_length=20, verbose_name='Пуск рассылки', default=False)

    client = models.ManyToManyField('Client', verbose_name='Кому')
    message = models.ForeignKey('Message', on_delete=models.CASCADE, verbose_name='Сообщение')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.time_start}-{self.time_end} {self.periodicity} {self.is_active} {self.client} {self.message}'

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"


class Message(models.Model):
    """Сообщение."""

    head = models.CharField(max_length=100, verbose_name='Тема')
    body = models.TextField(verbose_name='Сообщение')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.head} {self.body}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Client(models.Model):
    """Клиент"""

    name = models.CharField(max_length=50, verbose_name='имя', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='почта')
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.name}, {self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Logs(models.Model):
    """Лог"""

    STATUSES = (
        ('OK', 'Успешно'),
        ('FAILED', 'Ошибка'),
    )

    last_try = models.DateTimeField(verbose_name='Время последней попытки', auto_now_add=True)
    status_try = models.CharField(max_length=50, choices=STATUSES, verbose_name='Статус попытки', default='Успешно')
    answer = models.CharField(max_length=250, verbose_name='Ответ сервера', **NULLABLE)

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')
    client = models.EmailField(max_length=150, verbose_name='Email клиента', **NULLABLE)

    def __str__(self):
        return f'{self.last_try} {self.status_try} {self.mailing} {self.client}'

    class Meta:
        verbose_name = "Лог"
        verbose_name_plural = "Логи"
