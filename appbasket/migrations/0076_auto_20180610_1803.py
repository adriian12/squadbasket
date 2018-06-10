# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0075_auto_20180610_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizacion',
            fields=[
                ('titulo', models.CharField(max_length=50)),
                ('id', models.CharField(max_length=25, serialize=False, primary_key=True)),
                ('descripcion', models.TextField(default=b'org', max_length=300, blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ClubOrg',
        ),
    ]
