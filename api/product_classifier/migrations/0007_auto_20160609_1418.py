# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-09 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_classifier', '0006_contentcategory_productclasscontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='productclasscontent',
            name='pcc_unit',
            field=models.CharField(blank=True, help_text='Content Unit e.g. name=ra unit=deg.', max_length=128, null=True, verbose_name='Unit'),
        ),
        migrations.AlterField(
            model_name='productclasscontent',
            name='pcc_display_name',
            field=models.CharField(blank=True, help_text='Display Name of the content.', max_length=128, null=True, verbose_name='Display Name'),
        ),
        migrations.AlterField(
            model_name='productclasscontent',
            name='pcc_reference',
            field=models.CharField(blank=True, help_text='Column Reference e.g. name=ra unit=dec reference=J2000.', max_length=128, null=True, verbose_name='Reference'),
        ),
        migrations.AlterField(
            model_name='productclasscontent',
            name='pcc_ucd',
            field=models.CharField(blank=True, help_text='The standard unified content descriptor.', max_length=128, null=True, verbose_name='UCD'),
        ),
    ]
