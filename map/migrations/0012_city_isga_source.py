# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0011_auto_20170403_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='isga_source',
            field=models.URLField(blank=True, null=True),
        ),
    ]