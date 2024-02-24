from django.shortcuts import get_object_or_404

from users.permissions import IsOwnerPermission
from rest_framework.permissions import IsAuthenticated
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
    - id: идентификационный номер раздела;

    Запросы:
    - GET: Получение списка разделов пользователя.
    """

    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]

    def get_queryset(self):
        return Section.objects.filter(owner=self.request.user)


class SectionRetrieve(generics.RetrieveAPIView):
    """
    API для получения информации о конкретном разделе.

    Разрешения:
    - Аутентифицированные пользователи могут видеть только свои разделы.

    Поля:
    - title: Наименование раздела;
    - description: Описание раздела;
    - owner: Владелец;
    - id: идентификационный номер раздела;

    Запросы:
    - GET: Получение информации о конкретном разделе.
    """
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]

    def get_queryset(self):
        return Section.objects.filter(owner=self.request.user)


class SectionCreate(generics.CreateAPIView):
    """
    API для создания раздела.

    Разрешения:
    - Аутентифицированные пользователи могут создать новый раздел.

    Поля:
    - title: Наименование раздела;
    - description: Описание раздела;

    Запросы:
    - POST: Создание нового раздела.
    """
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SectionDestroy(generics.DestroyAPIView):
    """
    API для удаления конкретного раздела.

    Разрешения:
    - Аутентифицированные пользователи могут удалять только свой раздел.

    Поля:
    - title: Наименование раздела;
    - description: Описание раздела;
    - owner: Владелец;
    - id: идентификационный номер раздела;

    Запросы:
    - DELETE: Удаление конкретного раздела.
    """
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]


class SectionUpdate(generics.UpdateAPIView):
    """
    API для обновления информации о конкретном разделе.

    Разрешения:
    - Аутентифицированные пользователи могут обновлять только свой раздел.

    Поля:
    - title: Наименование раздела;
    - description: Описание раздела;
    - owner: Владелец;
    - id: идентификационный номер раздела;

    Запросы:
    - PUT: Полное обновление информации о разделе.
    - PATCH: Частичное обновление информации о конкретном разделе.
    """
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]


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
    - id: идентификационный номер материала;

    Запросы:
    - GET: Получение списка материалов пользователя.
    """

    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]

    def get_queryset(self):
        return Material.objects.filter(owner=self.request.user)


class MaterialRetrieve(generics.RetrieveAPIView):
    """
    API для получения информации о конкретном материале.

    Разрешения:
    - Аутентифицированные пользователи могут видеть только свои материалы.

    Поля:
    - title: Наименование материала;
    - description: Описание материалов;
    - text: Содержание;
    - owner: Владелец;
    - section: Раздел;
    - id: идентификационный номер материала;

    Запросы:
    - GET: Получение информации о конкретном материале.
    """

    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]

    def get_queryset(self):
        return Material.objects.filter(owner=self.request.user)


class MaterialCreate(generics.CreateAPIView):
    """
    API для создания материалов.

    Разрешения:
    - Аутентифицированные пользователи могут создать новый материал.

    Поля:
    - title: Наименование материала;
    - description: Описание материала;
    - text: Содержание;

    Запросы:
    - POST: Создание нового материала к указанному разделу (указывается в виде id в url).
    """
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        section_pk = self.kwargs.get('section_pk')
        section = get_object_or_404(Section, pk=section_pk)
        serializer.save(owner=self.request.user, section=section)


class MaterialDestroy(generics.DestroyAPIView):
    """
    API для удаления конкретного материала.

    Разрешения:
    - Аутентифицированные пользователи могут удалять только свой материал.

    Поля:
    - title: Наименование материала;
    - description: Описание материала;
    - text: Содержание;

    Запросы:
    - DELETE: Удаление конкретного материала.
    """
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]


class MaterialUpdate(generics.UpdateAPIView):
    """
    API для обновления информации о конкретном материале.

    Разрешения:
    - Аутентифицированные пользователи могут обновлять только свой материал.

    Поля:
    - title: Наименование материала;
    - description: Описание материала;
    - text: Содержание;

    Запросы:
    - PUT: Полное обновление информации о материале.
    - PATCH: Частичное обновление информации о конкретном материале.
    """
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]
