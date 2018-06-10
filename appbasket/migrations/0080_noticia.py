# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appbasket', '0079_auto_20180610_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('titulo', models.CharField(max_length=50)),
                ('texto', models.TextField(max_length=400)),
                ('completo', models.TextField(max_length=1000)),
                ('imagen', models.ImageField(upload_to=b'noticias')),
                ('codigo', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('creada', models.DateTimeField(default=django.utils.timezone.now)),
                ('publicada', models.DateTimeField(null=True, blank=True)),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
