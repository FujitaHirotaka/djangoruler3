# Generated by Django 2.1.1 on 2018-11-01 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='django_project4',
            name='project_path',
            field=models.FilePathField(allow_files=False, allow_folders=True, match='ff*', path='C:\\Users\\sakodaken\\PycharmProjects', recursive=True),
        ),
    ]
