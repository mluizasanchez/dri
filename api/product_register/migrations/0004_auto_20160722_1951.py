# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-22 19:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_register', '0003_auto_20160722_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='sti_url',
            field=models.URLField(blank=True, null=True, verbose_name='Url'),
        ),
        migrations.AlterField(
            model_name='externalprocess',
            name='epr_site',
            field=models.ForeignKey(default=None, help_text='origin of the process. instance from which it was imported.', on_delete=django.db.models.deletion.CASCADE, to='product_register.Site', verbose_name='Site'),
        ),
    ]
