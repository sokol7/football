# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-25 14:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0009_auto_20180725_1541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='country_slug_name',
            new_name='slug',
        ),
    ]
