from django.contrib import admin
from .models import MyTest, Question


# Регистрация модели MyTest в административной панели Django
@admin.register(MyTest)
class MyTestAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'material')  # Отображаемые поля в списке тестов
    list_filter = ('owner__email', 'material__title')  # Фильтрация по пользователю и названию материала


# Регистрация модели Question в административной панели Django
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'true_answer')  # Отображаемые поля в списке вопросов
    list_filter = ('mytest__owner__email', 'mytest__material__title')  # Фильтрация по владельцу теста и названию теста
