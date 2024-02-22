from users.serializers import UserSerializer

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST


class UserRegistrationView(generics.CreateAPIView):
    """
    API для регистрации нового пользователя.

    Поля:
    - email: почта пользователя (уникальное поле);
    - password: пароль пользователя;

    Запросы:
    - POST: Создание нового пользователя. Ожидается передача данных пользователя в формате JSON.
    """

    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
