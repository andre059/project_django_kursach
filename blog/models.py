from django.db import models

from car.models import NULLABLE


class Post(models.Model):
    """Данные о посте"""

    heading = models.CharField(max_length=150, verbose_name='Заголовок')
    blog_body = models.TextField(verbose_name='записи блога')
    author = models.CharField(max_length=100, verbose_name='имя автора')
    date_publication = models.DateTimeField(verbose_name='дата и время публикации')
    images = models.ImageField(upload_to='blogImj/', verbose_name='изображения', **NULLABLE)

    def __str__(self):
        return f'{self.heading}, {self.author}'

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
