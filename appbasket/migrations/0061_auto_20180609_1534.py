# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0060_auto_20180609_1532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jugadores',
            old_name='numero',
            new_name='dorsal',
        ),
    ]
