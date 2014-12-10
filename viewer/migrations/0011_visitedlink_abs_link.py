# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0010_auto_20141210_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitedlink',
            name='abs_link',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.RunSQL(
            'UPDATE viewer_visitedlink SET abs_link = link;'
        )
    ]
