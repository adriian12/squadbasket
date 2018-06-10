# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0072_plantilla_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoria', models.CharField(max_length=25)),
                ('total', models.CharField(max_length=15)),
                ('complemento_uno', models.CharField(max_length=35, verbose_name='Complemento')),
                ('complemento_dos', models.CharField(max_length=35, verbose_name='Complemento', blank=True)),
                ('complemento_tres', models.CharField(max_length=35, verbose_name='Complemento', blank=True)),
                ('complemento_cuatro', models.CharField(max_length=35, verbose_name='Complemento', blank=True)),
                ('complemento_cinco', models.CharField(max_length=35, verbose_name='Complemento', blank=True)),
                ('url', models.CharField(max_length=100, blank=True)),
            ],
        ),
    ]
