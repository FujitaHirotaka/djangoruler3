# Generated by Django 2.1.1 on 2018-11-01 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20181101_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='django_project4',
            name='project_path',
            field=models.FilePathField(allow_files=False, allow_folders=True, path='C:\\Users\\sakodaken\\PycharmProjects', recursive=True),
        ),
    ]
