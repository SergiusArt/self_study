from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from study.models import Material
from users.models import User
from .models import MyTest, Question


class MyTestsTestCase(TestCase):
    # Начальные условия для тестов
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='user_test@sky.pro', is_superuser=False)
        self.user.set_password('user_test')
        self.user.save()
        self.client.force_authenticate(user=self.user)

    # Проверяет создание нового объекта MyTest через API.
    def test_mytest_create(self):
        material = Material.objects.create(
            owner=self.user,
            title='Test Section',
            description='Test Description',
            text='Test Text'
        )
        url = reverse('tests:test_create', args=[material.pk])
        data = {
            'owner': self.user.id,
            'title': 'Тестовый Тест'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MyTest.objects.count(), 1)
        self.assertEqual(MyTest.objects.get().title, 'Тестовый Тест')

    # Проверяет удаление объекта MyTest через API.
    def test_mytest_delete(self):
        material = Material.objects.create(
            owner=self.user,
            title='Test Section',
            description='Test Description',
            text='Test Text'
        )
        mytest = MyTest.objects.create(
            owner=self.user,
            title='Тестовый Тест 1',
            material=material
        )
        url = reverse('tests:test_delete', args=[mytest.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(MyTest.objects.count(), 0)

    # Проверяет получение списка объектов MyTest через API.
    def test_mytest_list(self):
        material = Material.objects.create(
            owner=self.user,
            title='Test Section',
            description='Test Description',
            text='Test Text'
        )
        MyTest.objects.create(
            owner=self.user,
            title='Тестовый Тест 1',
            material=material
        )
        MyTest.objects.create(
            owner=self.user,
            title='Тестовый Тест 1',
            material=material
        )
        url = reverse('tests:test_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(MyTest.objects.filter(owner=self.user).count(), 2)

    # Проверяет получение конкретного объекта MyTest через API.
    def test_mytest_retrieve(self):
        material = Material.objects.create(
            owner=self.user,
            title='Test Section',
            description='Test Description',
            text='Test Text'
        )
        mytests = MyTest.objects.create(
            owner=self.user,
            title='Тестовый Тест 1',
            material=material
        )
        url = reverse('tests:test_retrieve', args=[mytests.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], mytests.title)

    # Проверяет обновление объекта MyTest через API.
    def test_mytest_update_put_patch(self):
        material = Material.objects.create(
            owner=self.user,
            title='Test Section',
            description='Test Description',
            text='Test Text'
        )
        mytests = MyTest.objects.create(
            owner=self.user,
            title='Тестовый Тест 1',
            material=material
        )
        url = reverse('tests:test_update', args=[mytests.pk])
        data = {
            'title': 'Updated Test MyTest',
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(MyTest.objects.get(pk=mytests.pk).title, 'Updated Test MyTest')

        data = {
            'title': 'Updated 2 Test MyTest',
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(MyTest.objects.get(pk=mytests.pk).title, 'Updated 2 Test MyTest')

    # Проверяет создание нового объекта Question через API.
    def test_question_create(self):
        material = Material.objects.create(
            owner=self.user,
            title='Test Section',
            description='Test Description',
            text='Test Text'
        )
        mytests = MyTest.objects.create(
            owner=self.user,
            title='Тестовый Тест 1',
            material=material
        )
        url = reverse('tests:question_create', args=[mytests.pk])
        data = {
            'text': 'Вопрос на тест №1',
            'true_answer': '3'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.count(), 1)
        self.assertEqual(Question.objects.get().true_answer, '3')

    # Проверяет удаление объекта Question через API.
    def test_question_delete(self):
        material = Material.objects.create(
            owner=self.user,
            title='Test Section',
            description='Test Description',
            text='Test Text'
        )
        mytests = MyTest.objects.create(
            owner=self.user,
            title='Тестовый Тест 1',
            material=material
        )
        question = Question.objects.create(
            text='Вопрос на тест №1',
            true_answer='3',
            mytest=mytests
        )
        url = reverse('tests:question_delete', args=[question.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Question.objects.count(), 0)

    # Проверяет получение списка объектов Question через API.
    def test_question_list(self):
        material = Material.objects.create(
            owner=self.user,
            title='Test Section',
            description='Test Description',
            text='Test Text'
        )
        mytests = MyTest.objects.create(
            owner=self.user,
            title='Тестовый Тест 1',
            material=material
        )
        Question.objects.create(
            text='Вопрос на тест №1',
            true_answer='3',
            mytest=mytests
        )
        Question.objects.create(
            text='Вопрос на тест №2',
            true_answer='4',
            mytest=mytests
        )
        url = reverse('tests:question_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Question.objects.count(), 2)

    # Проверяет получение конкретного объекта Question через API.
    def test_question_retrieve(self):
        material = Material.objects.create(
            owner=self.user,
            title='Test Section',
            description='Test Description',
            text='Test Text'
        )
        mytests = MyTest.objects.create(
            owner=self.user,
            title='Тестовый Тест 1',
            material=material
        )
        question = Question.objects.create(
            text='Вопрос на тест №1',
            true_answer='3',
            mytest=mytests
        )
        url = reverse('tests:question_retrieve', args=[question.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], question.text)

    # Проверяет обновление объекта Question через API.
    def test_question_update_put_patch(self):
        material = Material.objects.create(
            owner=self.user,
            title='Test Section',
            description='Test Description',
            text='Test Text'
        )
        mytests = MyTest.objects.create(
            owner=self.user,
            title='Тестовый Тест 1',
            material=material
        )
        question = Question.objects.create(
            text='Вопрос на тест №1',
            true_answer='3',
            mytest=mytests
        )
        url = reverse('tests:question_update', args=[question.pk])
        data = {
            'text': 'Updated Question',
            'true_answer': '4'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Question.objects.get(pk=question.pk).text, 'Updated Question')
        self.assertEqual(Question.objects.get(pk=question.pk).true_answer, '4')

        data = {
            'text': 'Updated 2 Question',
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Question.objects.get(pk=question.pk).text, 'Updated 2 Question')
