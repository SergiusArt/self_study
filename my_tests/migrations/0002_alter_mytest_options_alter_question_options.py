# Generated by Django 5.0.2 on 2024-02-19 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mytest',
            options={'verbose_name': 'Мой тест', 'verbose_name_plural': 'Мои тесты'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
    ]
