# Generated by Django 5.1 on 2024-09-03 14:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0022_remove_materias_profesor_interino_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materias',
            name='Docente_Titular',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academico.docentes'),
        ),
    ]
