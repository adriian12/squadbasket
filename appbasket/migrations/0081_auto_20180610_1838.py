# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0080_noticia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='autor',
        ),
        migrations.DeleteModel(
            name='Noticia',
        ),
    ]
