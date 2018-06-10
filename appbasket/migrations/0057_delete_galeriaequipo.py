# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0056_remove_galeriaequipo_categoria'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GaleriaEquipo',
        ),
    ]
