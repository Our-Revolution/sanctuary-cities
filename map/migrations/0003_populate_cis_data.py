# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import migrations
import csv, re, requests


def populate_cis_data(apps, schema_editor):

    City = apps.get_model('map', 'City')
    County = apps.get_model('map', 'County')
    State = apps.get_model('map', 'State')

    sheet_url = "https://docs.google.com/spreadsheets/d/1x474rAr1cblv3T-b6_AQZNpkAzQkXspqLPcy2QJrbv4/export?format=csv"
    response = requests.get(sheet_url).text

    fields = [re.sub(r'\W+', '_', field.lower()) for field in response.split("\r\n")[1].split(",")]

    reader = csv.DictReader(response.split("\r\n")[2:], fields)

    for line in reader:

        if 'County' in line['location_']:
            try:
                territory = County.objects.get(name=line['location_'].replace(' County', ''), state=State.objects.get(name=line['state']))
            except County.DoesNotExist:
                print "Could not find %s, %s; continuing" % (line['location_'], line['state'])
                continue
            except State.DoesNotExist:
                print "Could not find %s; continuing" % (line['state'])
                continue

            if line['policy_'] == 'N/A':
                territory.jails_honor_ice_detainers = 'yes-in-practice'
                territory.jails_honor_ice_detainers_short_answer = " ".join([line['criteria_for_honoring_detainer_'], line['source_'] if line['source_'] else ''])
            else:
                territory.jails_honor_ice_detainers = 'yes-by-law'
                territory.jails_honor_ice_detainers_short_answer = " ".join([line['policy_'], line['criteria_for_honoring_detainer_'], ("Enacted %s" % line['date_enacted_']) if line['date_enacted_'] else '', line['source_'] if line['source_'] else ''])

        elif line['location_'] == 'n/a':

            try:
                territory, created = State.objects.get_or_create(name=line['state'])
            except State.DoesNotExist:
                print "Could not find %s; continuing" % (line['state'])
                continue

            if line['policy_'] == 'N/A':
                territory.limited_ice_cooperation = 'yes-in-practice'
                territory.limited_ice_cooperation_short_answer = " ".join([line['criteria_for_honoring_detainer_'], line['source_'] if line['source_'] else ''])
            else:
                territory.limited_ice_cooperation = 'yes-by-law'
                territory.limited_ice_cooperation_short_answer = " ".join([line['policy_'], line['criteria_for_honoring_detainer_'], ("Enacted %s" % line['date_enacted_']) if line['date_enacted_'] else '', line['source_'] if line['source_'] else ''])

        else:

            try:
                territory, created = City.objects.get_or_create(name=line['location_'], state=State.objects.get(name=line['state']))
            except State.DoesNotExist:
                print "Could not find %s; continuing" % (line['state'])
                continue

            if line['policy_'] == 'N/A':
                territory.limited_ice_cooperation = 'yes-in-practice'
                territory.limited_ice_cooperation_short_answer = " ".join([line['criteria_for_honoring_detainer_'], line['source_'] if line['source_'] else ''])
            else:
                territory.limited_ice_cooperation = 'yes-by-law'
                territory.limited_ice_cooperation_short_answer = " ".join([line['policy_'], line['criteria_for_honoring_detainer_'], ("Enacted %s" % line['date_enacted_']) if line['date_enacted_'] else '', line['source_'] if line['source_'] else ''])

        territory.save()





class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20170206_2337'),
    ]

    operations = [
        migrations.RunPython(populate_cis_data)
    ]
