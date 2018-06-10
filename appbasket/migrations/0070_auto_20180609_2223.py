# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0069_entrenadores_posicion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GaleriaEquipo',
            new_name='Equipo',
        ),
    ]
