from django.urls import path
from study.apps import StudyConfig
from .api import *

app_name = StudyConfig.name

urlpatterns = [
    path('', MyTestList.as_view(), name='test_list'),
    path('<int:pk>/', MyTestRetrieve.as_view(), name='test_retrieve'),
    path('<int:material_pk>/create/', MyTestCreate.as_view(), name='test_create'),
    path('<int:pk>/update/', MyTestUpdate.as_view(), name='test_update'),
    path('<int:pk>/delete/', MyTestDestroy.as_view(), name='test_delete'),

    path('question/', QuestionList.as_view(), name='question_list'),
    path('question/<int:question_id>/check-answer/', AnswerCheckAPI.as_view(), name='check_answer'),
    path('question/<int:pk>/', QuestionRetrieve.as_view(), name='question_retrieve'),
    path('question/<int:pk>/update/', QuestionUpdate.as_view(), name='question_update'),
    path('question/<int:pk>/delete/', QuestionDestroy.as_view(), name='question_delete'),
    path('<int:test_pk>/question/create/', QuestionCreate.as_view(), name='question_create'),
]