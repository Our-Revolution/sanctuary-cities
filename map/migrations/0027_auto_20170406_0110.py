# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-06 01:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0026_remove_state_other_policies_and_services_short_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='local_effort_cta_text',
            field=models.CharField(blank=True, max_length=22, null=True),
        ),
        migrations.AddField(
            model_name='county',
            name='local_effort_cta_text',
            field=models.CharField(blank=True, max_length=22, null=True),
        ),
        migrations.AddField(
            model_name='state',
            name='local_effort_cta_text',
            field=models.CharField(blank=True, max_length=22, null=True),
        ),
    ]
