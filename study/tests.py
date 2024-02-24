from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from users.models import User
from .models import Section, Material


class StudyTestCase(TestCase):
    # Начальные условия для тестов
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='user_test@sky.pro', is_superuser=False)
        self.user.set_password('user_test')
        self.user.save()
        self.client.force_authenticate(user=self.user)

    # Проверка на создание раздела
    def test_section_create(self):
        url = reverse('study:section_create')
        data = {
            'owner': self.user.id,
            'title': 'Тестовый раздел',
            'description': 'Тестовое описание',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Section.objects.count(), 1)
        self.assertEqual(Section.objects.get().title, 'Тестовый раздел')

    # Проверка на получение списка разделов
    def test_own_section_list(self):
        Section.objects.create(owner=self.user, title='Тестовый раздел 1', description='Тестовое описание 1')
        Section.objects.create(owner=self.user, title='Тестовый раздел 2', description='Тестовое описание 2')
        url = reverse('study:section_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Section.objects.filter(owner=self.user).count(), 2)

    # Проверка на удаление раздела
    def test_section_delete(self):
        section = Section.objects.create(owner=self.user, title='Тестовый раздел 1', description='Тестовое описание 1')
        url = reverse('study:section_delete', args=[section.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Section.objects.count(), 0)

    # Проверка на получение раздела
    def test_own_section_retrieve(self):
        section = Section.objects.create(owner=self.user, title='Тестовый раздел 1', description='Тестовое описание 1')
        url = reverse('study:section_retrieve', args=[section.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], section.title)

    # Проверка на полное обновление раздела
    def test_section_update_put(self):
        section = Section.objects.create(
            owner=self.user, title='Test Section', description='Test Description'
        )
        url = reverse('study:section_update', args=[section.pk])
        data = {
            'title': 'Updated Test Section',
            'description': 'Updated Test Description',
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Section.objects.get(pk=section.pk).title, 'Updated Test Section')
        self.assertEqual(Section.objects.get(pk=section.pk).description, 'Updated Test Description')

    # Проверка на частичное обновление раздела
    def test_section_update_patch(self):
        section = Section.objects.create(
            owner=self.user, title='Test Section', description='Test Description'
        )
        url = reverse('study:section_update', args=[section.pk])
        data = {
            'title': 'Updated Test Section',
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Section.objects.get(pk=section.pk).title, 'Updated Test Section')
        self.assertEqual(Section.objects.get(pk=section.pk).description, 'Test Description')

    # Проверка на отображение списка материалов
    def test_material_list(self):
        Material.objects.create(
            owner=self.user, title='Тестовый материал 1',
            description='Тестовое описание 1',
            text='Тестовый текст 1'
        )
        Material.objects.create(
            owner=self.user, title='Тестовый материал 2',
            description='Тестовое описание 2',
            text='Тестовый текст 2'
        )
        url = reverse('study:material_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Material.objects.filter(owner=self.user).count(), 2)

    # Проверка на отображение материала
    def test_own_material_retrieve(self):
        material = Material.objects.create(
            owner=self.user, title='Тестовый материал 1',
            description='Тестовое описание 1',
            text='Тестовый текст 1'
        )
        url = reverse('study:material_retrieve', args=[material.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], material.title)

    # Проверка на создание материала
    def test_material_create(self):
        section = Section.objects.create(
            owner=self.user, title='Test Section', description='Test Description'
        )
        url = reverse('study:material_create', args=[section.pk])
        data = {
            'owner': self.user.id,
            'title': 'Тестовый материал',
            'description': 'Тестовое описание',
            'text': 'Тестовый текст'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Material.objects.count(), 1)
        self.assertEqual(Material.objects.get().title, 'Тестовый материал')

    # Проверка на удаление материала
    def test_material_delete(self):
        section = Section.objects.create(
            owner=self.user,
            title='Test Section',
            description='Test Description'
        )
        material = Material.objects.create(
            owner=self.user,
            title='Тестовый материал 1',
            description='Тестовое описание 1',
            text='Тестовый текст 1',
            section=section
        )
        url = reverse('study:material_delete', args=[material.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Material.objects.count(), 0)

    # Проверка на обновление материала
    def test_material_update_put(self):
        material = Material.objects.create(
            owner=self.user,
            title='Test Material',
            description='Test Description',
            text='Test Text'
        )
        url = reverse('study:material_update', args=[material.pk])
        data = {
            'title': 'Updated Test Material',
            'description': 'Updated Test Description',
            'text': 'Updated Test Text'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Material.objects.get(pk=material.pk).title, 'Updated Test Material')
        self.assertEqual(Material.objects.get(pk=material.pk).description, 'Updated Test Description')
        self.assertEqual(Material.objects.get(pk=material.pk).text, 'Updated Test Text')

    # Проверка на частичное обновление материала
    def test_material_update_patch(self):
        material = Material.objects.create(
            owner=self.user,
            title='Test Material',
            description='Test Description',
            text='Test Text'
        )
        url = reverse('study:material_update', args=[material.pk])
        data = {
            'title': 'Updated Test Material',
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Material.objects.get(pk=material.pk).title, 'Updated Test Material')
        self.assertEqual(Material.objects.get(pk=material.pk).description, 'Test Description')
