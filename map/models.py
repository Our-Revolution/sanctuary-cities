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
    ice_cooperation_limited = models.CharField(choices=POLICY_CHOICES, null=True, blank=True, default=None, max_length=128, verbose_name="Is ICE cooperation limited?")
    ice_cooperation_limited_notes = models.CharField(max_length=2048, null=True, blank=True, verbose_name="If yes, please cite your source.")
    police_policy = models.CharField(choices=POLICY_CHOICES, null=True, blank=True, default=None, max_length=128, verbose_name="Is there policy for when police come into contact witth undocumented immigrants?")
    police_policy_notes = models.CharField(max_length=2048, null=True, blank=True, verbose_name="If yes, what?")
    barriers_to_accessing_services = models.NullBooleanField()
    barriers_to_accessing_services_notes = models.CharField(max_length=2048, null=True, blank=True, verbose_name="If yes, what?")

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class State(BaseTerritory):
    TUITION_CHOICES = (
            ('yes', 'Yes'),
            ('no', 'No'),
            ('limited', 'Limited'),
        )
    in_state_tuition = models.CharField(max_length=128, null=True, blank=True, default=None, choices=TUITION_CHOICES, verbose_name="Can undocumented students access in-state tuition at public colleges?")
    in_state_tuition_notes = models.CharField(max_length=2048, null=True, blank=True, verbose_name="If limted, please explain.", default=None)
    drivers_licenses = models.NullBooleanField(verbose_name="Can undocumented immigrants get drivers' licenses?")
    other_ids_available = models.NullBooleanField(verbose_name="If no, are other IDs available to them?")
    other_ids_limitations = models.CharField(max_length=2048, null=True, blank=True, verbose_name="What are the limitations to these IDs (e.g. Do police recognize them as an official ID? Can they buy alcohol with this ID? etc.)?")


class City(BaseTerritory):
    LEGAL_REPRESENTATION_CHOICES = (
            ('yes', 'Yes'),
            ('at-immigrants-expense', 'At Immigrants\' Expense'),
            ('no', 'No'),
        )
    state = models.ForeignKey(State)
    form_i247n = models.NullBooleanField(verbose_name="Form I-247N, Request for Voluntary Notification of Release of Suspected Priority Alien")
    form_i247d = models.NullBooleanField(verbose_name="Form I-247D, Immigration Detainer - Request for Voluntary Action")
    form_i247x = models.NullBooleanField(verbose_name="Form I-247-X, Request for Voluntary Transfer")
    legal_representation = models.CharField(max_length=128, null=True, blank=True, default=None, choices=LEGAL_REPRESENTATION_CHOICES)
    restrictions_on_social_services = models.NullBooleanField(verbose_name="Are there restrictions on social services (library cards, local IDs, school registration, etc.) for undocumented immigrants?")
    restrictions_on_social_services_notes = models.CharField(max_length=2048, null=True, blank=True, default=None, verbose_name="If yes, what?")

    class Meta:
        verbose_name_plural = "Cities"
