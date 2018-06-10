# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0067_remove_plantilla_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrenadores',
            fields=[
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=20, blank=True)),
                ('id', models.CharField(max_length=4, serialize=False, primary_key=True)),
                ('imagen', models.ImageField(default=b'plantilla/default.jpeg', upload_to=b'plantilla/', blank=True)),
                ('equipo', models.ForeignKey(to='appbasket.Plantilla')),
            ],
        ),
    ]
