# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-26 20:30
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('coadd', '0025_auto_20160915_1437'),
        ('product_register', '0009_auto_20160915_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessRelease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_register.ExternalProcess')),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coadd.Release')),
            ],
        ),
        migrations.AddField(
            model_name='externalprocess',
            name='releases',
            field=models.ManyToManyField(default=None, through='product_register.ProcessRelease', to='coadd.Release',
                                         verbose_name='Releases'),
        ),
    ]