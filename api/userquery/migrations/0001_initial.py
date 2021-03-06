# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-03-02 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=128, verbose_name='Owner')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Description')),
                ('query', models.CharField(blank=True, max_length=1024, verbose_name='Query')),
                ('creationdate', models.DateTimeField(auto_now_add=True, help_text='Creation Date', null=True, verbose_name='Date')),
                ('tablename', models.CharField(blank=True, max_length=128, verbose_name='Table Name')),
            ],
        ),
    ]
