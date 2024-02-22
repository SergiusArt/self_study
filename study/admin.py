from django.contrib import admin
from .models import Section, Material


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'owner')
    list_filter = ('owner__email',)  # Фильтрация по пользователю


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'text', 'owner')
    list_filter = ('owner__email',) # Фильтрация по пользователю
