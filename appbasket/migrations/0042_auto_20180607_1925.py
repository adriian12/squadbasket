# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0041_auto_20180607_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeriaequipo',
            name='enlace',
            field=models.TextField(max_length=50),
        ),
    ]
