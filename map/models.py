from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models


class BaseTerritory(models.Model):
    POLICY_CHOICES = (
            (None, ''),
            ('yes-by-law', 'Yes, by Law'),
            ('yes-by-practice', 'Yes, by Practice'),
            ('no', 'No')
        )
    name = models.CharField(max_length=128)
    geom = models.MultiPolygonField(blank=True, null=True, srid=4326)


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
    pass


class County(FipsTerritory):
    LIMITED_ICE_COOPERATION_CHOICES = (
            ('yes-by-law', 'Yes, by law'),
            ('yes-in-practice', 'Yes, in practice (informal)'),
            ('unlimited', 'Mark if there is unlimited ICE cooperation'),
            (None, 'Information N/A')
        )
    state = models.ForeignKey(State)
    limited_ice_cooperation = models.CharField(max_length=128, null=True, blank=True, choices=LIMITED_ICE_COOPERATION_CHOICES)
    limited_ice_cooperation_short_answer = models.TextField(null=True, blank=True)


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
    jails_honor_ice_detainers = models.NullBooleanField()
    jails_honor_ice_detainers_short_answer = models.TextField(null=True, blank=True)
    participate_287g_program = models.NullBooleanField()
    participate_287g_program_short_answer = models.TextField(null=True, blank=True)
    provide_legal_representation = models.NullBooleanField()
    provide_legal_representation_short_answer = models.TextField(null=True, blank=True)
    city_services = models.NullBooleanField()
    city_services_short_answer = models.TextField(null=True, blank=True)
    separate_form_of_id = models.NullBooleanField()
    separate_form_of_id_short_answer = models.TextField(null=True, blank=True)
    office_civic_engagement_immigrant_affairs = models.NullBooleanField()
    office_civic_engagement_immigrant_affairs_short_answer = models.TextField(null=True, blank=True)
    other_policies_and_services = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Cities'

