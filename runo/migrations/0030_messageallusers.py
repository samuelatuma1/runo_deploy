# Generated by Django 3.2 on 2021-08-09 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runo', '0029_userprofile_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageAllUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]