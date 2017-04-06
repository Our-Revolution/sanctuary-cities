# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0010_auto_20170403_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='resources',
        ),
        migrations.AddField(
            model_name='city',
            name='city_services_source',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='jails_honor_ice_detainers_source',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='limited_ice_cooperation_source',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='other_policies_short_answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='participate_287g_program_source',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='police_use_body_cameras_source',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='provide_legal_representation_source',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='separate_form_of_id_source',
            field=models.URLField(blank=True, null=True),
        ),
    ]
