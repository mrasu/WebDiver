# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0004_auto_20141209_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='ignorelink',
            name='regex',
            field=models.CharField(max_length=100, default=''),
            preserve_default=False,
        ),
    ]
