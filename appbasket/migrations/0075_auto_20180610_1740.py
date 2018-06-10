# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0074_auto_20180609_2339'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClubInfo',
            new_name='Club',
        ),
    ]
