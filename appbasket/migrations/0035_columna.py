# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0034_delete_columna'),
    ]

    operations = [
        migrations.CreateModel(
            name='Columna',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('texto', models.TextField(max_length=200)),
                ('icono', models.TextField(max_length=50)),
            ],
        ),
    ]
