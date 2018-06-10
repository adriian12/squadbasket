# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0082_noticia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizacion',
            name='descripcion',
            field=models.TextField(max_length=300, blank=True),
        ),
    ]
