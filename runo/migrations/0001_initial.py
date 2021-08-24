# Generated by Django 3.2 on 2021-07-17 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolName', models.CharField(default='RUNO DAYSPRING SCHOOL', max_length=50)),
                ('img', models.ImageField(upload_to='intro/')),
                ('desc', models.TextField()),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-uploaded'],
            },
        ),
    ]