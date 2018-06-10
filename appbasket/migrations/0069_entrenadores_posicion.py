# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0068_entrenadores'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrenadores',
            name='posicion',
            field=models.CharField(max_length=15, blank=True),
        ),
    ]
