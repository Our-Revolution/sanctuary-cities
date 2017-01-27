from django.contrib.gis import admin
from .models import State, City


@admin.register(City)
class CityAdmin(admin.OSMGeoAdmin):
    list_display = ['name']


@admin.register(State)
class StateAdmin(admin.OSMGeoAdmin):
    list_display = ['name']