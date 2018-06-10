# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0045_clubinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clubinfo',
            old_name='tit_organizacion',
            new_name='titulo_organizacion',
        ),
    ]
