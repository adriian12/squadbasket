# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0029_auto_20180607_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Directiva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('puesto', models.TextField(max_length=30)),
                ('imagen', models.ImageField(upload_to=b'directiva')),
            ],
        ),
        migrations.AlterField(
            model_name='reciente',
            name='titulo',
            field=models.CharField(max_length=40),
        ),
    ]
