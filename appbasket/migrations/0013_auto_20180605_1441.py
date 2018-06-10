# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appbasket', '0012_auto_20180605_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('texto', models.TextField(max_length=80)),
                ('creada', models.DateTimeField(default=django.utils.timezone.now)),
                ('imagen', models.ImageField(upload_to=b'uploads/logo')),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='noticias',
            name='texto',
            field=models.TextField(max_length=80),
        ),
        migrations.AlterField(
            model_name='slider',
            name='imagen',
            field=models.ImageField(upload_to=b'uploads/slider'),
        ),
    ]
