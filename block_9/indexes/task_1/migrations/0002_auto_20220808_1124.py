# Generated by Django 3.2.13 on 2022-08-08 11:24

from django.db import migrations
from django.core import (
    serializers,
)


def load_data(apps, schema_editor):
    Employee = apps.get_model('indexes_task_1', 'Employee')  
    if not Employee.objects.exists():
        path = '/opt/project/block_9/indexes/task_1/migrations/test.json'
        with open(path, 'r') as f:
            data = f.read()

        for obj in serializers.deserialize("json", data):
            obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('indexes_task_1', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data),
    ]
