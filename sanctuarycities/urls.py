from django.conf.urls import url
from django.contrib import admin
from map.views import MapView

urlpatterns = [
    url(r'^$', MapView.as_view()),
    url(r'^admin/', admin.site.urls),
]
