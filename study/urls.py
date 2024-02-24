from django.urls import path
from study.apps import StudyConfig
from .api import SectionList, SectionRetrieve, SectionCreate, SectionUpdate, SectionDestroy, MaterialList, \
    MaterialRetrieve, MaterialCreate, MaterialUpdate, MaterialDestroy

# Маршруты URL для приложения Study
app_name = StudyConfig.name  # Установка имени приложения

urlpatterns = [
    path('', SectionList.as_view(), name='section_list'),  # Список разделов
    path('<int:pk>/', SectionRetrieve.as_view(), name='section_retrieve'),  # Детали раздела.
    path('create/', SectionCreate.as_view(), name='section_create'),  # Создание раздела.
    path('<int:pk>/update/', SectionUpdate.as_view(), name='section_update'),  # Обновление раздела.
    path('<int:pk>/delete/', SectionDestroy.as_view(), name='section_delete'),  # Удаление раздела.

    path('material/', MaterialList.as_view(), name='material_list'),  # Список материалов
    path('material/<int:pk>/', MaterialRetrieve.as_view(), name='material_retrieve'),  # Детали материала.
    path('<int:section_pk>/material/create/', MaterialCreate.as_view(), name='material_create'),  # Создание материала.
    path('material/<int:pk>/update/', MaterialUpdate.as_view(), name='material_update'),  # Обновление материала.
    path('material/<int:pk>/delete/', MaterialDestroy.as_view(), name='material_delete'),  # Удаление материала.
]
