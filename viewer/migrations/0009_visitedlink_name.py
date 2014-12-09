# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0008_auto_20141209_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitedlink',
            name='name',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
