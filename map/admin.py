from django.contrib.gis import admin
from django.contrib.gis.geos import MultiPolygon
from django.db import models
from django.forms.widgets import Textarea
from .forms import CityForm, CountyForm, StateForm
from .mapping import UploadToDataSource
from .models import State, City, County



@admin.register(City)
class CityAdmin(admin.OSMGeoAdmin):
    list_display = ['name']
    fieldsets = (
            (None, {
                'fields': ('name', 'slug', 'state', 'limited_ice_cooperation', 'limited_ice_cooperation_short_answer',
                            'jails_honor_ice_detainers', 'jails_honor_ice_detainers_short_answer',
                            'participate_287g_program', 'participate_287g_program_short_answer',
                            'provide_legal_representation', 'provide_legal_representation_short_answer',
                            'city_services', 'city_services_short_answer', 'separate_form_of_id',
                            'separate_form_of_id_short_answer', 'police_use_body_cameras',
                            'police_use_body_cameras_short_answer',
                            'local_effort', 'local_effort_short_answer', 'isga') }),
            ('Advanced options', {
                'classes': ('collapse',),
                'fields': ('geom', 'shapefile', 'shapefile_url',),
            }),
        )
    form = CityForm
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':60})},
    }
    prepopulated_fields = {"slug": ("name",)}


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
    fieldsets = (
            (None, {
                'fields': ('name', 'slug', 'limited_ice_cooperation', 'limited_ice_cooperation_short_answer',
                            'ice_contracts', 'ice_contracts_short_answer', 'igsa', 'igsa_short_answer',
                            'provide_legal_representation', 'provide_legal_representation_short_answer',
                            'drivers_license', 'drivers_license_short_answer', 'in_state_tuition', 'in_state_tuition_short_answer',
                            'barrier', 'barrier_short_answer', 'policies_against_profiling_short_answer', 'other_policies_and_services',
                            'other_policies_and_services_short_answer', 'local_effort', 'local_effort_short_answer') }),
            ('Advanced options', {
                'classes': ('collapse',),
                'fields': ('geom', 'shapefile', 'shapefile_url',),
            }),
        )
    form = StateForm
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':60})},
    }
    prepopulated_fields = {"slug": ("name",)}


    def get_queryset(self, request):
        return super(StateAdmin, self).get_queryset(request).defer('geom')


@admin.register(County)
class CountyAdmin(admin.OSMGeoAdmin):
    list_display = ['name', 'state']
    list_select_related = ['state']
    list_filter = ['state__name']
    search_fields = ['name']
    fieldsets = (
            (None, {
                'fields': ('name', 'slug', 'jails_honor_ice_detainers',
                        'jails_honor_ice_detainers_short_answer', 'jails_prohibit_inquiries',
                        'jails_prohibit_inquiries_short_answer', 'ice_contracts',
                        'ice_contracts_short_answer', 'isga', 'isga_short_answer',
                        'preventing_policies', 'preventing_policies_short_answer',
                        'permitting_policies', 'permitting_policies_short_answer',
                        'other_policies_and_services',) }),
            ('Advanced options', {
                'classes': ('collapse',),
                'fields': ('geom', 'shapefile', 'shapefile_url',),
            }),
        )
    form = CountyForm
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':60})},
    }
    prepopulated_fields = {"slug": ("name",)}

    
    def get_queryset(self, request):
        return super(CountyAdmin, self).get_queryset(request).select_related('state').defer('geom', 'state__geom')
