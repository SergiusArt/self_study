from django.db import models
from config import settings
from study.models import Material
from src.constants import NULLABLE


# Модель тестов
class MyTest(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='my_tests',
                              verbose_name='Владелец')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='tests', verbose_name='Материал')
    title = models.CharField(max_length=255, verbose_name='Заголовок теста')

    def __str__(self):
        return self.title  # Возвращает заголовок теста как строковое представление

    class Meta:
        verbose_name = 'Мой тест'  # Отображаемое имя модели в единственном числе
        verbose_name_plural = 'Мои тесты'  # Отображаемое имя модели во множественном числе


# Модель вопросов
class Question(models.Model):
    text = models.TextField(verbose_name='Текст вопроса и варианты ответа')
    true_answer = models.CharField(max_length=255, verbose_name='Правильный ответ')
    mytest = models.ForeignKey(MyTest, on_delete=models.CASCADE, related_name='questions', **NULLABLE,
                               verbose_name='Мой тест')

    @property
    def owner(self):
        return self.mytest.owner  # Возвращает владельца вопроса, который совпадает с владельцем теста

    def __str__(self):
        return self.text  # Возвращает текст вопроса как строковое представление

    class Meta:
        verbose_name = 'Вопрос'  # Отображаемое имя модели в единственном числе
        verbose_name_plural = 'Вопросы'  # Отображаемое имя модели во множественном числе
