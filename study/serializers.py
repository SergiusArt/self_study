from rest_framework import serializers
from study.models import Section, Material
from users.models import User


class SectionSerializer(serializers.ModelSerializer):

    owner = serializers.EmailField(source='owner.email', read_only=True)

    class Meta:
        model = Section
        fields = ['title', 'description', 'owner', 'id']


class MaterialSerializer(serializers.ModelSerializer):

    section = serializers.CharField(source='section.title', read_only=True)
    owner = serializers.EmailField(source='owner.email', read_only=True)

    class Meta:
        model = Material
        fields = ['title', 'description', 'text', 'owner', 'section', 'id']

