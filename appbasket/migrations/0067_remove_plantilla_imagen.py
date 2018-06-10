# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0066_plantilla_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantilla',
            name='imagen',
        ),
    ]
