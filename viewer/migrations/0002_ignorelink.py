# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IgnoreLink',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('url', models.ForeignKey(to='viewer.WebPage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
