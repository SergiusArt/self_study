from django.urls import path
from study.apps import StudyConfig
from .api import *

app_name = StudyConfig.name

urlpatterns = [
    path('', SectionList.as_view(), name='section_list'),
    path('<int:pk>/', SectionRetrieve.as_view(), name='section_retrieve'),
    path('create/', SectionCreate.as_view(), name='section_create'),
    path('<int:pk>/update/', SectionUpdate.as_view(), name='section_update'),
    path('<int:pk>/delete/', SectionDestroy.as_view(), name='section_delete'),

    path('material/', MaterialList.as_view(), name='material_list'),
    path('material/<int:pk>/', MaterialRetrieve.as_view(), name='material_retrieve'),
    path('<int:section_pk>/material/create/', MaterialCreate.as_view(), name='material_create'),
    path('material/<int:pk>/update/', MaterialUpdate.as_view(), name='material_update'),
    path('material/<int:pk>/delete/', MaterialDestroy.as_view(), name='material_delete'),
]
