# Generated by Django 5.1 on 2024-09-03 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0028_alter_alumnos_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='Sexo',
            field=models.CharField(choices=[('V', 'Varón'), ('M', 'Mujer')], max_length=1),
        ),
    ]
