from django.contrib.auth.models import AbstractUser
from django.db import models

from car.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна')
    is_active = models.BooleanField(default=False, verbose_name='активный')

    date_of_birth = models.DateField(verbose_name='дата_рождения', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Есть ли у пользователя определенное разрешение?"""
        return True


class EmailVerificationToken(models.Model):
    """
    Модель предназначена для хранения информации о токене верификации электронной почты пользователя.
    Она связана с конкретным пользователем через внешний ключ user,
    хранит сам токен token и дату его создания created_at.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='пользователь')

    token = models.CharField(max_length=255, unique=True, verbose_name='токен верификации')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания токена')

    def __str__(self):
        return f'{self.token} {self.created_at}'
