# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-06 00:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0025_auto_20170406_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='other_policies_and_services_short_answer',
        ),
    ]