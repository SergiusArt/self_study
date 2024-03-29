"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth import views as auth_views

# Создание представления схемы API
schema_view = get_schema_view(
    openapi.Info(
        title="API для платформы самообучения",
        default_version='v1',
        description="Здесь можно протестировать API для платформы самообучения",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],  # Разрешение доступа для всех пользователей
)

# Определение маршрутов URL для приложения
urlpatterns = [
    # Путь к схеме Swagger в формате JSON или YAML
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # Путь к интерфейсу Swagger UI
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # Путь к интерфейсу Redoc
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # Путь к административной панели Django
    path('admin/', admin.site.urls),
    # Пути для приложений пользователей, обучения и тестов
    path('users/', include('users.urls', namespace='users')),
    path('study/', include('study.urls', namespace='study')),
    path('tests/', include('my_tests.urls', namespace='tests')),
    # Путь к странице входа в аккаунт
    path('accounts/login/', auth_views.LoginView.as_view()),
]
