# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0013_remove_city_participate_287g_program_source'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='city',
        #     name='participate_287g_program_short_answer',
        # ),
        migrations.AddField(
            model_name='city',
            name='participate_287g_program_source',
            field=models.URLField(blank=True, null=True),
        ),
    ]
