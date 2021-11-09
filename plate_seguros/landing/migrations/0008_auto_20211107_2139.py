# Generated by Django 3.2.8 on 2021-11-08 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0007_quienessomos_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('subtitulo', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Home',
            },
        ),
        migrations.AlterModelOptions(
            name='quienessomos',
            options={'verbose_name': 'Quienes Somos'},
        ),
        migrations.AlterModelOptions(
            name='segurosencabezado',
            options={'verbose_name': 'Seguros Encabezado'},
        ),
    ]