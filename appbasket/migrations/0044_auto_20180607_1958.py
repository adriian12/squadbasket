# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0043_auto_20180607_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeriaequipo',
            name='descripcion',
            field=models.TextField(max_length=50, blank=True),
        ),
    ]
