# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0035_columna'),
    ]

    operations = [
        migrations.CreateModel(
            name='GaleriaEquipos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoria', models.CharField(max_length=30)),
                ('imagen', models.ImageField(upload_to=b'categorias')),
                ('equipo', models.CharField(max_length=30)),
                ('descripcion', models.TextField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='columna',
            name='texto',
            field=models.TextField(max_length=250),
        ),
    ]
