# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0002_auto_20180604_1413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticia',
            old_name='created_date',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='noticia',
            old_name='published_date',
            new_name='publicar',
        ),
        migrations.RenameField(
            model_name='noticia',
            old_name='text',
            new_name='texto',
        ),
        migrations.RenameField(
            model_name='noticia',
            old_name='title',
            new_name='titulo',
        ),
    ]
