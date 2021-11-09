# Generated by Django 3.2.8 on 2021-11-08 01:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0010_incapacidad_incapacidadslide'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aseguradora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to='images')),
                ('posicion', models.IntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(50)])),
            ],
        ),
        migrations.AlterModelOptions(
            name='incapacidadslide',
            options={},
        ),
    ]
