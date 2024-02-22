from django.urls import path
from study.apps import StudyConfig
from .api import MyTestList, QuestionList, AnswerCheckAPI

app_name = StudyConfig.name

urlpatterns = [
    path('', MyTestList.as_view(), name='test_list'),
    path('question/', QuestionList.as_view(), name='question_list'),
    path('question/<int:question_id>/check-answer/', AnswerCheckAPI.as_view(), name='check_answer'),
]