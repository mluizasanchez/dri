# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-05-25 17:03
from __future__ import unicode_literals

import current_user
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('coadd', '0027_auto_20170524_1519'),
        ('common', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pst_ra', models.FloatField(verbose_name='RA (deg)')),
                ('pst_dec', models.FloatField(verbose_name='Dec (deg)')),
                ('pst_date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('pst_comment', models.CharField(max_length=2048, verbose_name='Comment')),
                ('owner',
                 models.ForeignKey(default=current_user.get_current_user, on_delete=django.db.models.deletion.CASCADE,
                                   to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
                ('pst_dataset',
                 models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE,
                                   to='coadd.Dataset', verbose_name='Dataset')),
                ('pst_filter',
                 models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE,
                                   to='common.Filter', verbose_name='Filter')),
            ],
        ),
    ]
