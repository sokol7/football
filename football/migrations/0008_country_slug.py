# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-25 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0007_auto_20180724_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='slug',
            field=models.SlugField(blank=True, max_length=40),
        ),
    ]
