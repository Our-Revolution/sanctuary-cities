# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_populate_slugs'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='local_effort',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='city',
            name='local_effort_short_answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='police_use_body_cameras',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='city',
            name='police_use_body_cameras_short_answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='policies_against_profiling',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='city',
            name='policies_against_profiling_short_answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='political_landscape',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='state',
            name='local_effort',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='state',
            name='local_effort_short_answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='state',
            name='policies_against_profiling',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='state',
            name='policies_against_profiling_short_answer',
            field=models.TextField(blank=True, null=True),
        ),
    ]