# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0031_auto_20180607_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='directiva',
            name='tabla',
            field=models.TextField(default=b'', max_length=1024, null=True, blank=True),
        ),
    ]
