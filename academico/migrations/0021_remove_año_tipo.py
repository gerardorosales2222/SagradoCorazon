# Generated by Django 5.1 on 2024-09-03 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0020_remove_año_observacion_remove_division_observacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='año',
            name='Tipo',
        ),
    ]
