# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-27 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0011_newspage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='image',
            field=models.ImageField(default='image field', upload_to='media/'),
        ),
    ]