from users.permissions import IsOwnerPermission
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from .serializers import QuestionSerializer, MyTestSerializer, AnswerCheckSerializer
from .models import MyTest, Question
from rest_framework.response import Response


class MyTestList(generics.ListAPIView):
    """
    API для получения списка названий тестов.

    Разрешения:
    - Аутентифицированные пользователи могут видеть только свои тесты.

    Поля:
    - owner: Владелец;
    - material: Материал;
    - title: Заголовок теста;

    Запросы:
    - GET: Получение списка тестов пользователя.
    """

    serializer_class = MyTestSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]

    def get_queryset(self):
        return MyTest.objects.filter(owner=self.request.user)


class QuestionList(generics.ListAPIView):
    """
    API для получения списка материалов тестов.

    Разрешения:
    - Аутентифицированные пользователи могут видеть только свои материалы тестов.

    Поля:
    - text: Текст вопроса и варианты ответа;
    - mytest: Наименование теста;
    - id: идентификационный номер теста;

    Запросы:
    - GET: Получение списка материалов тестов пользователя.
    """

    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]

    def get_queryset(self):
        # Получить все вопросы, относящиеся к тестам владельца (пользователя)
        return Question.objects.filter(mytest__owner=self.request.user)


class AnswerCheckAPI(generics.GenericAPIView):
    """
    API для получения результата ответа на выбранный вопрос теста.

    Разрешения:
    - Аутентифицированные пользователи могут видеть только свои материалы тестов.

    Поля:
    - user_answer: ответ на вопрос теста;

    Запросы:
    - POST: Получение результата ответа на выбранный вопрос теста (указывается в виде id в url).
    """
    serializer_class = AnswerCheckSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]

    def post(self, request, *args, **kwargs):
        question_id = self.kwargs.get('question_id')
        question = Question.objects.get(id=question_id)

        serializer = self.get_serializer(data=request.data, context={'question': question})
        serializer.is_valid(raise_exception=True)

        response_data = serializer.validated_data

        return Response(response_data)
