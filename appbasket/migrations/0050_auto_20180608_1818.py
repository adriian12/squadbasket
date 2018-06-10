# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0049_auto_20180608_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluborg',
            name='descripcion',
            field=models.TextField(default=b'org', max_length=300, blank=True),
        ),
    ]
