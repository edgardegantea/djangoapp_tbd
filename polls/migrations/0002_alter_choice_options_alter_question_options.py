# Generated by Django 4.1 on 2022-08-25 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': 'Opción', 'verbose_name_plural': 'Opciones'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Pregunta', 'verbose_name_plural': 'Preguntas'},
        ),
    ]
