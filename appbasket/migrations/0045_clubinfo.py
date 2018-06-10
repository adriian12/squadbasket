# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0044_auto_20180607_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to=b'club')),
                ('descripcion', models.TextField(max_length=500)),
                ('que_hacemos', models.TextField(max_length=300)),
                ('tit_organizacion', models.CharField(max_length=50)),
                ('organizacion', models.TextField(max_length=300, blank=True)),
            ],
        ),
    ]
