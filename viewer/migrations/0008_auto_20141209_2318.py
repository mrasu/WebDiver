# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0007_auto_20141209_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitedlink',
            name='img_link',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
