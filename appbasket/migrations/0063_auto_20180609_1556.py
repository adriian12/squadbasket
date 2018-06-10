# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0062_auto_20180609_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugadores',
            name='apellido',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='jugadores',
            name='id',
            field=models.CharField(max_length=4, serialize=False, primary_key=True),
        ),
    ]
