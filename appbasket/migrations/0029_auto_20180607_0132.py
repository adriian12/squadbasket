# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appbasket', '0028_recientes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('texto', models.TextField(max_length=400)),
                ('creada', models.DateTimeField(default=django.utils.timezone.now)),
                ('publicada', models.DateTimeField(null=True, blank=True)),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=30)),
                ('texto', models.TextField(max_length=300)),
                ('imagen', models.ImageField(upload_to=b'noticias')),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='Columnas',
            new_name='Columna',
        ),
        migrations.RemoveField(
            model_name='noticias',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='recientes',
            name='autor',
        ),
        migrations.DeleteModel(
            name='Noticias',
        ),
        migrations.DeleteModel(
            name='Recientes',
        ),
    ]
