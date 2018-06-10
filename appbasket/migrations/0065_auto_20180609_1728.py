# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0064_auto_20180609_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugadores',
            name='imagen',
            field=models.ImageField(default=b'plantilla/default.jpeg', upload_to=b'plantilla/', blank=True),
        ),
    ]
