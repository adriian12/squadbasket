# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0047_auto_20180608_1420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cluborg',
            old_name='organizacion',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='cluborg',
            old_name='titulo_organizacion',
            new_name='titulo',
        ),
    ]
