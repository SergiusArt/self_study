from users.permissions import IsOwnerPermission
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from .serializers import SectionSerializer, MaterialSerializer
from.models import Section, Material


class SectionList(generics.ListAPIView):
    """
    API для получения списка разделов.

    Разрешения:
    - Аутентифицированные пользователи могут видеть только свои разделы.

    Поля:
    - title: Наименование раздела;
    - description: Описание раздела;
    - owner: Владелец;

    Запросы:
    - GET: Получение списка разделов пользователя.
    """

    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]

    def get_queryset(self):
        return Section.objects.filter(owner=self.request.user)


class MaterialList(generics.ListAPIView):
    """
    API для получения списка материалов.

    Разрешения:
    - Аутентифицированные пользователи могут видеть только свои материалы.

    Поля:
    - title: Наименование материала;
    - description: Описание материалов;
    - text: Содержание;
    - owner: Владелец;
    - section: Раздел;

    Запросы:
    - GET: Получение списка материалов пользователя.
    """

    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]

    def get_queryset(self):
        return Material.objects.filter(owner=self.request.user)
