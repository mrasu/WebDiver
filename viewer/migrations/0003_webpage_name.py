# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0002_ignorelink'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='name',
            field=models.CharField(max_length=200, default=''),
            preserve_default=False,
        ),
    ]
