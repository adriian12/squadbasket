# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0015_sliderpro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderpro',
            name='imagen',
            field=models.ImageField(upload_to=b''),
        ),
    ]
