from django.contrib import admin
from .models import Section, Material


# Регистрация модели Section в административной панели Django
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'owner')  # Отображаемые поля в списке разделов
    list_filter = ('owner__email',)  # Фильтрация по владельцу раздела


# Регистрация модели Material в административной панели Django
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'text', 'owner')  # Отображаемые поля в списке материалов
    list_filter = ('owner__email',)  # Фильтрация по владельцу материала
