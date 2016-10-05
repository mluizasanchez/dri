# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-30 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_auto_20160930_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='tbl_database',
            field=models.CharField(blank=True, help_text='Database identifier in settings', max_length=128, null=True, verbose_name='Database'),
        ),
    ]
