# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0052_auto_20180608_1955'),
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
            ],
        ),
        migrations.AlterField(
            model_name='galeriaequipo',
            name='categoria',
            field=models.CharField(max_length=30, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='galeriaequipo',
            name='id',
            field=models.CharField(max_length=25, primary_key=True),
        ),
    ]
