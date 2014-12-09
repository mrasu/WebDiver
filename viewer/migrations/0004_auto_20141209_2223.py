# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0003_webpage_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ignorelink',
            name='id',
            field=models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newdiscover',
            name='id',
            field=models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newdiscoverlink',
            name='id',
            field=models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visitedlink',
            name='id',
            field=models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='webpage',
            name='id',
            field=models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
