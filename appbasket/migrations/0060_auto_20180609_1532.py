# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0059_plantilla'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jugadores',
            fields=[
                ('id', models.CharField(max_length=25, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('posicion', models.CharField(max_length=15)),
                ('numero', models.CharField(max_length=2)),
                ('imagen', models.ImageField(upload_to=b'plantilla')),
            ],
        ),
        migrations.RemoveField(
            model_name='plantilla',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='plantilla',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='plantilla',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='plantilla',
            name='numero',
        ),
        migrations.RemoveField(
            model_name='plantilla',
            name='posicion',
        ),
        migrations.AddField(
            model_name='jugadores',
            name='equipo',
            field=models.ForeignKey(to='appbasket.Plantilla'),
        ),
    ]
