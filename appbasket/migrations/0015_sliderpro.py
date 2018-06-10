# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0014_auto_20180605_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderPro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(upload_to=b'uploads/slider')),
            ],
        ),
    ]
