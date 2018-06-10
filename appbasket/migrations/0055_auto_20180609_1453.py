# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0054_delete_plantilla'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeriaequipo',
            name='categoria',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='galeriaequipo',
            name='id',
            field=models.CharField(max_length=25, serialize=False, primary_key=True),
        ),
    ]
