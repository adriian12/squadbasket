# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0065_auto_20180609_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantilla',
            name='imagen',
            field=models.ImageField(upload_to=b'categorias', blank=True),
        ),
    ]
