# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0039_delete_galeriaequipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='GaleriaEquipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoria', models.CharField(max_length=30)),
                ('imagen', models.ImageField(upload_to=b'categorias')),
                ('equipo', models.CharField(max_length=30)),
                ('descripcion', models.TextField(max_length=50)),
                ('enlace', models.TextField(max_length=50)),
            ],
        ),
    ]
