from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^research/get-started/', include('onboard.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'', include('map.urls', namespace="map")),
]
