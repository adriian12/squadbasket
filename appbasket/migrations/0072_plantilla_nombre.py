# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0071_auto_20180609_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantilla',
            name='nombre',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
