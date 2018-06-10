# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0086_auto_20180610_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='completo',
            field=models.TextField(max_length=1500, blank=True),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
    ]
