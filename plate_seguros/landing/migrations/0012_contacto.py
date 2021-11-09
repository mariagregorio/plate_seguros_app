# Generated by Django 3.2.8 on 2021-11-08 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0011_auto_20211107_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('instagram', models.CharField(max_length=250)),
                ('facebook', models.CharField(max_length=250)),
                ('linkedin', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('telefono1', models.CharField(max_length=50)),
                ('telefono2', models.CharField(max_length=50)),
                ('telefono3', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contacto',
            },
        ),
    ]
