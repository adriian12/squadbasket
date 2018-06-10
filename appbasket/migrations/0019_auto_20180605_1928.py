# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0018_columnas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='columnas',
            name='texto',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='columnas',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='texto',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
    ]
