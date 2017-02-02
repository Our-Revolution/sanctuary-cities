from django.contrib.gis import admin
from django.contrib.gis.geos import MultiPolygon
from django.db import models
from django.forms.widgets import Textarea
from .forms import CityForm
from .mapping import UploadToDataSource
from .models import State, City



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
                'fields': ('geom', 'shapefile', 'shapefile_url',),
            }),
        )
    form = CityForm
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':60})},
    }

    def save_model(self, request, obj, form, change):
        super(CityAdmin, self).save_model(request, obj, form, change)
        if request.method == 'POST' and (request.FILES.get('shapefile', None) or request.POST.get('shapefile_url', None)):
            data_source = UploadToDataSource(request=request, file_param='shapefile', url_param='shapefile_url').process()
            geos = data_source[0].geom.geos
            if not isinstance(geos, MultiPolygon):
                geos = MultiPolygon(geos)
            obj.geom = geos
            obj.save()


    def get_queryset(self, request):
        return super(CityAdmin, self).get_queryset(request).select_related('state').defer('geom', 'state__geom')


@admin.register(State)
class StateAdmin(admin.OSMGeoAdmin):
    list_display = ['name']

    def get_queryset(self, request):
        return super(StateAdmin, self).get_queryset(request).defer('geom')