# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0073_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precio',
            name='complemento_uno',
            field=models.CharField(max_length=35, verbose_name='Complemento', blank=True),
        ),
        migrations.AlterField(
            model_name='precio',
            name='total',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='precio',
            name='url',
            field=models.TextField(max_length=150, blank=True),
        ),
    ]
