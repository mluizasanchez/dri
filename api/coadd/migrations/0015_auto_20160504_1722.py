# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-04 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('coadd', '0014_survey_srv_fov'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='srv_fov',
            field=models.FloatField(blank=True, help_text='Initial Zoom in degrees.', max_length=10, null=True,
                                    verbose_name='FoV'),
        ),
    ]
