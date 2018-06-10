# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0076_auto_20180610_1803'),
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
