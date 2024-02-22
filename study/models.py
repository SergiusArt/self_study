from django.db import models
from config import settings
from src.constants import NULLABLE


class Section(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование раздела')
    description = models.TextField(**NULLABLE, verbose_name='Описание раздела')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sections',
                              verbose_name='Владелец')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Material(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование материала')
    description = models.TextField(**NULLABLE, verbose_name='Описание материалов')
    text = models.TextField(verbose_name='Содержание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='materials',
                              verbose_name='Владелец')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='materials', **NULLABLE,
                                verbose_name='Раздел')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
