# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0050_auto_20180608_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directiva',
            name='id',
            field=models.CharField(max_length=25, serialize=False, primary_key=True),
        ),
    ]
