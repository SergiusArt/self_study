from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Регистрация модели пользователей (User) в административной панели Django
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'is_active', 'is_authenticated')  # Отображаемые поля в списке пользователей

    # Определение метода для отображения статуса аутентификации пользователя
    def is_authenticated(self, obj):
        return obj.is_authenticated
    is_authenticated.boolean = True  # Указание, что поле является булевым значением
    is_authenticated.short_description = 'Authenticated'  # Название поля в административной панели
    ordering = ('email',)  # Сортировка пользователей по электронной почте

    # Настройка полей для отображения и редактирования в административной панели
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone', 'avatar', 'country', 'verification_code',
                                      'is_verified')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # Настройка полей при добавлении нового пользователя в административной панели
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
