# Generated by Django 5.1 on 2024-09-19 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0008_alter_notas_carpeta_alter_notas_conducta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='años',
            field=models.CharField(choices=[('Primero', '1'), ('2', 'Segundo'), ('3', 'Tercero'), ('4', 'Cuarto'), ('5', 'Quinto'), ('6', 'Sexto'), ('7', 'Septimo')], default=1, max_length=30),
        ),
    ]
