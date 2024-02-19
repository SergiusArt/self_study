from django.db import models
from config import settings
from src.constants import NULLABLE
from study.models import Material


class MyTest(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='my_tests',
                              verbose_name='Владелец')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='tests', verbose_name='Материал')
    title = models.CharField(max_length=255, verbose_name='Заголовок теста')
    score = models.IntegerField(default=0, verbose_name='Результат теста')

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.TextField(verbose_name='Текст вопроса и варианты ответа')
    true_answer = models.CharField(max_length=255, verbose_name='Правильный ответ')
    user_answer = models.CharField(max_length=255, blank=True, null=True, verbose_name='Ответ пользователя')

    def __str__(self):
        return self.text
