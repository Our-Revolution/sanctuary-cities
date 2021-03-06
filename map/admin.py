# -*- coding: utf-8 -*-

from django.contrib.gis import admin
from django.contrib.gis.geos import MultiPolygon
from django.db import models
from django.forms.widgets import Textarea
from .forms import CityForm, CountyForm, StateForm
from .mapping import UploadToDataSource
from .models import State, City, County


class HTTPSOSMGeoAdmin(admin.OSMGeoAdmin):
    openlayers_url = 'https://openlayers.org/api/2.13.1/OpenLayers.js'
    wms_url = 'https://vmap0.tiles.osgeo.org/wms/vmap0'
    map_srid = 4326


@admin.register(City)
class CityAdmin(HTTPSOSMGeoAdmin):
    list_display = ['name', 'limited_ice_cooperation_bool', 'jails_honor_ice_detainers_bool',
                        'participate_287g_program_bool', 'provide_legal_representation_bool',
                        'separate_form_of_id_bool', 'police_use_body_cameras_bool',
                        'local_effort_bool', 'isga_bool']
    fieldsets = (
            (None, {
                'fields': ('name', 'slug', 'state', 'limited_ice_cooperation', 
                            'limited_ice_cooperation_short_answer', 'limited_ice_cooperation_source',
                            'jails_honor_ice_detainers', 'jails_honor_ice_detainers_short_answer', 'jails_honor_ice_detainers_source',
                            'participate_287g_program', 'participate_287g_program_short_answer', 'participate_287g_program_source',
                            'provide_legal_representation', 'provide_legal_representation_short_answer', 'provide_legal_representation_source',
                            'city_services', 'city_services_short_answer', 'city_services_source', 'separate_form_of_id', 'separate_form_of_id_short_answer', 'separate_form_of_id_source', 'police_use_body_cameras', 'police_use_body_cameras_short_answer', 'police_use_body_cameras_source',
                            'other_policies_and_services','other_policies_short_answer','other_policies_source','local_effort',
                            'local_effort_short_answer', 'local_effort_link','local_effort_cta_text','resources', 'isga', 'isga_source', 'city_council_contact_info') }),
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

    def limited_ice_cooperation_bool(self, obj):
        return '' if obj.limited_ice_cooperation == None else '✅'
    limited_ice_cooperation_bool.short_description = "ICE Cooperation"

    def jails_honor_ice_detainers_bool(self, obj):
        return '' if obj.jails_honor_ice_detainers == None else '✅'
    jails_honor_ice_detainers_bool.short_description = "ICE Detainers"

    def participate_287g_program_bool(self, obj):
        return '' if obj.participate_287g_program == None else '✅'
    participate_287g_program_bool.short_description = "287G"

    def provide_legal_representation_bool(self, obj):
        return '' if obj.provide_legal_representation == None else '✅'
    provide_legal_representation_bool.short_description = "Legal Rep"

    def separate_form_of_id_bool(self, obj):
        return '' if obj.separate_form_of_id == None else '✅'
    separate_form_of_id_bool.short_description = "Separate ID"

    def police_use_body_cameras_bool(self, obj):
        return '' if obj.police_use_body_cameras == None else '✅'
    police_use_body_cameras_bool.short_description = "Body Cameras"

    def local_effort_bool(self, obj):
        return '' if obj.local_effort == None else '✅'
    local_effort_bool.short_description = "Local"

    def isga_bool(self, obj):
        return '' if obj.isga == None else '✅'
    isga_bool.short_description = "ISGA"


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
class StateAdmin(HTTPSOSMGeoAdmin):
    list_display = ['name']
    fieldsets = (
            (None, {
                'fields': ('name', 'slug', 'limited_ice_cooperation', 
                            'limited_ice_cooperation_short_answer','limited_ice_cooperation_source',
                            'ice_contracts', 'ice_contracts_short_answer', 'ice_contracts_source','isga', 'isga_short_answer','isga_source',
                            'provide_legal_representation', 'provide_legal_representation_short_answer',
                            'provide_legal_representation_source','drivers_license', 'drivers_license_short_answer',
                            'drivers_license_source', 'in_state_tuition', 'in_state_tuition_short_answer','in_state_tuition_source',
                            'barrier', 'barrier_short_answer','barrier_source',
                            'policies_against_profiling', 'policies_against_profiling_short_answer', 'policies_against_profiling_source','other_policies_and_services','other_policies_and_services_source', 'local_effort', 'local_effort_short_answer','local_effort_link','local_effort_cta_text','resources') }),
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


    def save_model(self, request, obj, form, change):
        super(StateAdmin, self).save_model(request, obj, form, change)
        if request.method == 'POST' and (request.FILES.get('shapefile', None) or request.POST.get('shapefile_url', None)):
            data_source = UploadToDataSource(request=request, file_param='shapefile', url_param='shapefile_url').process()
            geos = data_source[0].geom.geos
            if not isinstance(geos, MultiPolygon):
                geos = MultiPolygon(geos)
            obj.geom = geos
            obj.save()


@admin.register(County)
class CountyAdmin(HTTPSOSMGeoAdmin):
    list_display = ['name', 'state']
    list_select_related = ['state']
    list_filter = ['state__name']
    search_fields = ['name']
    fieldsets = (
            (None, {
                'fields': ('name', 'slug', 'jails_honor_ice_detainers',
                        'jails_honor_ice_detainers_short_answer', 'jails_honor_ice_detainers_source','jails_prohibit_inquiries',
                        'jails_prohibit_inquiries_short_answer', 'jails_prohibit_inquiries_source',
                        'ice_contracts', 'ice_contracts_short_answer','ice_contracts_source',
                        'isga', 'isga_short_answer', 'isga_source','preventing_policies', 'preventing_policies_short_answer','preventing_policies_source',
                        'permitting_policies', 'permitting_policies_short_answer','permitting_policies_source',
                        'other_policies_and_services','other_policies_and_source','local_effort',
                        'local_effort_short_answer', 'local_effort_link','local_effort_cta_text','resources') }),
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

    def save_model(self, request, obj, form, change):
        super(CountyAdmin, self).save_model(request, obj, form, change)
        if request.method == 'POST' and (request.FILES.get('shapefile', None) or request.POST.get('shapefile_url', None)):
            data_source = UploadToDataSource(request=request, file_param='shapefile', url_param='shapefile_url').process()
            geos = data_source[0].geom.geos
            if not isinstance(geos, MultiPolygon):
                geos = MultiPolygon(geos)
            obj.geom = geos
            obj.save()