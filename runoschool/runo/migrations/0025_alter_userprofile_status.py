# Generated by Django 3.2 on 2021-08-01 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runo', '0024_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='status',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
