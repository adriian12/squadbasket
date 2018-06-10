# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0021_delete_logoimagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='columnas',
            old_name='texto',
            new_name='col_texto',
        ),
        migrations.RenameField(
            model_name='columnas',
            old_name='titulo',
            new_name='col_titulo',
        ),
    ]
