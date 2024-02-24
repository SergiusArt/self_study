from django.apps import AppConfig


# Конфигурация приложения Study
class StudyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Используемое поле автоинкремента по умолчанию
    name = 'study'  # Название приложения
    verbose_name = 'Разделы с материалами'  # Читаемое название приложения, отображаемое в административной панели
