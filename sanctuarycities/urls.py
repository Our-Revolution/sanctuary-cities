from django.conf.urls import url
from django.contrib import admin
from map.views import *

urlpatterns = [
    url(r'^$', MapView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<slug>[\w\-]+)$', MapDetailView.as_view()),
]
