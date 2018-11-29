# Generated by Django 2.1.2 on 2018-11-29 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppSpecie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='アプリの種類')),
            ],
            options={
                'verbose_name_plural': 'アプリの種類',
            },
        ),
        migrations.CreateModel(
            name='AppType_1',
            fields=[
                ('object_id', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='オブジェクトID')),
                ('appNo', models.CharField(max_length=10, verbose_name='アプリＮｏ')),
                ('indexURL', models.CharField(max_length=255, verbose_name='indexページのURL')),
            ],
            options={
                'verbose_name_plural': 'AppType_1フォーム（関数view_モデルなし）',
            },
        ),
        migrations.CreateModel(
            name='DjangoApp',
            fields=[
                ('appNo', models.CharField(max_length=10, verbose_name='アプリＩＤ')),
                ('app_name', models.CharField(max_length=255, verbose_name='アプリ名')),
                ('object_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('app_specie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.AppSpecie', verbose_name='アプリの種類')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': 'アプリ',
            },
        ),
        migrations.CreateModel(
            name='DjangoProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255, unique=True, verbose_name='プロジェクト名')),
            ],
            options={
                'verbose_name_plural': 'プロジェクト',
            },
        ),
        migrations.AddField(
            model_name='djangoapp',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.DjangoProject', verbose_name='プロジェクト名'),
        ),
        migrations.AddField(
            model_name='apptype_1',
            name='app_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.DjangoApp', verbose_name='アプリ名'),
        ),
    ]
