# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-24 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0004_auto_20180723_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='slug',
            field=models.SlugField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newspage',
            name='slug',
            field=models.SlugField(blank=True, max_length=40, unique=True),
        ),
    ]
