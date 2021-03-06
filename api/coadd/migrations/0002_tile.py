# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-07 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coadd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tli_tilename', models.CharField(max_length=20, unique=True, verbose_name='Tilename')),
                ('tli_project', models.CharField(blank=True, max_length=80, null=True, verbose_name='Project')),
                ('tli_ra', models.FloatField(blank=True, null=True, verbose_name='RA')),
                ('tli_dec', models.FloatField(blank=True, null=True, verbose_name='Dec')),
                ('tli_equinox', models.FloatField(blank=True, null=True, verbose_name='equinox')),
                ('tli_pixelsize', models.FloatField(blank=True, null=True, verbose_name='pixelsize')),
                ('tli_npix_ra', models.SmallIntegerField(blank=True, null=True, verbose_name='npix_ra')),
                ('tli_npix_dec', models.SmallIntegerField(blank=True, null=True, verbose_name='npix_dec')),
                ('tli_rall', models.FloatField(blank=True, null=True, verbose_name='rall')),
                ('tli_decll', models.FloatField(blank=True, null=True, verbose_name='decll')),
                ('tli_raul', models.FloatField(blank=True, null=True, verbose_name='raul')),
                ('tli_decul', models.FloatField(blank=True, null=True, verbose_name='decul')),
                ('tli_raur', models.FloatField(blank=True, null=True, verbose_name='raur')),
                ('tli_decur', models.FloatField(blank=True, null=True, verbose_name='decur')),
                ('tli_ralr', models.FloatField(blank=True, null=True, verbose_name='ralr')),
                ('tli_declr', models.FloatField(blank=True, null=True, verbose_name='declr')),
                ('tli_urall', models.FloatField(blank=True, null=True, verbose_name='urall')),
                ('tli_udecll', models.FloatField(blank=True, null=True, verbose_name='udecll')),
                ('tli_uraur', models.FloatField(blank=True, null=True, verbose_name='uraur')),
                ('tli_udecur', models.FloatField(blank=True, null=True, verbose_name='udecur')),
            ],
        ),
    ]
