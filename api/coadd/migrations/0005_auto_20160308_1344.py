# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 13:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coadd', '0004_remove_tag_tiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag_Tile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.CharField(blank=True, max_length=30, null=True, verbose_name='Run')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coadd.Tag')),
                ('tile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coadd.Tile')),
            ],
        ),
        migrations.AddField(
            model_name='tag',
            name='tiles',
            field=models.ManyToManyField(through='coadd.Tag_Tile', to='coadd.Tile'),
        ),
    ]