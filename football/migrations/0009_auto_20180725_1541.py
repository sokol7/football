# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-25 12:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0008_country_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='slug',
            new_name='country_slug_name',
        ),
    ]
