# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0021_auto_20170405_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='local_effort_short_answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='other_policies_source',
            field=models.URLField(blank=True, null=True),
        ),
    ]
