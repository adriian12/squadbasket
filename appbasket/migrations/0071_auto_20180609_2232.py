# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0070_auto_20180609_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directiva',
            name='tabla',
            field=models.TextField(null=True, blank=True),
        ),
    ]
