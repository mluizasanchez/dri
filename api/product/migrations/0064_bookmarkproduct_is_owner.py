# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-02 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0063_bookmarkproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmarkproduct',
            name='is_owner',
            field=models.BooleanField(default=False, verbose_name='Is Owner'),
        ),
    ]
