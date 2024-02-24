from django.urls import path
from study.apps import StudyConfig
from .api import (MyTestList, MyTestRetrieve, MyTestCreate, MyTestUpdate, MyTestDestroy, QuestionList, AnswerCheckAPI,
                  QuestionRetrieve, QuestionCreate, QuestionUpdate, QuestionDestroy)

# Получение имени приложения Study
app_name = StudyConfig.name

# Определение маршрутов URL для различных операций с тестами и вопросами
urlpatterns = [
    path('', MyTestList.as_view(), name='test_list'),  # Список тестов
    path('<int:pk>/', MyTestRetrieve.as_view(), name='test_retrieve'),  # Получение теста
    path('<int:material_pk>/create/', MyTestCreate.as_view(), name='test_create'),  # Создание теста
    path('<int:pk>/update/', MyTestUpdate.as_view(), name='test_update'),  # Обновление теста
    path('<int:pk>/delete/', MyTestDestroy.as_view(), name='test_delete'),  # Удаление теста

    path('question/', QuestionList.as_view(), name='question_list'),  # Список вопросов
    path('question/<int:question_id>/check-answer/', AnswerCheckAPI.as_view(), name='check_answer'),  # Проверка ответа
    path('question/<int:pk>/', QuestionRetrieve.as_view(), name='question_retrieve'),  # Получение вопроса
    path('question/<int:pk>/update/', QuestionUpdate.as_view(), name='question_update'),  # Обновление вопроса
    path('question/<int:pk>/delete/', QuestionDestroy.as_view(), name='question_delete'),  # Удаление вопроса
    path('<int:test_pk>/question/create/', QuestionCreate.as_view(), name='question_create'),  # Создание вопроса
]
