# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0058_galeriaequipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plantilla',
            fields=[
                ('id', models.CharField(max_length=25, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('posicion', models.CharField(max_length=15)),
                ('numero', models.CharField(max_length=2)),
                ('imagen', models.ImageField(upload_to=b'plantilla')),
                ('equipo', models.ForeignKey(to='appbasket.GaleriaEquipo')),
            ],
        ),
    ]
