# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0009_slider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='imagen',
            field=models.ImageField(upload_to=b'img/slides'),
        ),
    ]
