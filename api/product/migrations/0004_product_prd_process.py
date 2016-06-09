# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-06 20:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_register', '0001_initial'),
        ('product', '0003_auto_20160405_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prd_process',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='product_register.ExternalProcess', verbose_name='External Process'),
            preserve_default=False,
        ),
    ]
