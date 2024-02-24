from django.shortcuts import get_object_or_404

from study.models import Material
from users.permissions import IsOwnerPermission
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from .serializers import QuestionSerializer, MyTestSerializer, AnswerCheckSerializer, QuestionDetailSerializer
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
    - id: идентификационный номер теста;

    Запросы:
    - GET: Получение списка тестов пользователя.
    """

    serializer_class = MyTestSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]

    def get_queryset(self):
        return MyTest.objects.filter(owner=self.request.user)


class MyTestRetrieve(generics.RetrieveAPIView):
    """
    API для получения информации о конкретном тесте.

    Разрешения:
    - Аутентифицированные пользователи могут видеть только свои тесты.

    Поля:
    - owner: Владелец;
    - material: Материал;
    - title: Заголовок теста;

    Запросы:
    - GET: Получение информации о конкретном тесте.
    """
    serializer_class = MyTestSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]

    def get_queryset(self):
        return MyTest.objects.filter(owner=self.request.user)


class MyTestCreate(generics.CreateAPIView):
    """
    API для создания нового теста.

    Разрешения:
    - Аутентифицированные пользователи могут создавать новый тест.

    Поля:
    - owner: Владелец;
    - material: Материал;
    - title: Заголовок теста;

    Запросы:
    - POST: Создание нового теста.
    """
    serializer_class = MyTestSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]

    def perform_create(self, serializer):
        material_pk = self.kwargs.get('material_pk')
        material = get_object_or_404(Material, pk=material_pk)
        serializer.save(owner=self.request.user, material=material)


class MyTestUpdate(generics.UpdateAPIView):
    """
    API для обновления информации о конкретном тесте.

    Разрешения:
    - Аутентифицированные пользователи могут обновлять только свои тесты.

    Поля:
    - owner: Владелец;
    - material: Материал;
    - title: Заголовок теста;

    Запросы:
    - PUT: Обновление информации о конкретном тесте.
    - PATCH: Обновление информации о конкретном тесте.
    """
    serializer_class = MyTestSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    queryset = MyTest.objects.all()


class MyTestDestroy(generics.DestroyAPIView):
    """
    API для удаления конкретного теста.

    Разрешения:
    - Аутентифицированные пользователи могут удалять только свои тесты.

    Поля:
    - owner: Владелец;
    - material: Материал;
    - title: Заголовок теста;

    Запросы:
    - DELETE: Удаление конкретного теста.
    """
    serializer_class = MyTestSerializer
    queryset = MyTest.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerPermission]


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
    queryset = Question.objects.all()

    def get_queryset(self):
        # Получить все вопросы, относящиеся к тестам владельца (пользователя)
        return Question.objects.filter(mytest__owner=self.request.user)


class QuestionRetrieve(generics.RetrieveAPIView):
    """
    API для получения информации о конкретном материале теста.

    Разрешения:
    - Аутентифицированные пользователи могут видеть только свои материалы тестов.

    Поля:
    - text: Текст вопроса и варианты ответа;
    - mytest: Наименование теста;
    - id: идентификационный номер теста;

    Запросы:
    - GET: Получение информации о конкретном материале теста.
    """
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]

    def get_queryset(self):
        # Получить все вопросы, относящиеся к тестам владельца (пользователя)
        return Question.objects.filter(mytest__owner=self.request.user)


class QuestionCreate(generics.CreateAPIView):
    """
    API для создания нового вопроса.

    Разрешения:
    - Аутентифицированные пользователи могут создавать новый вопрос.

    Поля:
    - text: Текст вопроса и варианты ответа;
    - mytest: Наименование теста;
    - id: идентификационный номер теста;

    Запросы:
    - POST: Создание нового вопроса.
    """
    serializer_class = QuestionDetailSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]

    def perform_create(self, serializer):
        test_pk = self.kwargs.get('test_pk')
        mytest = get_object_or_404(MyTest, pk=test_pk)
        text = serializer.validated_data['text']
        true_answer = serializer.validated_data['true_answer']
        serializer.save(mytest=mytest, text=text, true_answer=true_answer)


class QuestionDestroy(generics.DestroyAPIView):
    """
    API для удаления конкретного вопроса.

    Разрешения:
    - Аутентифицированные пользователи могут удалять только свои вопросы.

    Поля:
    - text: Текст вопроса и варианты ответа;
    - mytest: Наименование теста;
    - id: идентификационный номер теста;

    Запросы:
    - DELETE: Удаление конкретного вопроса.
    """
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    queryset = Question.objects.all()


class QuestionUpdate(generics.UpdateAPIView):
    """
    API для обновления конкретного вопроса.

    Разрешения:
    - Аутентифицированные пользователи могут обновлять только свои вопросы.

    Поля:
    - text: Текст вопроса и варианты ответа;
    - mytest: Наименование теста;
    - id: идентификационный номер теста;

    Запросы:
    - PUT: Полное обновление конкретного вопроса.
    - PATCH: Частичное обновление конкретного вопроса.
    """
    serializer_class = QuestionDetailSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    queryset = Question.objects.all()


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
