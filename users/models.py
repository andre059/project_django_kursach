from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from car.models import NULLABLE


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    objects = UserManager()

    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна')
    is_active = models.BooleanField(default=False, verbose_name='активный')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


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
