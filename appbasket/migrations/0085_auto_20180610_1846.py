# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0084_auto_20180610_1841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticia',
            old_name='categoria',
            new_name='etiqueta',
        ),
    ]
