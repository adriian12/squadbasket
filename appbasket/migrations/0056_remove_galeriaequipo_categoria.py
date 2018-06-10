# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0055_auto_20180609_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galeriaequipo',
            name='categoria',
        ),
    ]
