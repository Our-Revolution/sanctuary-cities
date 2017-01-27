from django.contrib.gis import admin
from .models import State, City


@admin.register(City)
class CityAdmin(admin.OSMGeoAdmin):
    list_display = ['name']

    def get_queryset(self, request):
        return super(CityAdmin, self).get_queryset(request).select_related('state').defer('geom', 'state__geom')


@admin.register(State)
class StateAdmin(admin.OSMGeoAdmin):
    list_display = ['name']

    def get_queryset(self, request):
        return super(StateAdmin, self).get_queryset(request).defer('geom')