# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 05:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0015_city_participate_287g_program_short_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
