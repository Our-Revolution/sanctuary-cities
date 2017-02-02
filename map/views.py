from django.contrib.gis.db.models.functions import AsGeoJSON
from django.db.models.expressions import RawSQL
from django.views.generic import TemplateView
from .models import City



class MapView(TemplateView):
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        simplified = RawSQL('ST_Simplify(map_city.geom, 0.0005)', ())
        simplified.srid = True
        context['cities'] = City.objects.select_related('state').defer('state__geom') \
                                    .annotate(simplified=simplified,
                                            geojson=AsGeoJSON('simplified', precision=3)).all()
        return context