from rest_framework import serializers
from study.models import Section, Material


# Сериализатор для модели Section
class SectionSerializer(serializers.ModelSerializer):

    owner = serializers.EmailField(source='owner.email', read_only=True)  # Поле для электронной почты владельца

    class Meta:
        model = Section  # Используемая модель
        fields = ['title', 'description', 'owner', 'id']  # Поля для сериализации


# Сериализатор для модели Material
class MaterialSerializer(serializers.ModelSerializer):

    section = serializers.CharField(source='section.title', read_only=True)  # Поле для названия раздела
    owner = serializers.EmailField(source='owner.email', read_only=True)   # Поле для электронной почты владельца

    class Meta:
        model = Material  # Используемая модель
        fields = ['title', 'description', 'text', 'owner', 'section', 'id']  # Поля для сериализации
