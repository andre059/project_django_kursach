from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Owner(models.Model):
    name = models.CharField(max_length=150, verbose_name='имя')
    email = models.EmailField(verbose_name='почта', unique=True)

    def __str__(self):
        return f'{self.email} ({self.name})'

    class Meta:
        verbose_name = 'владелец'
        verbose_name_plural = 'владельцы'


class Car(models.Model):

    name = models.CharField(max_length=50, verbose_name='модель')
    year = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='год выпуска')

    price = models.IntegerField(**NULLABLE, verbose_name='цена')

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose_name='владелец')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'машина'
        verbose_name_plural = 'машины'


class CarHistory(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='машина')
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, verbose_name='владелец', **NULLABLE)

    start_year = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='владел с')
    stop_year = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='владел по')

    def __str__(self):
        return f'{self.car} {self.start_year}-{self.stop_year}'

    class Meta:
        verbose_name = 'история'
        verbose_name_plural = 'истории'

