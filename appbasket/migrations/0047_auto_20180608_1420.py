# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0046_auto_20180608_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubOrg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo_organizacion', models.CharField(max_length=50)),
                ('organizacion', models.TextField(max_length=300, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='clubinfo',
            name='organizacion',
        ),
        migrations.RemoveField(
            model_name='clubinfo',
            name='titulo_organizacion',
        ),
    ]
