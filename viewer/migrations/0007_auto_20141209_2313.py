# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0006_newdiscover_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ignorelink',
            old_name='url',
            new_name='page',
        ),
        migrations.RenameField(
            model_name='visitedlink',
            old_name='url',
            new_name='page',
        ),
        migrations.AddField(
            model_name='visitedlink',
            name='img_link',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
