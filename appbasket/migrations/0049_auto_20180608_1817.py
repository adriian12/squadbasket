# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0048_auto_20180608_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubinfo',
            name='descripcion',
            field=models.TextField(max_length=550),
        ),
        migrations.AlterField(
            model_name='clubinfo',
            name='que_hacemos',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='cluborg',
            name='id',
            field=models.CharField(max_length=25, serialize=False, primary_key=True),
        ),
    ]
