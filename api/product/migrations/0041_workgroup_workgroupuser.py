# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-31 13:19
from __future__ import unicode_literals

import current_user
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0040_auto_20170127_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workgroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wgp_workgroup', models.CharField(help_text="group's name", max_length=60, verbose_name='Workgroup')),
                ('owner', models.ForeignKey(default=current_user.get_current_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
        ),
        migrations.CreateModel(
            name='WorkgroupUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wgu_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('wgu_workgroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Workgroup', verbose_name='Workgroup')),
            ],
        ),
    ]
