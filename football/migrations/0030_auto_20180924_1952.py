# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-24 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0029_auto_20180903_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
