# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-11-02 15:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0002_auto_20171101_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketing',
            name='header_bg',
            field=models.FilePathField(blank=True, null=True, path='/Users/saun0063/Workspace/dexalytics.com/static/images/marketing', verbose_name='Header Background Image'),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 2, 15, 52, 41, 911934, tzinfo=utc), verbose_name='Last Update'),
        ),
    ]
