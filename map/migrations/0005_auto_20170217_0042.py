# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 00:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_populate_slugs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='isga_short_answer',
        ),
        migrations.RemoveField(
            model_name='city',
            name='office_civic_engagement_immigrant_affairs',
        ),
        migrations.RemoveField(
            model_name='city',
            name='office_civic_engagement_immigrant_affairs_short_answer',
        ),
    ]
