from django.urls import path
from study.apps import StudyConfig
from .api import SectionList, MaterialList

app_name = StudyConfig.name

urlpatterns = [
    path('', SectionList.as_view(), name='section_list'),
    path('material/', MaterialList.as_view(), name='material_list'),
]
