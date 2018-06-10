# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0061_auto_20180609_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugadores',
            name='apellido',
            field=models.CharField(max_length=25, blank=True),
        ),
        migrations.AlterField(
            model_name='jugadores',
            name='dorsal',
            field=models.CharField(max_length=2, blank=True),
        ),
        migrations.AlterField(
            model_name='jugadores',
            name='imagen',
            field=models.ImageField(default=b'static/img/jug-default.png', upload_to=b'plantilla/', blank=True),
        ),
        migrations.AlterField(
            model_name='jugadores',
            name='posicion',
            field=models.CharField(max_length=15, blank=True),
        ),
    ]
