# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-04-20 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0044_remove_productcontentassociation_pca_setting'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcontent',
            name='pcn_ucd',
            field=models.CharField(blank=True, help_text='The standard unified content descriptor.', max_length=128, null=True, verbose_name='UCD'),
        ),
    ]
