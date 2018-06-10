# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0007_auto_20180604_1705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticias',
            old_name='author',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='noticias',
            old_name='created_date',
            new_name='creada',
        ),
        migrations.RenameField(
            model_name='noticias',
            old_name='published_date',
            new_name='publicada',
        ),
        migrations.RenameField(
            model_name='noticias',
            old_name='text',
            new_name='texto',
        ),
        migrations.RenameField(
            model_name='noticias',
            old_name='title',
            new_name='titulo',
        ),
    ]
