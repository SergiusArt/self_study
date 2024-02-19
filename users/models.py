import uuid

from django.db import models
from src.constants import NULLABLE
from django.contrib.auth.models import AbstractUser


# Класс модели пользователей
class User(AbstractUser):
    # Удаляем поле "username", так как мы используем "email" в качестве уникального идентификатора пользователя
    username = None

    # Поле для хранения почты пользователя
    email = models.EmailField(unique=True, verbose_name='Почта')

    # Поле для хранения номера телефона пользователя
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)

    # Поле для хранения аватара пользователя
    avatar = models.ImageField(upload_to='users/avatars', verbose_name='Аватар', **NULLABLE)

    # Поле для хранения страны пользователя
    country = models.CharField(max_length=35, verbose_name='Страна', **NULLABLE)

    # Поле для хранения верификационного кода пользователя, который генерируется рандомно при создании пользователя
    verification_code = models.CharField(max_length=35, verbose_name='Код', **NULLABLE)

    # Поле для хранения значения верифицирован ли пользователь. По умолчанию - False
    is_verified = models.BooleanField(default=False, verbose_name='Верификация')

    # Указываем поле "email" как поле для входа в систему
    USERNAME_FIELD = "email"

    # Поля, которые должны быть заполнены при создании пользователя
    REQUIRED_FIELDS = []

    # Переопределяем метод save для автоматической генерации verification_code при создании пользователя
    def save(self, *args, **kwargs):
        # Генерируем уникальный код с помощью функции uuid4()
        self.verification_code = str(uuid.uuid4())[:8]
        super().save(*args, **kwargs)
