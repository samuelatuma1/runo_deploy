# Generated by Django 3.2 on 2021-07-25 05:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('runo', '0010_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class', models.CharField(choices=[('1', 'Pre-Nursery'), ('2', 'Nursery 1'), ('3', 'Nursey 2'), ('3', 'Nursery 3')], default='1', max_length=30)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
