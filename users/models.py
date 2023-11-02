from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models

from car.models import NULLABLE


class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Создает и сохраняет пользователя с указанным адресом электронной почты, датой
        рождения и паролем.
        """
        if not email:
            raise ValueError("У пользователей должен быть адрес электронной почты")

        user = self.model(email=self.normalize_email(email), date_of_birth=date_of_birth, )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        """
        Создает и сохраняет суперпользователя с указанным адресом электронной почты, датой
        рождения и паролем.
        """
        user = self.create_user(email, password=password, date_of_birth=date_of_birth, )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    objects = UserManager()

    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна')
    is_active = models.BooleanField(default=False, verbose_name='активный')

    date_of_birth = models.DateField(verbose_name='дата_рождения', **NULLABLE)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["date_of_birth"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Есть ли у пользователя определенное разрешение?"""
        return True

    def has_module_perms(self, app_label):
        """Есть ли у пользователя разрешения на просмотр приложения 'app_label'?"""
        return True

    @property
    def is_staff(self):
        """Является ли пользователь сотрудником?"""
        return self.is_admin


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
