# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-03 16:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0028_auto_20180903_1939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_id',
            new_name='father_comment',
        ),
    ]