from django.apps import AppConfig


# Конфигурация приложения MyTests
class MyTestsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Использование BigAutoField по умолчанию
    name = 'my_tests'  # Название приложения
    verbose_name = 'Мои тесты'  # Читаемое название приложения, отображаемое в административной панели Django
