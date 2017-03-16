from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import City, County, State


class CitySerializer(GeoFeatureModelSerializer):
    model = serializers.SerializerMethodField()

    def get_model(self, obj):
        return 'map.city'

    class Meta:
        model = City
        fields = ('model', 'name', 'slug', 'limited_ice_cooperation', 'limited_ice_cooperation_short_answer',
                'jails_honor_ice_detainers', 'jails_honor_ice_detainers_short_answer',
                'participate_287g_program', 'participate_287g_program_short_answer',
                'provide_legal_representation', 'provide_legal_representation_short_answer',
                'city_services', 'city_services_short_answer', 'separate_form_of_id',
                'separate_form_of_id_short_answer', 'police_use_body_cameras',
                'police_use_body_cameras_short_answer', 'other_policies_and_services',
                'local_effort', 'local_effort_short_answer', 'isga', 'political_landscape', 'city_council_contact_info')
        geo_field = 'geom_cached'


class CountySerializer(GeoFeatureModelSerializer):
    model = serializers.SerializerMethodField()

    def get_model(self, obj):
        return 'map.county'

    class Meta:
        model = County
        fields = ('model', 'name', 'slug', 'jails_honor_ice_detainers', 'jails_honor_ice_detainers_short_answer',
                    'jails_prohibit_inquiries', 'jails_prohibit_inquiries_short_answer',
                    'ice_contracts', 'ice_contracts_short_answer', 'isga',
                    'isga_short_answer', 'preventing_policies',
                    'preventing_policies_short_answer', 'permitting_policies',
                    'permitting_policies_short_answer', 'other_policies_and_services')
        geo_field = 'geom_cached'


class StateSerializer(GeoFeatureModelSerializer):
    model = serializers.SerializerMethodField()

    def get_model(self, obj):
        return 'map.state'

    class Meta:
        model = State
        fields = ('model', 'name', 'slug', 'limited_ice_cooperation', 'limited_ice_cooperation_short_answer',
                    'ice_contracts', 'ice_contracts_short_answer', 'isga', 'isga_short_answer',
                    'provide_legal_representation', 'provide_legal_representation_short_answer',
                    'drivers_license', 'drivers_license_short_answer', 'in_state_tuition',
                    'in_state_tuition_short_answer', 'barrier', 'barrier_short_answer',
                    'policies_against_profiling', 'policies_against_profiling_short_answer',
                    'other_policies_and_services', 'local_effort', 'local_effort_short_answer')
        geo_field = 'geom_cached'