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


class Comments(models.Model):
    """Коментарии"""

    email = models.EmailField()
    name = models.CharField(max_length=50, verbose_name='имя')
    text_comments = models.TextField(max_length=2000, verbose_name='текст коментария')

    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='публикация')

    def __str__(self):
        return f'{self.name}, {self.post}, {self.text_comments}'

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'


class Likes(models.Model):
    """Лайки"""

    ip = models.CharField(max_length=100, verbose_name='IP-адрес')
    pos = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='публикация')