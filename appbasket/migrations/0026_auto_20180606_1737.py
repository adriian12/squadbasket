# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0025_auto_20180606_1712'),
    ]

    operations = [
        migrations.RenameField(
            model_name='columnas',
            old_name='col_texto',
            new_name='texto',
        ),
        migrations.RenameField(
            model_name='columnas',
            old_name='col_titulo',
            new_name='titulo',
        ),
        migrations.AlterField(
            model_name='slider',
            name='imagen',
            field=models.ImageField(upload_to=b'slides'),
        ),
    ]
