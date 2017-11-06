# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-11-06 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0006_auto_20171102_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marketing',
            name='title_block',
        ),
        migrations.AlterField(
            model_name='marketing',
            name='header_bg',
            field=models.FilePathField(blank=True, null=True, path='/Users/suche010/Documents/Projects/dexalytics.com/static/images/marketing', verbose_name='Header Background Image'),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='socials',
            field=models.BooleanField(default=False, verbose_name='Social Icons?'),
        ),
    ]
