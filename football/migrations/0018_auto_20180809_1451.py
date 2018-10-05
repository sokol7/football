# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-09 11:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0017_auto_20180807_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_profile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='football.UserProfile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='profile_images'),
        ),
    ]
