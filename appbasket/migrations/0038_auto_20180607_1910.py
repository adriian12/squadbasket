# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0037_auto_20180607_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeriaequipo',
            name='descripcion',
            field=models.TextField(max_length=50),
        ),
    ]
