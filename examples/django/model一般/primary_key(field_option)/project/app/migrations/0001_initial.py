# Generated by Django 2.1.1 on 2018-11-22 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='選手名')),
            ],
        ),
    ]
