from rest_framework import serializers
from my_tests.models import MyTest, Question


# Сериализатор для модели MyTest
class MyTestSerializer(serializers.ModelSerializer):

    owner = serializers.EmailField(source='owner.email', read_only=True)  # Поле для владельца (почта)
    material = serializers.CharField(source='material.title', read_only=True)  # Поле для названия материала

    class Meta:
        model = MyTest  # Используемая модель
        fields = ['owner', 'material', 'title', 'id']  # Поля для сериализации


# Сериализатор для модели Question
class QuestionSerializer(serializers.ModelSerializer):

    mytest = serializers.CharField(source='mytest.title', read_only=True)  # Поле для названия теста

    class Meta:
        model = Question  # Используемая модель
        fields = ['text', 'mytest', 'id']  # Поля для сериализации


# Сериализатор для детальной информации о вопросе
class QuestionDetailSerializer(serializers.ModelSerializer):

    mytest = serializers.CharField(source='mytest.title', read_only=True)  # Поле для названия теста

    class Meta:
        model = Question  # Используемая модель
        fields = ['text', 'true_answer', 'mytest', 'id']  # Поля для сериализации


# Сериализатор для проверки ответа пользователя
class AnswerCheckSerializer(serializers.Serializer):
    user_answer = serializers.CharField()  # Поле для ответа пользователя

    def validate(self, data):
        user_answer = data.get('user_answer')
        question = self.context['question']  # Получение объекта вопроса из контекста

        if user_answer == question.true_answer:  # Проверка правильности ответа
            data['result'] = 'Верный ответ!'
        else:
            data['result'] = 'Не верно'

        return data  # Возвращение данных после проверки
