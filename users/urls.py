from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.api import UserRegistrationView
from users.apps import UsersConfig


# Определение имени приложения
app_name = UsersConfig.name

# Определение маршрутов URL
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Получение токена
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Обновление токена
    path('register/', UserRegistrationView.as_view(), name='user-registration'),  # Регистрация пользователя
]
