# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 21:36
from __future__ import unicode_literals

from django.db import migrations
import map.fields


def save_geoms(apps, schema_editor):
    City = apps.get_model('map', 'City')
    County = apps.get_model('map', 'County')
    State = apps.get_model('map', 'State')

    for city in City.objects.all():
        city.save()

    for county in County.objects.all():
        county.save()

    for state in State.objects.all():
        state.save()



class Migration(migrations.Migration):

    dependencies = [
        ('map', '0007_city_city_council_contact_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='geom_cached',
            field=map.fields.CachedMultiPolygonField(field_name='geom', precision=3, simplify=0.0007, srid=4326),
        ),
        migrations.AddField(
            model_name='county',
            name='geom_cached',
            field=map.fields.CachedMultiPolygonField(field_name='geom', precision=3, simplify=0.0007, srid=4326),
        ),
        migrations.AddField(
            model_name='state',
            name='geom_cached',
            field=map.fields.CachedMultiPolygonField(field_name='geom', precision=3, simplify=0.0007, srid=4326),
        ),
        migrations.RunPython(save_geoms, reverse_code=migrations.RunPython.noop)
    ]
