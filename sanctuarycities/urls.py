from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'', include('map.urls', namespace="map")),
    url(r'^admin/', admin.site.urls),
]
