# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-09 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0067_auto_20170608_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='cutoutjob',
            name='cjb_label_colors',
            field=models.CharField(blank=True, max_length=7, null=True, verbose_name='Label Colors'),
        ),
    ]
