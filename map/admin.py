from django.contrib.gis import admin
from django.db import models
from django.forms.widgets import Textarea
from .models import State, City
from .forms import CityForm


@admin.register(City)
class CityAdmin(admin.OSMGeoAdmin):
    list_display = ['name']
    fieldsets = (
            (None, {
                'fields': ('name', 'state', 'limited_ice_cooperation', 'limited_ice_cooperation_short_answer',
                            'jails_honor_ice_detainers', 'jails_honor_ice_detainers_short_answer',
                            'participate_287g_program', 'participate_287g_program_short_answer',
                            'provide_legal_representation', 'provide_legal_representation_short_answer',
                            'city_services', 'city_services_short_answer', 'separate_form_of_id',
                            'separate_form_of_id_short_answer', 'office_civic_engagement_immigrant_affairs',
                            'office_civic_engagement_immigrant_affairs_short_answer', 'other_policies_and_services') }),
            ('Advanced options', {
                'classes': ('collapse',),
                'fields': ('geom',),
            }),
        )
    form = CityForm
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':60})},
    }

    def get_queryset(self, request):
        return super(CityAdmin, self).get_queryset(request).select_related('state').defer('geom', 'state__geom')


@admin.register(State)
class StateAdmin(admin.OSMGeoAdmin):
    list_display = ['name']

    def get_queryset(self, request):
        return super(StateAdmin, self).get_queryset(request).defer('geom')