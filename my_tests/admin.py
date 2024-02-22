from django.contrib import admin
from .models import MyTest, Question
from users.models import User


@admin.register(MyTest)
class MyTestAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'material')
    list_filter = ('owner__email', 'material__title') # Фильтрация по пользователю и названию материала


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'true_answer')
    list_filter = ('mytest__owner__email', 'mytest__material__title')  # Фильтрация по владельцу теста и названию теста
