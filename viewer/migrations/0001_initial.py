# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewDiscover',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewDiscoverLink',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('discover', models.ForeignKey(to='viewer.NewDiscover')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VisitedLink',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('link', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WebPage',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='visitedlink',
            name='url',
            field=models.ForeignKey(to='viewer.WebPage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newdiscoverlink',
            name='link',
            field=models.ForeignKey(to='viewer.VisitedLink'),
            preserve_default=True,
        ),
    ]
