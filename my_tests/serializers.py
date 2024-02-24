from rest_framework import serializers
from my_tests.models import MyTest, Question


class MyTestSerializer(serializers.ModelSerializer):

    owner = serializers.EmailField(source='owner.email', read_only=True)
    material = serializers.CharField(source='material.title', read_only=True)

    class Meta:
        model = MyTest
        fields = ['owner', 'material', 'title', 'id']


class QuestionSerializer(serializers.ModelSerializer):

    mytest = serializers.CharField(source='mytest.title', read_only=True)

    class Meta:
        model = Question
        fields = ['text', 'mytest', 'id']


class QuestionDetailSerializer(serializers.ModelSerializer):

    mytest = serializers.CharField(source='mytest.title', read_only=True)

    class Meta:
        model = Question
        fields = ['text', 'true_answer', 'mytest', 'id']


class AnswerCheckSerializer(serializers.Serializer):
    user_answer = serializers.CharField()

    def validate(self, data):
        user_answer = data.get('user_answer')
        question = self.context['question']

        if user_answer == question.true_answer:
            data['result'] = 'Верный ответ!'
        else:
            data['result'] = 'Не верно'

        return data
