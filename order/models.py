from django.db import models


class Order(models.Model):
    car = models.ForeignKey('car.Car', on_delete=models.CASCADE, verbose_name='машина')

    name = models.CharField(max_length=150, verbose_name='имя')
    email = models.EmailField(max_length=150, verbose_name='почта')
    message = models.TextField()

    closed = models.BooleanField(default=False, verbose_name='закказ закрыт')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.car} от {self.email}'

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
