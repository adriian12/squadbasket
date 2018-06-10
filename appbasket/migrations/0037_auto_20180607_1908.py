# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0036_auto_20180607_1907'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GaleriaEquipos',
            new_name='GaleriaEquipo',
        ),
    ]
