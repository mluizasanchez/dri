# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-05 19:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfaces', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='app_icon',
        ),
        migrations.RemoveField(
            model_name='application',
            name='app_thumbnail',
        ),
    ]
