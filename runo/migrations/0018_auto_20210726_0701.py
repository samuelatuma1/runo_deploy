# Generated by Django 3.2 on 2021-07-26 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runo', '0017_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='is_student',
        ),
        migrations.AddField(
            model_name='userclass',
            name='is_student',
            field=models.BooleanField(default=True),
        ),
    ]
