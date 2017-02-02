from django.views.generic import TemplateView
from .models import City



class MapView(TemplateView):
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        cities = []
        for city in City.objects.select_related('state').defer('state__geom').all():
            city.geojson = city.geom.simplify(0.00001).geojson
            cities.append(city)
        context['cities'] = cities
        return context