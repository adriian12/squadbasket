# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0020_logoimagen'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LogoImagen',
        ),
    ]
