# Generated by Django 5.1 on 2024-09-02 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0008_año_division_nivel_cursos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='casas',
            options={'verbose_name': 'Casa', 'verbose_name_plural': 'Casas'},
        ),
        migrations.AlterModelOptions(
            name='colegios',
            options={'verbose_name': 'Colegio', 'verbose_name_plural': 'Colegios'},
        ),
        migrations.AlterModelTable(
            name='casas',
            table='Casas',
        ),
        migrations.AlterModelTable(
            name='colegios',
            table='Colegios',
        ),
    ]
