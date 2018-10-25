# Generated by Django 2.1.1 on 2018-10-25 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Django_Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('example_path', models.FilePathField(allow_files=False, allow_folders=True, path='C:\\users\\sakodaken\\pycharmprojects\\djangoruler3\\project')),
            ],
        ),
        migrations.CreateModel(
            name='LargeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('largecategoryname', models.CharField(max_length=200, verbose_name='大カテゴリー名')),
            ],
        ),
        migrations.CreateModel(
            name='MiddleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middlecategoryname', models.CharField(max_length=200, verbose_name='中カテゴリー名')),
                ('largecategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_example.LargeCategory', verbose_name='大カテゴリー')),
            ],
        ),
    ]
