# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-05-03 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0051_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cutoutjob',
            name='cjb_status',
            field=models.CharField(choices=[('st', 'Start'), ('bs', 'Submit Job'), ('rn', 'Running'), ('ok', 'Done'), ('er', 'Error'), ('job_error', 'Job Error')], default='st', max_length=2, verbose_name='Status'),
        ),
    ]
