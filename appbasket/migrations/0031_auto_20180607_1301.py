# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0030_auto_20180607_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directiva',
            name='puesto',
            field=models.CharField(max_length=30),
        ),
    ]
