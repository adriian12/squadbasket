# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0085_auto_20180610_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reciente',
            name='autor',
        ),
        migrations.DeleteModel(
            name='Reciente',
        ),
    ]
