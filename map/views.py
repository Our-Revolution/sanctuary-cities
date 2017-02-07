from django.contrib.gis.db.models.functions import AsGeoJSON
from django.db.models.expressions import RawSQL
from django.views.generic import TemplateView
from .models import City, County, State



class MapView(TemplateView):
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)

        # states
        simplified = RawSQL('ST_Simplify(map_state.geom, 0.0007)', ())
        simplified.srid = True
        context['states'] = State.objects \
                                    .annotate(simplified=simplified).annotate(geojson=AsGeoJSON('simplified', precision=3)) \
                                    .filter(geom__isnull=False, limited_ice_cooperation__isnull=False)

        # counties
        simplified = RawSQL('ST_Simplify(map_county.geom, 0.0007)', ())
        simplified.srid = True
        context['counties'] = County.objects.select_related('state').defer('state__geom') \
                                    .annotate(simplified=simplified).annotate(geojson=AsGeoJSON('simplified', precision=3)) \
                                    .filter(geom__isnull=False, jails_honor_ice_detainers__isnull=False)

        # # cities
        simplified = RawSQL('ST_Simplify(map_city.geom, 0.0005)', ())
        simplified.srid = True
        context['cities'] = City.objects.select_related('state').defer('state__geom') \
                                    .annotate(simplified=simplified).annotate(geojson=AsGeoJSON('simplified', precision=4)) \
                                    .filter(geom__isnull=False, limited_ice_cooperation__isnull=False)


        return context