# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0051_auto_20180608_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galeriaequipo',
            name='enlace',
        ),
        migrations.AlterField(
            model_name='galeriaequipo',
            name='id',
            field=models.CharField(max_length=25, serialize=False, primary_key=True),
        ),
    ]
