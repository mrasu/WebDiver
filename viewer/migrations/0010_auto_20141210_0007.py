# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0009_visitedlink_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitedlink',
            name='name',
            field=models.CharField(null=True, max_length=1000),
            preserve_default=True,
        ),
    ]
