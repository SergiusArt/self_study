from rest_framework import permissions


# Пользовательское разрешение для проверки владельца объекта
class IsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user  # Проверяет, является ли пользователь владельцем объекта
