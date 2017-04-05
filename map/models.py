from __future__ import unicode_literals
from django.contrib.gis.db import models
from django.contrib.gis.geos import MultiPolygon
from .mapping import URLToDataSource
from .fields import CachedMultiPolygonField


class BaseTerritory(models.Model):
    POLICY_CHOICES = (
            (None, ''),
            ('yes-by-law', 'Yes, by Law'),
            ('yes-by-practice', 'Yes, by Practice'),
            ('no', 'No')
        )
    name = models.CharField(max_length=128)
    geom = models.MultiPolygonField(blank=True, null=True, srid=4326)
    geom_cached = CachedMultiPolygonField(field_name='geom', simplify=0.0007, precision=3)
    slug = models.SlugField(null=True, blank=True, max_length=128)

    class Meta:
        abstract = True
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class FipsTerritory(BaseTerritory):
    fips = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True


class State(FipsTerritory):
    LIMITED_ICE_COOPERATION_CHOICES = (
            ('yes-by-law', 'Yes, by law'),
            ('yes-in-practice', 'Yes, in practice (informal)'),
            ('unlimited', 'Mark if there is unlimited ICE cooperation'),
            (None, 'Information N/A')
        )
    limited_ice_cooperation = models.CharField(max_length=128, null=True, blank=True, choices=LIMITED_ICE_COOPERATION_CHOICES)
    limited_ice_cooperation_short_answer = models.TextField(null=True, blank=True)
    ice_contracts = models.NullBooleanField()
    ice_contracts_short_answer = models.TextField(null=True, blank=True)
    isga = models.NullBooleanField()
    isga_short_answer = models.TextField(null=True, blank=True)
    provide_legal_representation = models.NullBooleanField()
    provide_legal_representation_short_answer = models.TextField(null=True, blank=True)
    drivers_license = models.NullBooleanField()
    drivers_license_short_answer = models.TextField(null=True, blank=True)
    in_state_tuition = models.NullBooleanField()
    in_state_tuition_short_answer = models.TextField(null=True, blank=True)
    barrier = models.NullBooleanField()
    barrier_short_answer = models.TextField(null=True, blank=True)
    policies_against_profiling = models.NullBooleanField()
    policies_against_profiling_short_answer = models.TextField(null=True, blank=True)
    other_policies_and_services = models.TextField(null=True, blank=True)
    local_effort = models.NullBooleanField()
    resources = models.TextField(null=True, blank=True)
    local_effort_link = models.URLField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)


class County(FipsTerritory):
    LIMITED_ICE_COOPERATION_CHOICES = (
            ('yes-by-law', 'Yes, by law'),
            ('yes-in-practice', 'Yes, in practice (informal)'),
            ('unlimited', 'Mark if there is unlimited ICE cooperation'),
            (None, 'Information N/A')
        )
    state = models.ForeignKey(State)
    jails_honor_ice_detainers = models.CharField(max_length=128, null=True, blank=True, choices=LIMITED_ICE_COOPERATION_CHOICES)
    jails_honor_ice_detainers_short_answer = models.TextField(null=True, blank=True)
    jails_prohibit_inquiries = models.NullBooleanField()
    jails_prohibit_inquiries_short_answer = models.TextField(null=True, blank=True)
    ice_contracts = models.NullBooleanField()
    ice_contracts_short_answer = models.TextField(null=True, blank=True)
    isga = models.NullBooleanField()
    isga_short_answer = models.TextField(null=True, blank=True)
    preventing_policies = models.NullBooleanField()
    preventing_policies_short_answer = models.TextField(null=True, blank=True)
    permitting_policies = models.NullBooleanField()
    permitting_policies_short_answer = models.TextField(null=True, blank=True)
    other_policies_and_services = models.TextField(null=True, blank=True)
    local_effort = models.NullBooleanField()
    resources = models.TextField(null=True, blank=True)
    local_effort_link = models.URLField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)


class City(BaseTerritory):
    LIMITED_ICE_COOPERATION_CHOICES = (
            ('yes-by-law', 'Yes, by law'),
            ('yes-in-practice', 'Yes, in practice (informal)'),
            ('unlimited', 'Mark if there is unlimited ICE cooperation'),
            (None, 'Information N/A')
        )
    state = models.ForeignKey(State)
    limited_ice_cooperation = models.CharField(max_length=128, null=True, blank=True, choices=LIMITED_ICE_COOPERATION_CHOICES)
    limited_ice_cooperation_short_answer = models.TextField(null=True, blank=True)
    limited_ice_cooperation_source = models.URLField(null=True, blank=True)
    jails_honor_ice_detainers = models.NullBooleanField()
    jails_honor_ice_detainers_short_answer = models.TextField(null=True, blank=True)
    jails_honor_ice_detainers_source = models.URLField(null=True, blank=True)
    participate_287g_program = models.NullBooleanField()
    participate_287g_program_short_answer = models.TextField(null=True, blank=True)
    participate_287g_program_source = models.URLField(null=True, blank=True)
    provide_legal_representation = models.NullBooleanField()
    provide_legal_representation_short_answer = models.TextField(null=True, blank=True)
    provide_legal_representation_source = models.URLField(null=True, blank=True)
    city_services = models.NullBooleanField()
    city_services_short_answer = models.TextField(null=True, blank=True)
    city_services_source = models.URLField(null=True, blank=True)
    separate_form_of_id = models.NullBooleanField()
    separate_form_of_id_short_answer = models.TextField(null=True, blank=True)
    separate_form_of_id_source = models.URLField(null=True, blank=True)
    police_use_body_cameras = models.NullBooleanField()
    police_use_body_cameras_short_answer = models.TextField(null=True, blank=True)
    police_use_body_cameras_source = models.URLField(null=True, blank=True)
    other_policies_and_services = models.TextField(null=True, blank=True)
    other_policies_short_answer = models.TextField(null=True, blank=True)
    other_policies_source = models.URLField(null=True, blank=True)
    local_effort = models.NullBooleanField()
    local_effort_short_answer = models.TextField(null=True, blank=True)
    local_effort_link = models.URLField(null=True, blank=True)
    resources = models.TextField(null=True, blank=True)
    isga = models.NullBooleanField()
    isga_source = models.URLField(null=True, blank=True)
    political_landscape = models.TextField(null=True, blank=True)
    city_council_contact_info = models.TextField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):

        if not self.geom and self.state:

            try:
                state_data_source = URLToDataSource(url='https://www2.census.gov/geo/tiger/TIGER2015/PLACE/tl_2015_%s_place.zip' % str(self.state.fips).zfill(2)).process()

                geos = None

                for feature in state_data_source:

                    try:
                        if str(feature['NAME']) == self.name:
                            geos = feature.geom.geos
                    except UnicodeEncodeError:
                        pass

                if geos:
                    if not isinstance(geos, MultiPolygon):
                        geos = MultiPolygon(geos)
                    self.geom = geos

            except:
                pass
        
        return super(City, self).save(*args, **kwargs)



    class Meta:
        verbose_name_plural = 'Cities'
