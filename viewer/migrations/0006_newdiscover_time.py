# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0005_ignorelink_regex'),
    ]

    operations = [
        migrations.AddField(
            model_name='newdiscover',
            name='time',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
    ]
