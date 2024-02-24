from django.apps import AppConfig


# Конфигурация приложения Users
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Использование BigAutoField по умолчанию
    name = 'users'  # Название приложения
    verbose_name = 'Пользователи'  # Читаемое название приложения, отображаемое в административной панели Django
