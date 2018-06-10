# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0063_auto_20180609_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugadores',
            name='imagen',
            field=models.ImageField(default=b'plantilla/jug-default.png', upload_to=b'plantilla/', blank=True),
        ),
    ]
