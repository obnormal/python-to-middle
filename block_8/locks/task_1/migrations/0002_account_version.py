# Generated by Django 3.2.13 on 2022-08-08 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locks_task_1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='version',
            field=models.IntegerField(default=0),
        ),
    ]
