# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-12-15 18:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_register', '0012_auto_20160930_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='export',
            name='exp_external_process',
        ),
        migrations.AlterField(
            model_name='export',
            name='exp_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='export',
            name='exp_username',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='User Name'),
        ),
    ]
