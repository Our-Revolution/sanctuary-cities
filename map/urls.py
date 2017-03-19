from django.conf.urls import url
from map.views import *

urlpatterns = [    
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'map', MapView.as_view(), name="map"),
    url(r'^api/1/territories', TerritoriesView.as_view(), name="territories")
]
