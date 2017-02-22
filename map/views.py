from django.contrib.gis.db.models.functions import AsGeoJSON
from django.contrib.gis.geos import Point
from django.core.serializers import serialize
from django.db.models.expressions import RawSQL
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse, Http404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, TemplateView, View
from djgeojson.serializers import Serializer as GeoJSONSerializer
from .models import City, County, State
import json




@method_decorator(cache_page(300), name='dispatch')
class MapView(TemplateView):
    template_name = "map/index.html"

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        serializer = GeoJSONSerializer()
        
        # states
        context['states'] = serializer.serialize(State.objects.filter(geom__isnull=False, limited_ice_cooperation__isnull=False), simplify=0.0007, precision=3, geometry_field='geom', properties=filter(lambda f: f not in ['geom', 'id'], map(lambda f: f.name, State._meta.local_fields)))        
                                    
        # counties  
        context['counties'] = serializer.serialize(County.objects.filter(geom__isnull=False, jails_honor_ice_detainers__isnull=False), simplify=0.0007, precision=3, geometry_field='geom', properties=filter(lambda f: f not in ['geom', 'id'], map(lambda f: f.name, County._meta.local_fields)))

        # cities
        context['cities'] = serializer.serialize(City.objects.filter(limited_ice_cooperation__isnull=False), simplify=0.0007, precision=3, geometry_field='geom', properties=filter(lambda f: f not in ['geom', 'id'], map(lambda f: f.name, City._meta.local_fields)))

        return context


class TerritoriesView(View):

    def get(self, request, *args, **kwargs):
        lat, lng = float(request.GET.get('lat')), float(request.GET.get('lng'))

        point = Point(x=lng, y=lat, srid=4326)
        context = {}

        serializer = GeoJSONSerializer()

        for model in [City, County, State]:
            context[model._meta.verbose_name_raw] = serializer.serialize(model.objects.filter(geom__contains=point), simplify=0.0007, precision=3, geometry_field='geom', properties=filter(lambda f: f not in ['geom', 'id'], map(lambda f: f.name, model._meta.local_fields)))
            
        return JsonResponse(context)





class MapDetailView(DetailView):

    def get_template_name(self):
        return "map/%s_detail.html" % self.object._meta.db_table
    
    def get_object(self):

        obj = None
        slug = self.kwargs.get(self.slug_url_kwarg)

        models = [City, County, State]
        slug_field = self.get_slug_field()

        for model in models:
            
            try:
                obj = model.objects.get(**{slug_field: slug})
            except model.DoesNotExist:
                continue

        if not obj:
            raise Http404("Could not find a place matching that URL.")

        return obj
