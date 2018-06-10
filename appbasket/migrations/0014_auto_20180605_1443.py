# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0013_auto_20180605_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='autor',
        ),
        migrations.DeleteModel(
            name='Home',
        ),
    ]
