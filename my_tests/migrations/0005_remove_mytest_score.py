# Generated by Django 5.0.2 on 2024-02-22 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_tests', '0004_remove_question_user_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mytest',
            name='score',
        ),
    ]